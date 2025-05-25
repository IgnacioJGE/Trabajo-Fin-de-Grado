FROM node:18
COPY . .
RUN npm install
EXPOSE 3000
CMD ["npx" , "next" , "start" , "-H" , "0.0.0.0" , "-p" , "3000"]