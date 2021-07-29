FROM python:3.7.3-alpine
RUN apk update
RUN apk upgrade
RUN apk add --no-cache bash git openssh util-linux
RUN pip3.7 install wheel
RUN apk add build-base
RUN apk add python3-dev libxml2 libxml2-dev libxslt-dev py3-setuptools py-pip
RUN pip3.7 install --upgrade conan
RUN apk add --no-cache cmake
ARG USER_ID
ARG USER_GROUP
RUN addgroup -g ${USER_GROUP} dockergroup
RUN adduser --disabled-password --gecos '' -u ${USER_ID} -G dockergroup dockertool
USER dockertool