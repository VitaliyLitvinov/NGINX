from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/')
def home():
    host_name = request.host
    host_ip = request.remote_addr
    author = os.getenv('AUTHOR', 'Неизвестный автор')
    return (f'<html><body><h1>Информация о сервере</h1>'
            f'<p>Имя хоста: {host_name}</p>'
            f'<p>IP адрес: {host_ip}</p>'
            f'<p>Автор: {author}</p></body></html>')

if __name__ == '__main__':
    app.run(port=8000,host='0.0.0.0',debug=True)