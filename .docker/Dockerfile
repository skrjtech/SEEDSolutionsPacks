FROM skrjtech/ros:melodic

SHELL [ "/bin/bash", "-c" ]

COPY buildseed.sh /.buildseed.sh
# COPY .docker/buildseed.sh /.buildseed.sh
RUN  bash /.buildseed.sh

CMD [ "/bin/bash" ]