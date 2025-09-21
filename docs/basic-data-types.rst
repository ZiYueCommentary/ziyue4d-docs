Basic Data Types
===================================

There are 4 basic data types:

- **Integer** are numeric values with no fractional part in them. For example: 5,-10,0 are integer values. All integer values in your program must be in the range -2147483648 to +2147483647. 

- **Float** are numeric values that include a fractional part. For example: .5, -10.1, 0.0 are all floating point values. 

- **String** are used to contain text. For example: "Hello World!".

- **Pointer** are objects that store a memory address. This type is for solving that pointers are stored in an integer in BlitzBasic.

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