import logging
import os
from collections import OrderedDict
import unittest
logger = logging.getLogger(__name__)


def lookup_environ_skip_status(marker):
    name = marker.name.upper()
    is_skip = os.environ.get("NO_" + name)
    if is_skip is not None:
        return bool(is_skip)
    return False


class _Marker:
    def __init__(self, name, fn, *, description=None):
        self.name = name
        self.reason = description or name
        self.fn = fn
        self.is_skip = None

    def skip_activate(self):
        self.is_skip = True

    def skip_deactivate(self):
        self.is_skip = False

    def __call__(self, test_item):
        if self.is_skip is None:
            self.is_skip = self.fn(self)
        return unittest.skipIf(self.is_skip, self.reason)(test_item)


class Repository:
    def __init__(self, fn):
        self.pool = OrderedDict()
        self.fn = fn
        self.registered_actions = {}

    def __getitem__(self, name):
        return self.pool[name]

    @property
    def markers(self):
        return self.pool.values()

    def create_marker(self, name, *, description=None):
        marker = self.pool[name] = _Marker(name, fn=self.fn, description=description)
        if name in self.registered_actions:
            getattr(marker, self.registered_actions[name])()
        elif "" in self.registered_actions:
            getattr(marker, self.registered_actions[""])()
        return marker

    def register_action(self, name, action):
        self.registered_actions[name] = action


class Manager:
    def __init__(self, repository):
        self.repository = repository

    def __getattr__(self, name):
        try:
            return self.repository[name]
        except KeyError:
            raise AttributeError(name)

    def create_marker(self, name, *, description=None):
        return self.repository.create_marker(name, description=description)

    def only(self, names):
        for name in names:
            self.repository.register_action(name, "skip_deactivate")
        self.repository.register_action("", "skip_activate")
        for marker in self:
            if marker.name in names:
                marker.skip_deactivate()

    def ignore(self, names):
        for name in names:
            self.repository.register_action(name, "skip_activate")
        for marker in self:
            if marker.name in names:
                marker.skip_activate()

    def __iter__(self):
        return iter(self.repository.markers)


class FluffyManager(Manager):
    def __getattr__(self, name):
        try:
            return self.repository[name]
        except KeyError:
            return self.create_marker(name)

    def freeze(self):
        self.__class__ = Manager


markers = FluffyManager(Repository(lookup_environ_skip_status))
