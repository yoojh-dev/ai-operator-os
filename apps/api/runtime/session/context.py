class RequestContext:

    def __init__(self, session, messages=None):

        self.session = session
        self.messages = messages or []

    def add_message(self, message):

        self.messages.append(message)