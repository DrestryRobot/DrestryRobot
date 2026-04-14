VisionMaster UTF-8编码问题
===========================
报错信息
^^^^^^^^^
.. warning::

    - C:/Program Files/VisionMaster4.2.0/Development/V4.x/Includes/MVD_ErrorDefine.h:1: warning: C4828: 文件包含在偏移 0x8f 处开始的字符，该字符在当前源字符集中无效(代码页 65001)。

解决办法
^^^^^^^^^
使用 PowerShell 批量转换include文件夹内.c文件为UTF-8格式

打开 PowerShell（Win + R → 输入 powershell → 回车）。运行以下命令：

.. code:: bash

    Get-ChildItem -Path "C:\Program Files\VisionMaster4.2.0\Development\V4.x\Includes" -Filter *.h | ForEach-Object {
    $content = Get-Content $_.FullName
    $content | Set-Content -Encoding UTF8 $_.FullName
    }

    Get-ChildItem -Path "C:\Program Files\VisionMaster4.2.0\Development\V4.x\Includes" -Filter *.c | ForEach-Object {
        $content = Get-Content $_.FullName
        $content | Set-Content -Encoding UTF8 $_.FullName
    }