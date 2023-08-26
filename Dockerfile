FROM --platform=linux/amd64  python:3-alpine3.17 as build
ADD server.py server.py
RUN pip install termcolor
RUN apk --update add net-tools busybox-extras mysql-client postgresql-client mongodb-tools
EXPOSE 3000
CMD ["python3", "server.py"]