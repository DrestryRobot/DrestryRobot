TCP通信
=========
.. contents:: 目录

TCP通信
---------
TCP通信，是一种通过网线端口在不同设备之间进行的通信。

TCP通信代码实现
---------------
TCP接收函数
~~~~~~~~~~~~~~~~~~
.. code:: c++

    /* TCP接收函数 */
    void runServer()
    {
        const char* server_ip = "127.0.0.1";
        int server_port = 7930;
        WSADATA wsaData;
        SOCKET sockfd;
        struct sockaddr_in server_addr;
        char buffer[1024];
        wchar_t wserver_ip[16];

        // 将多字节字符串转换为宽字符字符串
        size_t convertedChars = 0;
        mbstowcs_s(&convertedChars, wserver_ip, server_ip, strlen(server_ip) + 1);

        // 初始化Winsock
        if (WSAStartup(MAKEWORD(2, 2), &wsaData) != 0) {
            std::cerr << "WSAStartup failed\n";
            return;
        }

        // 创建socket
        if ((sockfd = socket(AF_INET, SOCK_STREAM, 0)) == INVALID_SOCKET) {
            std::cerr << "Socket creation error\n";
            WSACleanup();
            return;
        }

        // 设置服务器地址
        server_addr.sin_family = AF_INET;
        server_addr.sin_port = htons(server_port);

        // 使用InetPton替代inet_addr
        if (InetPton(AF_INET, wserver_ip, &server_addr.sin_addr) <= 0) {
            std::cerr << "Invalid address / Address not supported\n";
            closesocket(sockfd);
            WSACleanup();
            return;
        }

        // 连接服务器
        if (connect(sockfd, (struct sockaddr*)&server_addr, sizeof(server_addr)) == SOCKET_ERROR) {
            std::cerr << "Connection failed\n";
            closesocket(sockfd);
            WSACleanup();
            return;
        }

        // 接收一次数据
        int valread = recv(sockfd, buffer, sizeof(buffer) - 1, 0);
        if (valread > 0) {
            buffer[valread] = '\0';

            try {
                angle1 = std::stod(buffer);
            }
            catch (const std::exception& e) {
                std::cerr << "Conversion error: " << e.what() << std::endl;
            }
        }
        else if (valread == 0) {
            std::cout << "Connection closed by server\n";
        }
        else {
            std::cerr << "Read error\n";
        }

        // 关闭socket
        closesocket(sockfd);
        WSACleanup();
    }

TCP发送函数
~~~~~~~~~~~~~~~~~~
.. code:: c++

    /* TCP发送函数 */
    void runClient() 
    {
        WSADATA wsaData;
        if (WSAStartup(MAKEWORD(2, 2), &wsaData) != 0) {
            std::cerr << "WSAStartup 失败: " << WSAGetLastError() << std::endl;
            return;
        }

        SOCKET clientSocket = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);
        if (clientSocket == INVALID_SOCKET) {
            std::cerr << "创建 socket 失败: " << WSAGetLastError() << std::endl;
            WSACleanup();
            return;
        }

        sockaddr_in serverAddr;
        serverAddr.sin_family = AF_INET;
        serverAddr.sin_port = htons(7930);

        // 使用 inet_pton 代替 inet_addr
        if (inet_pton(AF_INET, "127.0.0.1", &serverAddr.sin_addr) <= 0) {
            std::cerr << "Invalid address/ Address not supported" << std::endl;
            closesocket(clientSocket);
            WSACleanup();
            return;
        }

        if (connect(clientSocket, (sockaddr*)&serverAddr, sizeof(serverAddr)) == SOCKET_ERROR) {
            std::cerr << "连接失败: " << WSAGetLastError() << std::endl;
            closesocket(clientSocket);
            WSACleanup();
            return;
        }
        else {
            std::cout << "连接成功" << std::endl;
        }

        const char* message = "1";

        int sendResult = send(clientSocket, message, strlen(message), 0);
        if (sendResult == SOCKET_ERROR) {
            std::cerr << "发送数据失败: " << WSAGetLastError() << std::endl;
        }
        else {
            std::cout << "发送数据: " << message << std::endl;
        }

        closesocket(clientSocket);
        WSACleanup();
    }
