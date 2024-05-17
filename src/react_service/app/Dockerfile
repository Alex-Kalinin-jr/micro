#DEVELOPMENT STAGE
FROM node:20
RUN mkdir /app
WORKDIR /app
COPY package*.json ./

RUN npm install
RUN npm install react-router-dom

EXPOSE 3000
CMD ["npm", "start"]


# docker run --rm -it -p 3000:3000 -v $PWD:/app my-react-app-dev
