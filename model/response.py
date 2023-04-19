
# classe para tratar as respostas
class Response:
    def __init__(self, ok=True, menssage='', data=[]):
        self.ok = ok
        self.message = menssage
        self.data = data

        