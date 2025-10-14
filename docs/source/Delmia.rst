Delmia
=========
.. contents:: 目录

Delmia
--------
Delmia，是一个兼具设计与仿真的工业软件，广泛应用于航空航天领域，功能丰富的行业级生产力工具。

Delmia二次开发
----------------
下面介绍delmia二次开发的三种方法及相关案例：

基于Python的二次开发
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
代码功能：新建一个Part文件。

运行环境：需要安装python和pywin32库，打开delmia软件后运行代码。

开发特性：Delmia二次开发最佳选择，编程简单，对接Delmia底层API接口。

.. code:: python

    import win32com.client
    delmia = win32com.client.Dispatch('delmia.application')
    delmia.documents.add('Part')

基于VBA的二次开发
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
代码功能：新建一个Part文件。

运行环境：新建代码为CATScript宏脚本文件，打开delmia软件后运行VBA宏代码。

开发特性：Delmia二次开发入门选择，直接在Delmia软件中编程，但是VBA对于SetDOFValues等Delmia底层API接口不支持，功能存在缺失。

.. code:: c#

    Sub CATMain()

        Dim Part As PartDocument
        Set Part = delmia.Documents.Add("Part")

    End Sub

基于C++的二次开发
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
代码功能：新建一个Part文件。

运行环境：Qt中新建C++工程项目，打开delmia软件后运行。

开发特性：Delmia二次开发高阶选择，用C/C++编程，依赖于Qt的QAxObject类，不支持Delmia中的CATSafeArrayVariant变量类型，功能存在缺失。

.. code:: c++

    #include <comdef.h>
    #include <QAxObject>

    int main()
    {
        QAxObject* catia = new QAxObject("DELMIA.Application", this);
        QAxObject* documents = catia->querySubObject("Documents");
        QAxObject* Part = documents->querySubObject("Add(const QString&)", "Part");
    }
