C++
=========
.. contents:: 目录

C++
----
C++，和C语言有些类似，但很多用法都变了，当然也可以在C++代码中写C代码。

C++try的用法
-------------
在C++中，try 关键字用于异常处理，它标志着一个 **尝试执行的代码块**，如果该代码块发生异常，程序可以通过 catch 语句来捕获并处理异常，而不是直接崩溃。

.. code:: c++

    #include <iostream>

    void divide(int a, int b) {
        try {
            if (b == 0) {
                throw std::runtime_error("除数不能为零");
            }
            std::cout << "结果: " << a / b << std::endl;
        } catch (const std::exception& e) {
            std::cerr << "异常: " << e.what() << std::endl;
        }
    }

    int main() {
        divide(10, 2);  // 正常执行
        divide(10, 0);  // 触发异常
        return 0;
    }

说明：
- try 语句块包含可能 **产生异常的代码**。

- throw 关键字用于 **抛出异常**，它可以是一个标准异常 (std::runtime_error 等) 或者是自定义异常。

- catch 语句块 **处理异常**，它会捕获 throw 抛出的异常对象，并执行适当的错误处理。

- 异常对象可以是 **基本数据类型**（如 int）、**标准异常类**（如 std::exception），或 **用户自定义的类**。