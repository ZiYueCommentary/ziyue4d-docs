.. _identifiers:

Identifiers
=================

Identifiers are used for constant names, variable names, array names, function names, and custom type names.

Identifiers supports Unicode characters, but not start with an number. For example, ``Hello``, ``player1``, ``time_to_live``, ``__var``, ``变量`` are all valid identifiers.

Identifiers are not case-sensitive. For example, ``Test``, ``TEST`` and ``test`` are all the same identifiers. Note that this works for alphabets only, Unicode identifiers may be case-sensitive.

It is allowed for identifiers to be reused for functions and variables. For example, you can have a variable called ``test``, a function called ``test``. When the identifier is not inside a function call, it will be seen as a function by default.

The example below shows how ZiYue4D distinguishes variables and functions. In line 1, ``Foo`` is a function, and ``bar`` is a variable. In line 2, ``Foo`` is a function, and ``bar`` is a function. However, the third line is suggested, since it clearly shows which one is variable.

.. code-block:: ziyue4d
    :emphasize-lines: 3
    :linenos:

    Foo bar, 3.14
    Foo bar(), 3.14
    Foo(bar(), 3.14)