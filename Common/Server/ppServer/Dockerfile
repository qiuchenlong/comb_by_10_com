# 基础镜像
FROM daocloud.io/python:3.5

# 维护者信息
MAINTAINER qiuchenlong <www.10.com>

ADD blog.tar.gz /usr/src/ 

# app 所在目录
WORKDIR /usr/src/qiuchenlong

# 安装 app 所需依赖
RUN pip install --no-cache-dir -r requirements.txt -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
