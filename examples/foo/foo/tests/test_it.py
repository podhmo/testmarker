import unittest
from testmarker import mark


@mark.a
class Test0(unittest.TestCase):
    def test_it(self):
        pass


@mark.b
class Test1(unittest.TestCase):
    def test_it(self):
        pass


@mark.c
class Test2(unittest.TestCase):
    def test_it(self):
        pass


@mark.d
class Test3(unittest.TestCase):
    def test_it(self):
        pass


@mark.e
class Test4(unittest.TestCase):
    def test_it(self):
        pass


@mark("f", description="f is default skipped", skip=True)
class Test5(unittest.TestCase):
    def test_it(self):
        pass


class Test6(unittest.TestCase):
    def test_it(self):
        pass
