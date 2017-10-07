PKG = foo


run:
	(cd ${PKG}; python setup.py test)
	(cd ${PKG}; python setup.py test --ignore a,b,c)
	(cd ${PKG}; python setup.py test --only a,b)

run2:
	(cd ${PKG}; F=1 python setup.py test)

run3:
	python -m testmarker discover foo --verbose
	python -m testmarker discover foo --ignore a,b --ignore c --verbose
	python -m testmarker discover foo --only a,b --verbose

help:
	(cd ${PKG}; python setup.py --help test)
