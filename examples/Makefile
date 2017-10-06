PKG = foo


run:
	(cd ${PKG}; python setup.py test)
	(cd ${PKG}; python setup.py test --ignore a,b,c)
	(cd ${PKG}; python setup.py test --only a,b)

run2:
	(cd ${PKG}; F=1 python setup.py test)

help:
	(cd ${PKG}; python setup.py --help test)
