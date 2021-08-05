FROM python:3.8-slim

LABEL maintainer = yi.hu@unitediot.com.cn

# add all the files into root directory
USER root
WORKDIR /
ADD . /
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
ENTRYPOINT [ "python3", "start.py" ]