class Invalid_Api_token(Exception):
    def __init__(self):
        self.args = {"Invalid Api Token Passed Please Add the Correct token"}


class Invalid_Api_request(Exception):
    def __init__(self, error: str):
        self.args = {error}


class Server_Error(Exception):
    def __init__(self):
        self.args = {"There is the error with the developer"}


class Failed_Transcription_Jobs(Exception):
    def __init__(self, args):
        self.args = {args['error']}
