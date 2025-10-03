Variables
===============

**Variables** may be of any basic data type, or a custom type. A variable's type is determined by a special character that follows its identifier. These special characters are called **type tags**.

+-----+----------------+
| Tag |      Type      |
+=====+================+
|``%``| :ref:`integer` |
+-----+----------------+
|``#``| :ref:`float`   |
+-----+----------------+
|``$``|  :ref:`string` |
+-----+----------------+
|``@``| :ref:`pointer` |
+-----+----------------+

The type tag only needs to be added the first time you use a variable, after that you can leave the type tag off if you wish.

If you don't supply a type tag the first time a variable is used, the variable defaults to an integer.

It is illegal to use the same variable name with a different type. For example, if you already have an integer variable called ``name%``, it is illegal to also have a string variable called ``name$``.

Assignment
-------------

You can use ``=`` to assign a value to a variable. For example: ``score% = 0`` will assign the value ``0`` to the integer variable ``score``. This expression returns the assigned value, which means you can do assignment and comparison in a single line.

.. code-block:: ziyue4d

    If (foo% = 2) <> 0 Then Print("do something...")

Scope
-------------

Variables may also be either ``Global``, or ``Local``. This refers to where in a program a variable may be used. ``Global`` variables can be used from anywhere in the program. ``Local`` variables can only be used within the function they are created in.

The ``Global`` keyword is used to define one or more global variables. For example: 

.. code-block:: ziyue4d

    Global Score# = 0.0, Lives% = 3, Player$ = "player"

Defines 3 global variables.

Similarly, ``Local`` is used to define local variables: 

.. code-block:: ziyue4d

    Local temp_x# = x, temp_y# = y

The operations above is called **explicit definition**. It indicates variable declaration, and throws a compile error when defining it multiple times. If you use a variable without defining it as either local or global, it defaults to being local. This operation is called **implicit definition**. This is not suggested since it creates another variable when you have a typo, leading to unexpected results.

It is strongly recommended to use ``Local`` or ``Global`` to declare variables, since it is a safer practice. You can also turn safe check in compiler to force the program to use explicit definition, and disable implicit definition.