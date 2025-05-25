FROM python:3.9-slim
COPY . .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 5005
COPY start.sh start.sh
RUN chmod +x /start.sh
CMD ["/start.sh"]
