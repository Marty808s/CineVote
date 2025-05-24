ARG NODE_VERSION
FROM node:${NODE_VERSION}-alpine

WORKDIR /app/frontend

COPY ../../frontend/package*.json ./
RUN npm install

#PAK ZMĚNIT DLE POTŘEBY
RUN npm start

EXPOSE 3000