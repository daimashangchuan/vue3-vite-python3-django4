#!/bin/bash

# 检查操作系统类型和处理器架构
if [[ "$OSTYPE" == "darwin"* ]]; then
    # Mac 环境
    COMMAND_SH_RUN="cd django/pvenv/bin/ && source activate && cd .. && cd .. && cd djangoproject && python3 manage.py runserver"
    COMMAND_SH_PIP="cd django/pvenv/bin/ && source activate && pip3 install $2"
elif [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" || "$OSTYPE" == "win32" ]]; then
    # Windows 环境
    COMMAND_SH_RUN='cd django/pvenv/bin/activate.bat && cd .. && cd .. && cd djangoproject && python3 manage.py runserver'
else
    echo "Unsupported operating system."
    exit 1
fi

# 检查命令行参数
if [ "$1" = "pip" ]; then
    # 虚拟环境下载依赖
    echo "++++++++++++++++++++++++++++++++"
    eval $COMMAND_SH_PIP
else
    # 启动服务器
    echo "==============================="
    eval $COMMAND_SH_RUN
fi