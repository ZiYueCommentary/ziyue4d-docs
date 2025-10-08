Constants
================

**Constants** are fixed values that  will not change during the course of the program. These are useful when you want to name immutable values.

Constants can be most of :ref:`basic-data-types`, excluding :ref:`pointer`. Expression of constants must be evaluated during compilation.

The ``Const`` keyword is used to assign an identifier to a constant. For example:

.. code-block:: ziyue4d

    Const width% = 640, height% = 480

You can then use the more readable ``width`` and ``height`` throughout your program instead of ``640`` and ``480``. Also, if you decide to change the ``width`` and ``height`` values, you only have to do so at one place in the program.

.. attention:: 

    Using another constant in the constant expression is undefined behavior, since the initialization order does not depend on their order in the source code.

    The example below shows this behavior. When the compiler initializes ``foo%`` before ``bar%``, this code will work properly. Conversely, it causes a compiler error.

    .. code-block:: ziyue4d

        Const foo% = 100
        Const bar% = foo
