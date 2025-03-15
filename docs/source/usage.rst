.. Usage
.. =====

.. .. _installation:

.. Installation
.. ------------

.. 中钱钱钱To use Lumache, first install it using pip:

.. .. code-block:: console

..    (.venv) $ pip install lumache

.. Creating recipes
.. ----------------

.. To retrieve a list of random ingredients,
.. you can use the ``lumache.get_random_ingredients()`` function:

.. .. autofunction:: lumache.get_random_ingredients

.. The ``kind`` parameter should be either ``"meat"``, ``"fish"``,
.. or ``"veggies"``. Otherwise, :py:func:`lumache.get_random_ingredients`
.. will raise an exception.

.. .. autoexception:: lumache.InvalidKindError

.. For example:

.. >>> import lumache
.. >>> lumache.get_random_ingredients()
.. ['shells', 'gorgonzola', 'parsley']

使用指南
=========

.. _installation:

安装
------------

中钱钱钱要使用 Lumache，请首先通过 pip 安装它：

.. code-block:: console

   (.venv) $ pip install lumache

创建食谱
----------------

要获取随机食材列表，可以使用 ``lumache.get_random_ingredients()`` 函数：

.. autofunction:: lumache.get_random_ingredients

The ``kind`` parameter should be either ``"meat"``, ``"fish"``,
or ``"veggies"``. Otherwise, :py:func:`lumache.get_random_ingredients`
will raise an exception.

.. autoexception:: lumache.InvalidKindError

例如：

>>> import lumache
>>> lumache.get_random_ingredients()
['shells', 'gorgonzola', 'parsley']


