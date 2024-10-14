FROM node:20.17.0-alpine

WORKDIR /app

COPY frontend/package.json ./ 
COPY frontend/package-lock.json ./

RUN npm install

COPY frontend/ ./

RUN npm run build

FROM nginx:alpine

COPY --from=0 /app/build /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]