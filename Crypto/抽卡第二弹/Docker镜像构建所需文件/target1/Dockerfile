FROM python:3.7

#===========================
# 拷贝同目录下的文件到容器中、requirements.txt、pip国内源配置文件
#===========================
COPY /files /
COPY /files/pip.conf /etc/pip.conf

#===========================
# 安装所需python库
#===========================
RUN pip install --default-timeout=10000 -r requirements.txt

#===========================
# 开放端口号，默认为9999
#===========================
EXPOSE 9999


#===========================
# 启动服务器脚本
#===========================
CMD python /draw_system.py
