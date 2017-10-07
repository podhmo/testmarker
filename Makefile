readme:
	kamidana _readme.rst.j2 -a kamidana.additionals.reader | sed "s@${HOME}@\$$HOME@" | tee README.rst
