import os
from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    # host_name = os.uname()[1]  # Get the host name
    # ip_address = os.popen('hostname -I').read().strip()  # Get the IP address
    # author = os.getenv('AUTHOR', 'Unknown')  # Get the author from environment variable
    return f"Welcome to the Simple Web Application!\nHost Name: {host_name}\nIP Address: {ip_address}\nAuthor: {author}"

if __name__ == "__main__":
    app.run(debug=True)