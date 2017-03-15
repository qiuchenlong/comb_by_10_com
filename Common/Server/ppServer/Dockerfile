# 基础镜像
FROM daocloud.io/python:3.5

# 维护者信息
MAINTAINER qiuchenlong <www.10.com>

RUN mkdir -p /app
WORKDIR /app

ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . /app
#COPY docker-entrypoint.sh docker-entrypoint.sh
#RUN chmod +x docker-entrypoint.sh

EXPOSE 8000

CMD manage.py runserver 0.0.0.0:8000
