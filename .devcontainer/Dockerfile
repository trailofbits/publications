ARG VARIANT="18-bullseye"
FROM mcr.microsoft.com/devcontainers/javascript-node:${VARIANT}

# Example: install git, curl and build-essential
RUN apt-get update && \
    apt-get install -y --no-install-recommends git curl build-essential && \
    rm -rf /var/lib/apt/lists/*
