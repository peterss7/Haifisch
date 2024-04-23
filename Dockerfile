FROM alpine:latest

WORKDIR /ngrok

# Download and install ngrok
RUN wget -q -O ngrok.zip https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip && \
    unzip ngrok.zip && \
    rm ngrok.zip

# Expose the ngrok command
ENV PATH="/ngrok:${PATH}"

CMD ["ngrok", "http", "5501"]
