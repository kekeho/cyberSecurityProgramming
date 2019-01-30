FROM kalilinux/kali-linux-docker

RUN apt update
RUN apt -y install python3
RUN echo 'alias python="python3"' >> ~/.bashrc

COPY ["./", "/home/cyber_security_programming/"]
WORKDIR /home/cyber_security_programming