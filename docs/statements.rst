Statements
===============

**Statements** are fragments of the program that are executed in sequence, usually contains a **condition expression**.

.. attention:: 

    ``=`` operator in condition expression represents relational operation "equals", equavlant to ``==``.

Selection statements
-------------------------

A **selection statement** chooses between one of several control flows.

If statement
^^^^^^^^^^^^^^^^

**If statement** conditionally executes another statement.

.. code-block:: ziyue4d

    If foo = 3.14 Then 
        Print("true statement") 
    ElseIf foo = 1.14 Then
        Print("elseif statement")
    Else
        Print("false statement")
    EndIf

``foo = 3.14`` is a **condition expression**, when the expression is not ``0``, the **true statement** will be executed. Condition expression must returns an :ref:`integer` value. ``Then`` keyword is optional.

You can add optional ``ElseIf`` and ``Else`` parts for different conditions. These statements can execute one at the same time. Note that ``Else`` can only be used once.

You can also fold the if statement into a single line. Note that no ``EndIf`` required.

.. code-block:: ziyue4d

    If foo = 3.14 Then Print("true statement") Else Print("false statement")

Iteration statements
----------------------
An **iteration statement** repeatedly executes some code.

While statement
^^^^^^^^^^^^^^^^^^



Repeat statement
^^^^^^^^^^^^^^^^