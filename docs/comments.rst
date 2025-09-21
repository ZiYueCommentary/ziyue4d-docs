Comments
===================================

You add comments to your programs using the ``;`` character. Everything following ``;`` until the end of the line will be ignored.

``/* */`` is also supported for block comments. Everything between ``/*`` and ``*/`` will be ignored, even if it spans multiple lines. Block comments do not nest.

.. code-block:: blitzbasic

    Function Redraw(param% /* an integer parameter */)
        ; do something...
    End Function 

