from setuptools.command.test import test as _test


class test(_test):
    user_options = _test.user_options + [
        ("markers", None, "listing registered markers"),
        ("ignore=", None, "ignore marked"),
        ("only=", None, "only marked"),
    ]

    def initialize_options(self):
        self.ignore = None
        self.only = None
        self.markers = False
        super().initialize_options()

    def run_listing_marker(self, markers):
        for m in markers:
            print(m.name, "--", m.description)

    def get_markers(self):
        from testmarker import markers
        return markers

    def run(self):
        markers = self.get_markers()
        if self.markers:
            return self.run_listing_markers(markers)
        elif self.only is not None:
            markers.only([x.strip() for x in self.only.split(",")])
        elif self.ignore is not None:
            markers.ignore([x.strip() for x in self.ignore.split(",")])
        return super().run()
