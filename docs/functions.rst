Functions
============

.. note:: 

    Functions cannot be declared inside a function.

A function is defined using the ``Function`` keyword:

.. code-block:: blitzbasic

    Function name%(arg1$, arg2# = 3.14)
        ; some statements...
    End Function

``name%(arg1$, arg2# = 3.14)`` is the **function signature**, which it contains:

    * ``name`` is the function name, can be any valid identifier.
    
    * ``%`` is the type of value returned by the function. If it is omitted,the function returns an integer value by default.
    
    * ``arg1$, arg2# = 3.14`` is a comma-separated list of arguments. ``arg1$`` is a **mandatory argument** with no default value. ``arg2#`` is an **optional argument** since it has a default value. Arguments are always local.

The statements between signature and ``End Function`` are the **function definition**. All ZiYue4D functions should have signature and definition.

A function may use the ``Return`` statement to return a result. ``Return`` may optionally be followed by an expression.

If there is no ``Return`` statement, or a ``Return`` without any expression is used, the function returns a default value of ``0`` for numeric functions, an empty string ``""`` for string functions, or a Null object for custom-type functions.

.. _extern-function:

Exteral function
------------------------

**External functions** are implemented in other programming languages, which are to be called by ZiYue4D program.

Using ``Extern`` keyword before its signature to declare an external function. External functions should not have a function definition. This concept is designed for replacing ``.decls`` in Blitz3D.

The example below shows a declaration of an external function.

.. code-block:: ziyue4d

    Extern MessageBox%(title$, msg$)

.. _function-overloading:

Function overloading
------------------------

.. attention:: 

    :ref:`extern-function` does not support overloading.

When multiple functions need to share the same name, ZiYue4D will check its arguments to determine whether it is overridable. Basically, the regulation of overloading is:

1. The functions share the same name.
2. Their number of mandatory arguments and optional arguments is unique.
3. The return value type and argument types are irrelevant to overloading. 

The example below shows the overloading. The first and the second are valid since they have different counts of mandatory and optional arguments. The third one is invalid, in contrast, even though its argument types are unique.

.. code-block:: ziyue4d
    :emphasize-lines: 11-15

    /* This function has 2 mandatory args, and 0 optional */
    Function foo$(arg1%, arg2%)
        ; some statements
    End Function

    /* This function has 1 mandatory args, and 1 optional */
    Function foo%(arg1$, arg2# = 3.14)
        ; some statements
    End Function

    ; Invalid overloading!
    /* This function has 1 mandatory args, and 1 optional*/
    Function foo#(arg1%, arg2$ = "3.14")
        ; some statements
    End Function
