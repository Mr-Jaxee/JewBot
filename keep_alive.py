from flask import Flask
from flask import request
from flask import session
from flask import url_for
from threading import Thread

app = Flask('')

@app.route('/')
def main():
    return "Your bot is alive!"


def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    server = Thread(target=run)
    server.start()
