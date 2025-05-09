FROM python:3.13.3-slim
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
ENV AUTHOR="User"
EXPOSE 8000
CMD ["python", "web-app1"]
