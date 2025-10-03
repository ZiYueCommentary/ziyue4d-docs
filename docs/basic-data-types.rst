Basic Data Types
===================================

There are 4 basic data types:

.. _integer:

Integer
----------------------

**Integer** are numeric values with no fractional part in them, ``int32`` in essence. For example: ``5``, ``-10``, ``0`` are integer values. All integer values in the program must be in the range ``-2147483648`` to ``+2147483647``. 

.. _digit_separator :

Digit separator
^^^^^^^^^^^^^^^^^^

**Digit separator** ``_`` can be used to separate a long literal number. For example, ``3_14_15_926`` is equavlant to ``31415926``.

.. _float:

Float
----------------------

**Float** are numeric values that include a fractional part. For example: ``.5``, ``-10.1``, ``0.0`` are all floating point values. You can also use :ref:`digit_separator` to separate literal.

.. _string:

String
-------------------

**String** are used to contain text. For example: ``"Hello World!"``.

Escape characters
^^^^^^^^^^^^^^^^^^^

You need to use **escape characters** to insert ``"`` or line feed in a literal string. This is a modern alternative to ``Chr`` function.

+-----------+-----------------+
| Character |      Result     |
+===========+=================+
|   ``\'``  | single quote    |
+-----------+-----------------+
|   ``\"``  | double quote    |
+-----------+-----------------+
|   ``\\``  | backslash       |
+-----------+-----------------+
|   ``\n``  | new line        |
+-----------+-----------------+
|   ``\r``  | carriage return |
+-----------+-----------------+
|   ``\t``  | tab             |
+-----------+-----------------+
|   ``\b``  | backspace       |
+-----------+-----------------+
|   ``\f``  | form feed       |
+-----------+-----------------+

The example below shows the usage of the escape character. Both of them print ``Hello"World!``. It is recommended to replace the legacy BlitzBasic method with escape characters, as it processes at compile time and produces fewer string objects at runtime.

.. code-block:: ziyue4d
    :emphasize-lines: 1
    :linenos:

    Print("Hello\"World!")
    Print("Hello" + Chr(34) + "World!")

.. _pointer:

Pointer
-----------------

**Pointer** are objects that store a memory address. This type is for solving that pointers are stored in an integer in BlitzBasic.

When assigning a pointer to an integer variable, ZiYue4D will automatically raise the variable to pointer type.

Implicit conversion
-------------------

**Implicit conversion** plays an important role in ZiYue4D. Most of the conversion in ZiYue4D is implicit, and observes the same rules as in BlitzBasic.

When an binary operation involves two different data types, ZiYue4D will automatically convert one of the operands to the other type. The conversion rules are as follows:

* Pointers cannot be converted to any other type, and no other type can be converted to pointers. [#f1]_
* If one operand is a string, the other is converted to a string.
* If one operand is floating point, the other is converted to floating point.
* Otherwise, both operands are integers.

+------------+---------+-------+--------+---------+
| From \\ To | Integer | Float | String | Pointer |
+============+=========+=======+========+=========+
| Integer    | ✅      | ✅    | ✅     | ❌      |
+------------+---------+-------+--------+---------+
| Float      |❗ [#f2]_| ✅    | ✅     | ❌      |
+------------+---------+-------+--------+---------+
| String     | ❌      | ❌    | ✅     | ❌      |
+------------+---------+-------+--------+---------+
| Pointer    |❗ [#f3]_| ❌    | ❌     | ✅      |
+------------+---------+-------+--------+---------+

.. rubric:: Footnotes
.. [#f1] When assigning a pointer to an integer variable, ZiYue4D will automatically raise the variable to pointer type.
.. [#f2] Float to Integer will round to the nearest integer. This may lead to loss of accuracy.
.. [#f3] Storing a pointer in an integer is deprecated BlitzBasic practice. ZiYue4D will raise the variable to pointer type automatically.