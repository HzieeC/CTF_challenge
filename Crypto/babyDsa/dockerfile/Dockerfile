FROM python:3



RUN sed -i s@/deb.debian.org/@/mirrors.aliyun.com/@g /etc/apt/sources.list && \
    sed -i s@/security.debian.org/@/mirrors.aliyun.com/@g /etc/apt/sources.list && \
    apt-get update -y && \
    apt-get install socat -y

RUN pip install pycryptodome -ihttps://pypi.tuna.tsinghua.edu.cn/simple
COPY dsa.py /dsa.py 
COPY flag.py /flag.py 

EXPOSE 10000

ENTRYPOINT socat TCP4-LISTEN:10000,tcpwrap=script,reuseaddr,fork EXEC:"python dsa.py"
