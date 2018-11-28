FROM debian:stretch-slim

MAINTAINER David Castellanos "davidcaste@gmail.com"

RUN apt-get update -qq \
    && apt-get install -yq build-essential python python-pip \
    && pip install flask connexion \
    && apt-get remove -yq build-essential \
    && apt-get autoremove -yq \
    && rm -rf /tmp/* /var/tmp/* /var/lib/apt/lists/* /usr/local/share/.cache

WORKDIR /app

ENTRYPOINT ["python"]
CMD ["server.py"]

COPY . /app
