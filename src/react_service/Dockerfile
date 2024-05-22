FROM node:20-alpine

ARG DOCKER_USER

ARG DOCKER_USER=default_user
RUN addgroup -S $DOCKER_USER && adduser -S $DOCKER_USER -G $DOCKER_USER
USER $DOCKER_USER

WORKDIR /app

RUN npm install -g npm@10.8.0
RUN npm install -g create-react-app@5.0.1

CMD ["npx", "create-react-app", "my_react_app"]



# docker build --build-arg USER_UID=$(id -u) --build-arg USER_GID=$(id -g) -t react_builder .
# docker run -it --rm -v "$PWD":/app:rw react_builder