FROM node:20-alpine

ARG USER_UID
ARG USER_GID

RUN addgroup -g $USER_GID usergroup && \
    adduser -D -u $USER_UID -G usergroup user && \
    chown -R $USER_UID:$USER_GID /app

WORKDIR /app

RUN npm install -g npm@10.8.0
RUN npm install -g create-react-app@5.0.1

USER ${USER_UID}:${USER_GID}
CMD ["npx", "create-react-app", "my_react_app"]



# docker build --build-arg USER_UID=$(id -u) --build-arg USER_GID=$(id -g) -t react_builder .
# docker run -it --rm -v "$PWD":/app:rw react_builder