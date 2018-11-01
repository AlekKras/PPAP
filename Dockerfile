FROM ubuntu 
LABEL Aleksandr Krasnov "alekforwork@gmail.com"

USER root

RUN apt-get update && apt-get install -y git && \
    apt-get install python python3 -y && \
    apt install python3-pip -y && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
    git clone https://github.com/AlekKras/PPAP.git && cd PPAP && python install_docker.py
