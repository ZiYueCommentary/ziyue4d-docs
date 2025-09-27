Unsafe operations
====================

**Unsafe operations** such as retrieving pointers or converting a pointer to integer, are not recommended for use. In most cases, unsafe operations are not required. Using them improperly will cause undefined behavior, and even crash the program.

Function pointer
----------------------------

.. warning:: 

    Retrieving pointer of function which used :ref:`function-overloading` is undefined behavior.

Using ``&`` unary operator on a function identifier to retrieve its pointer.

The example below shows retrieve a function pointer.

.. code-block:: ziyue4d
    :emphasize-lines: 5

    Function foo%()
        ; some statements...
    End Function

    ptr@ = &foo