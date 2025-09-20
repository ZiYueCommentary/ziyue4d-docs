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

When an operation involves two different data types, ZiYue4D will automatically convert one of the operands to the other type. The conversion rules are as follows:

+------------+---------+-------+--------+---------+
| From \\ To | Integer | Float | String | Pointer |
+============+=========+=======+========+=========+
| Integer    | ✅      | ✅    | ✅     | ❌      |
+------------+---------+-------+--------+---------+
| Float      |❗ [#f1]_| ✅    | ✅     | ❌      |
+------------+---------+-------+--------+---------+
| String     | ❌      | ❌    | ✅     | ❌      |
+------------+---------+-------+--------+---------+
| Pointer    |❗ [#f2]_| ❌    | ❌     | ✅      |
+------------+---------+-------+--------+---------+

.. rubric:: Footnotes
.. [#f1] Float to Integer conversion truncates the fractional part. This may leads to loss of accuracy.
.. [#f2] Storing a pointer in an integer is deprecated BlitzBasic practice. ZiYue4D will raise the variable to Pointer type automatically.