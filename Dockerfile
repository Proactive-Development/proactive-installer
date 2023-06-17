FROM ubuntu:kinetic
COPY docker/entrypoint.bash /entrypoint.bash
COPY installer.py /home/installer.py
RUN apt-get update
RUN apt-get install -y git
RUN apt-get install -y python3
ENTRYPOINT bash entrypoint.bash