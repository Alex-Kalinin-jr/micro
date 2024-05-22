FROM node:20
RUN mkdir /app
WORKDIR /app/

COPY package.json .
COPY package-lock.json .
RUN npm install --legacy-peer-deps

COPY . /app

EXPOSE 3000
CMD ["npm", "start"]

# docker build -t react_app .
# docker run --rm -it -p 3000:3000 -v $PWD:/app react_app
