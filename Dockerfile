FROM lambci/lambda:build-python3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN echo 'export PS1="\[\e[36m\]eduzenshell>\[\e[m\] "' >> /root/.bashrc

COPY requirements.txt requirements_dev.txt ./
RUN yum update -y && \
    yum install -y \
        postgresql \
        curl

RUN pip install -U pip
RUN pip install -r requirements_dev.txt

WORKDIR /code
ENV PYTHONPATH /code:$PYTHONPATH

# USER uwsgi
EXPOSE 80
COPY . /code/

CMD ["uwsgi", "--ini", "/code/scripts/uwsgi.ini"]
