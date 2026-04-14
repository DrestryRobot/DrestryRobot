VisionMaster 有关byte的报错
===========================
.. warning:: 

    - C:\Program Files (x86)\Windows Kits\10\Include\10.0.19041.0\shared\rpcndr.h:192: error: C2872: “byte”: 不明确的符号
    - C:\Program Files (x86)\Windows Kits\10\include\10.0.19041.0\shared\rpcndr.h(192): error C2872: “byte”: 不明确的符号
    - C:\Program Files (x86)\Windows Kits\10\include\10.0.19041.0\shared\rpcndr.h(191): note: 可能是“unsigned char byte”
    - C:\Program Files (x86)\Microsoft Visual Studio\2019\Professional\VC\Tools\MSVC\14.29.30133\include\cstddef(28): note: 或    “std::byte”

双击索引至报错位置，注释第191行代码（或第192行），如果下次构建再次出现类似的报错，尝试取消第191行注释（或第192行）。