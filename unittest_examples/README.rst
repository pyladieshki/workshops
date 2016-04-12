----------------------
Why writing **tests**?
----------------------
1.  The code **works** if the tests **pass**. No need to overthink -> savings of time & effort

2.  Visual feedback - we all like to see results

3.  Tests help you in **documenting** things, as well as breaking things down into smaller pieces

4.  Last, but not least - they save you potentially from *hours of debugging*!
    Common WRONG assumption: writing tests requires a lot of time and effort. In the long run they DO save you time!

--------------------------------------------------------------------------
How to **start** with writing **unit tests** using Python unittest module:
--------------------------------------------------------------------------

- import unittest
- write a class, which inherits from unittest.TestClass
- write methods inside the class, which each test one single operation, functionality, etc.
- run the tests by python3 -m unittest (run in the parent dir of the module)
  OR python3 -m unittest test_module.TestClassName.test_method

----------------------------------------
**Best practices** to running unit tests
----------------------------------------

a.  Each test must be independent from the rest (e.g., no dependency on the order of running)

b.  Test smallest functionalities

c.  Same results must be observed on every run

d.  Naming convention: test classes should start with the word "Test". The class methods must start with the word "test" and then must be followed by descriptive words of what you are testing.

e.  It is better to have slow tests, than no tests at all





