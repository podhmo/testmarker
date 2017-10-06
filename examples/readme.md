ignore

```
$ (cd foo; python setup.py test --ignore a,b,c)
running test
running egg_info
writing foo.egg-info/PKG-INFO
writing dependency_links to foo.egg-info/dependency_links.txt
writing top-level names to foo.egg-info/top_level.txt
reading manifest file 'foo.egg-info/SOURCES.txt'
writing manifest file 'foo.egg-info/SOURCES.txt'
running build_ext
test_it (foo.tests.test_it.Test0) ... skipped 'a'
test_it (foo.tests.test_it.Test1) ... skipped 'b'
test_it (foo.tests.test_it.Test2) ... skipped 'c'
test_it (foo.tests.test_it.Test3) ... ok
test_it (foo.tests.test_it.Test4) ... ok
test_it (foo.tests.test_it.Test5) ... skipped 'f is default skipped'

----------------------------------------------------------------------
Ran 6 tests in 0.000s

OK (skipped=4)
```

only

```
$ (cd foo; python setup.py test --only a,b)
running test
running egg_info
writing foo.egg-info/PKG-INFO
writing dependency_links to foo.egg-info/dependency_links.txt
writing top-level names to foo.egg-info/top_level.txt
reading manifest file 'foo.egg-info/SOURCES.txt'
writing manifest file 'foo.egg-info/SOURCES.txt'
running build_ext
test_it (foo.tests.test_it.Test0) ... ok
test_it (foo.tests.test_it.Test1) ... ok
test_it (foo.tests.test_it.Test2) ... skipped 'c'
test_it (foo.tests.test_it.Test3) ... skipped 'd'
test_it (foo.tests.test_it.Test4) ... skipped 'e'
test_it (foo.tests.test_it.Test5) ... skipped 'f is default skipped'

----------------------------------------------------------------------
Ran 6 tests in 0.000s

OK (skipped=4)
```
