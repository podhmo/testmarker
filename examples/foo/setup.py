from setuptools import setup, find_packages
from testmarker.setupcmd import test

setup(
    name='foo',
    version='0.0',
    description='-',
    packages=find_packages(exclude=["foo.tests"]),
    test_suite="foo.tests",
    cmdclass={"test": test}
)
