FROM ubuntu 
LABEL Aleksandr Krasnov "alekforwork@gmail.com"

USER root

RUN apt-get update -y  && apt-get install -y git && \
    apt-get install python python3 -y && \
    apt install python3-pip -y && \
   #: apt clean && apt autoremove  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
    git clone https://github.com/AlekKras/PPAP.git
    
#RUN python PPAP/install_docker.py
