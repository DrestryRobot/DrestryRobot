C语言入门
=========
.. contents:: 目录

C语言入门
-----------
C语言入门，介绍基本的常用的C语言编写语句，会用这些基本就会写C、C++的工程代码了，主要还是活学活用，举一反三。


常用语句
-------
变量定义
~~~~~~~~
::

	int a=0; //整数型
	float b=0; //浮点型
	double c=0; //双精度浮点型
	string d; //字符串型

条件语句
~~~~~~~~
::
	
	if(count<9)
	{
		a = 0;
	}
	else if(count>=9 && count<15)
	{
		a = 1;
	}
	else
	{
		a = 2;
	}

循环语句
~~~~~~~~
::
	
	while(1) // 死循环
	{
		a = 0;
	}

	for(int i=1; i<10; i++) // 循环给定次数
	{
		a = 1;
	}

函数定义
~~~~~~~~
::

	/* 无返回值的函数 */
	void function(); // 函数声明
	
	void function() // 函数定义
	{
		a = 0;
	}

	/* 有返回值的函数 */
	int function(int a); // 整数型函数声明
	float function(float a); // 浮点型函数声明
	double function(double a); // 双精度浮点型函数声明
	
	int function(int a) // 整数型函数定义
	{
		b = a;
		return b;
	}
	float function(float a) // 浮点型函数定义
	{
		b = a;
		return b;
	}
	double function(double a) // 双精度浮点型函数定义
	{
		b = a;
		return b;
	}

结构体定义
~~~~~~~~~~~
::

	th









