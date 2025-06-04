VisionMaster
=======================
.. contents:: 目录

VisionMaster
-------------
VisionMaster，是一个视觉算法软件，提供可视化流程界面，支持海康威视系列相机。不仅可以直接生成工程项目文件，向外发送数据，还支持二次开发，不通过VisionMaster去执行流程再发送数据给上位机程序，而是直接调用VisionMaster目录文件夹给的库和头文件，编写二次开发程序，实现利用程序执行流程并读取结果的功能。

UTF-8编码问题
---------------
报错
~~~~~
D:\FileData\VisionMaster4.4.0\Development\V4.x\Includes\MVD_ErrorDefine.h:1: warning: C4828: 文件包含在偏移 0x8f 处开始的字符，该字符在当前源字符集中无效(代码页 65001)。

解决办法
~~~~~~~~~
使用 PowerShell 批量转换include文件夹内.c文件为UTF-8格式

打开 PowerShell（Win + R → 输入 powershell → 回车）。运行以下命令：

::

    Get-ChildItem -Path "D:\FileData\VisionMaster4.4.0\Development\V4.x\Includes" -Filter *.h | ForEach-Object {
    $content = Get-Content $_.FullName
    $content | Set-Content -Encoding UTF8 $_.FullName
    }

    Get-ChildItem -Path "D:\FileData\VisionMaster4.4.0\Development\V4.x\Includes" -Filter *.c | ForEach-Object {
        $content = Get-Content $_.FullName
        $content | Set-Content -Encoding UTF8 $_.FullName
    }



示例代码
----------
.cpp
~~~~~~~~
.. code:: C

    #include "IVmSolution.h"
    #include "IVmProcedure.h"
    #include "VMException.h"

    using namespace VisionMasterSDK;
    using namespace VisionMasterSDK::VmSolution;
    using namespace VisionMasterSDK::VmProcedure;

    int main(int argc, char *argv[])
    {
        try
        {
            //加载方案，仅支持绝对路径，编码格式UTF-8
            IVmSolution * pVmSol = LoadSolution("D:\\204Clean\\jishu\\shiju\\204Clean.sol", "");
            if (NULL == pVmSol)
            {
                return IMVS_EC_NULL_PTR;
            }

            //使用流程名称获取流程对象
            IVmProcedure * pPrcObj = (IVmProcedure*)(*pVmSol)["流程1"];
            if (NULL == pPrcObj)
            {
                return IMVS_EC_NULL_PTR;
            }

            //获取流程所有模块信息
            ModuleInfoList * pModuList = pPrcObj->GetAllModuleList();

            //获取流程本层级模块信息，不包含Group内部模块
            ModuleInfoList * pModuListThisLayer = pPrcObj->GetProcedureModuleList();

            //禁用流程，禁用后流程不参与方案运行
            pPrcObj->DisableProcedure();

            //启用流程
            pPrcObj->EnableProcedure();

            //通过流程对象接口获取流程局部变量对象，用于设置/获取局部变量等
            CVariable * pVar = pPrcObj->GetLocalVariable();

            //通过流程对象接口获取流程参数对象，用于设置输入数据、设置/获取模块参数等
            IMVSProcedureParams *pParam = pPrcObj->GetParamObj();

            //流程同步执行一次
            pPrcObj->Run();

            //通过流程对象接口获取流程结果对象，用于获取流程输出
            //注意每次流程执行后，通过重新获取结果对象刷新其中输出数据
            //该操作存在耗时，建议获取结果对象后，直接使用对象获取具体输出数据
            IMVSProcedureResults *pRes = pPrcObj->GetResult();

            string out = std::to_string(pRes->GetOutputFloat("out").pFloatVal[0]);
            std::cout<<"out1:" << out <<std::endl;

            string ocrResult = pRes->GetOutputString("out2").astStringVal[0].strValue;
            std::cout<<"out2:" << ocrResult <<std::endl;

            string ocrNum = std::to_string(pRes->GetOutputInt("out3").pIntVal[0]);
            std::cout<<"out3:" << ocrNum <<std::endl;

            try {
                if(Result.nValueNum==0)
                {
                virsualCalibrationFlag = false;
                std::cout<<"Calibration failed!"<<endl;
                }else
                {
                virsualCalibrationFlag = true;
                float angle = Result.pFloatVal[10];
                // DebugStringData(Result.astStringVal[0]);
                // float angle = ConvertStringToFloat_CPP(Result.astStringVal[0]);
                std::cout<<"angle:" << angle <<std::endl;
                }
            } catch (std::exception) {
                std::cout<<"Calibration failed!!"<<endl;
            }

            //退出程序前释放所有资源，注意避免在析构函数中调用
            DisposeResource();
        }
        catch (CVmException vmex)
        {
            return vmex.GetErrorCode();
        }
        catch (...)
        {
            return IMVS_EC_UNKNOWN;
        }

        return IMVS_EC_OK;
    }


