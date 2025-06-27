I2C通信
============
.. contents:: 目录

I2C通信
---------
I2C通信，利用 **SCL** 和 **SDA** 引脚进行的通信。

I2C通信代码实现
-----------------
.. code:: c

    #include "stm32f1xx_hal.h"
    #include "IIC.h"

    /* 定义SCL和SDA的宏，已增加代码的可移植性和可阅读性 */
    #define IIC_SCL_1(IIC) HAL_GPIO_WritePin((IIC)->GPIO_Port, (IIC)->SCL_Pin, GPIO_PIN_SET)
    #define IIC_SCL_0(IIC) HAL_GPIO_WritePin((IIC)->GPIO_Port, (IIC)->SCL_Pin, GPIO_PIN_RESET)
    #define IIC_SDA_1(IIC) HAL_GPIO_WritePin((IIC)->GPIO_Port, (IIC)->SDA_Pin, GPIO_PIN_SET)
    #define IIC_SDA_0(IIC) HAL_GPIO_WritePin((IIC)->GPIO_Port, (IIC)->SDA_Pin, GPIO_PIN_RESET)
    #define IIC_SDA_READ(IIC) HAL_GPIO_ReadPin((IIC)->GPIO_Port, (IIC)->SDA_Pin)

    /* 定义IIC总线连接的GPIO端口, 用户只需要修改下面4行代码即可任意改变SCL和SDA的引脚 */
    IIC_TypeDef IIC1 = {GPIOB, GPIO_PIN_4, GPIO_PIN_5};
    IIC_TypeDef IIC2 = {GPIOB, GPIO_PIN_6, GPIO_PIN_7};
    IIC_TypeDef IIC3 = {GPIOB, GPIO_PIN_8, GPIO_PIN_9};

    /*
    *********************************************************************************************************
    *	函 数 名: IIC_Delay
    *	功能说明: IIC总线位延迟，最快400KHz
    *	形    参：无
    *	返 回 值: 无
    *********************************************************************************************************
    */
    static void IIC_Delay(void)
    {
        uint8_t i;

        /*　
            下面的时间是通过安富莱AX-Pro逻辑分析仪测试得到的。
            CPU主频72MHz时，在内部Flash运行, MDK工程不优化
            循环次数为10时，SCL频率 = 205KHz
            循环次数为7时，SCL频率 = 347KHz， SCL高电平时间1.5us，SCL低电平时间2.87us
            循环次数为5时，SCL频率 = 421KHz， SCL高电平时间1.25us，SCL低电平时间2.375us

        IAR工程编译效率高，不能设置为7
        */
        for (i = 0; i < 10; i++);
    }

    /*
    *********************************************************************************************************
    *	函 数 名: IIC_Start
    *	功能说明: CPU发起IIC总线启动信号
    *	形    参：无
    *	返 回 值: 无
    *********************************************************************************************************
    */
    void IIC_Start(IIC_TypeDef* IIC)
    {
        /* 当SCL高电平时，SDA出现一个下跳沿表示IIC总线启动信号 */
        IIC_SDA_1(IIC);
        IIC_SCL_1(IIC);
        IIC_Delay();
        IIC_SDA_0(IIC);
        IIC_Delay();
        IIC_SCL_0(IIC);
        IIC_Delay();
    }

    /*
    *********************************************************************************************************
    *	函 数 名: IIC_Stop
    *	功能说明: CPU发起IIC总线停止信号
    *	形    参：无
    *	返 回 值: 无
    *********************************************************************************************************
    */
    void IIC_Stop(IIC_TypeDef* IIC)
    {
        /* 当SCL高电平时，SDA出现一个上跳沿表示IIC总线停止信号 */
        IIC_SDA_0(IIC);
        IIC_SCL_1(IIC);
        IIC_Delay();
        IIC_SDA_1(IIC);
    }

    /*
    *********************************************************************************************************
    *	函 数 名: IIC_SendByte
    *	功能说明: CPU向IIC总线设备发送8bit数据
    *	形    参：_ucByte ： 等待发送的字节
    *	返 回 值: 无
    *********************************************************************************************************
    */
    void IIC_Send_Byte(IIC_TypeDef* IIC,uint8_t _ucByte)
    {
        uint8_t i;

        /* 先发送字节的高位bit7 */
        for (i = 0; i < 8; i++)
        {
            if (_ucByte & 0x80)
            {
                IIC_SDA_1(IIC);
            }
            else
            {
                IIC_SDA_0(IIC);
            }
            IIC_Delay();
            IIC_SCL_1(IIC);
            IIC_Delay();
            IIC_SCL_0(IIC);
            if (i == 7)
            {
                IIC_SDA_1(IIC); // 释放总线
            }
            _ucByte <<= 1;	/* 左移一个bit */
            IIC_Delay();
        }
    }

    /*
    *********************************************************************************************************
    *	函 数 名: IIC_ReadByte
    *	功能说明: CPU从IIC总线设备读取8bit数据
    *	形    参：无
    *	返 回 值: 读到的数据
    *********************************************************************************************************
    */
    uint8_t IIC_Read_Byte(IIC_TypeDef* IIC,uint8_t ack)
    {
        uint8_t i;
        uint8_t value;

        /* 读到第1个bit为数据的bit7 */
        value = 0;
        for (i = 0; i < 8; i++)
        {
            value <<= 1;
            IIC_SCL_1(IIC);
            IIC_Delay();
            if (IIC_SDA_READ(IIC))
            {
                value++;
            }
            IIC_SCL_0(IIC);
            IIC_Delay();
        }
        if(ack==0)
            IIC_NAck(IIC);
        else
            IIC_Ack(IIC);
        return value;
    }

    /*
    *********************************************************************************************************
    *	函 数 名: IIC_WaitAck
    *	功能说明: CPU产生一个时钟，并读取器件的ACK应答信号
    *	形    参：无
    *	返 回 值: 返回0表示正确应答，1表示无器件响应
    *********************************************************************************************************
    */
    uint8_t IIC_Wait_Ack(IIC_TypeDef* IIC)
    {
        uint8_t re;

        IIC_SDA_1(IIC);	/* CPU释放SDA总线 */
        IIC_Delay();
        IIC_SCL_1(IIC);	/* CPU驱动SCL = 1, 此时器件会返回ACK应答 */
        IIC_Delay();
        if (IIC_SDA_READ(IIC))	/* CPU读取SDA口线状态 */
        {
            re = 1;
        }
        else
        {
            re = 0;
        }
        IIC_SCL_0(IIC);
        IIC_Delay();
        return re;
    }

    /*
    *********************************************************************************************************
    *	函 数 名: IIC_Ack
    *	功能说明: CPU产生一个ACK信号
    *	形    参：无
    *	返 回 值: 无
    *********************************************************************************************************
    */
    void IIC_Ack(IIC_TypeDef* IIC)
    {
        IIC_SDA_0(IIC);	/* CPU驱动SDA = 0 */
        IIC_Delay();
        IIC_SCL_1(IIC);	/* CPU产生1个时钟 */
        IIC_Delay();
        IIC_SCL_0(IIC);
        IIC_Delay();
        IIC_SDA_1(IIC);	/* CPU释放SDA总线 */
    }

    /*
    *********************************************************************************************************
    *	函 数 名: IIC_NAck
    *	功能说明: CPU产生1个NACK信号
    *	形    参：无
    *	返 回 值: 无
    *********************************************************************************************************
    */
    void IIC_NAck(IIC_TypeDef* IIC)
    {
        IIC_SDA_1(IIC);	/* CPU驱动SDA = 1 */
        IIC_Delay();
        IIC_SCL_1(IIC);	/* CPU产生1个时钟 */
        IIC_Delay();
        IIC_SCL_0(IIC);
        IIC_Delay();
    }

    /*
    *********************************************************************************************************
    *	函 数 名: IIC_GPIO_Config
    *	功能说明: 配置IIC总线的GPIO，采用模拟IO的方式实现
    *	形    参：无
    *	返 回 值: 无
    *********************************************************************************************************
    */
    void IIC_GPIO_Init(IIC_TypeDef* IIC)
    {
            GPIO_InitTypeDef GPIO_InitStructure;
            
            //IIC->RCC_Enable();  // 打开GPIO时钟
            __HAL_RCC_GPIOB_CLK_ENABLE();
            GPIO_InitStructure.Pin = IIC->SCL_Pin | IIC->SDA_Pin;
            GPIO_InitStructure.Speed = GPIO_SPEED_FREQ_HIGH;
            GPIO_InitStructure.Mode = GPIO_MODE_OUTPUT_OD;  // 开漏输出
            HAL_GPIO_Init(IIC->GPIO_Port, &GPIO_InitStructure);
            
            /* 给一个停止信号, 复位IIC总线上的所有设备到待机模式 */
            IIC_Stop(IIC);

    }

    /*
    *********************************************************************************************************
    *	函 数 名: IIC_CheckDevice
    *	功能说明: 检测IIC总线设备，CPU向发送设备地址，然后读取设备应答来判断该设备是否存在
    *	形    参：_Address：设备的IIC总线地址
    *	返 回 值: 返回值 0 表示正确， 返回1表示未探测到
    *********************************************************************************************************
    */
    uint8_t IIC_CheckDevice(IIC_TypeDef* IIC,uint8_t _Address)
    {
        uint8_t ucAck;

        IIC_GPIO_Init(IIC);		/* 配置GPIO */

        IIC_Start(IIC);		/* 发送启动信号 */

        /* 发送设备地址+读写控制bit（0 = w， 1 = r) bit7 先传 */
        IIC_Send_Byte(IIC,_Address|IIC_WR);
        ucAck = IIC_Wait_Ack(IIC);	/* 检测设备的ACK应答 */

        IIC_Stop(IIC);			/* 发送停止信号 */

        return ucAck;
    }