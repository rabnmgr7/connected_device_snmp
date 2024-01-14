FROM --platform=$BUILDPLATFORM ubuntu:latest as build1
WORKDIR /app/
COPY . /app/
RUN apt update -y \
    && apt install python3 python3-pip -y \
    && apt install libsnmp-dev -y \
    && pip3 install -r requirements.txt
 
ENTRYPOINT ["python3"]
CMD ["app.py"]
