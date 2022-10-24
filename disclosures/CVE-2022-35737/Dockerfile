FROM ubuntu:20.04

# Configure timezone so that tzdata dependency does not require user input to
# configure.
ENV TZ=America/New_York
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Pin to SQLite install to vulnerable version.
RUN apt-get update && \
    apt-get install -y \
        build-essential \
        libsqlite3-dev=3.31.1-4ubuntu0.3 \
        php-cli \
        php-pdo-sqlite

COPY ./ /poc
WORKDIR /poc

RUN make
