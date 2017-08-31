import requests

HOST = 'http://127.0.0.1'
PORT = '5000'


class WebUI():
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.address = host + ':' + port

    def init(self, game_id, data):
        try:
            requests.post(self.address + '/create/' + str(game_id), json=data)
        except Exception as e:
            self.handle_server_exception(e)

    def update(self, game_id, data):
        try:
            requests.post(self.address + '/update/' + str(game_id), json=data)
        except Exception as e:
            self.handle_server_exception(e)

    def finish(self, game_id, status):
        try:
            requests.post(self.address + '/finish/' + str(game_id), json={'status': status})
        except Exception as e:
            self.handle_server_exception(e)

    def handle_server_exception(e):
        # Log the exception
        print(e)


webUI = WebUI(HOST, PORT)
