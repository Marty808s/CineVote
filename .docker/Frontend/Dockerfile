ARG NODE_VERSION
ARG REACT_PORT
FROM node:${NODE_VERSION}-alpine

WORKDIR /app/frontend

COPY ../../frontend/package*.json ./
RUN npm install

EXPOSE ${REACT_PORT}