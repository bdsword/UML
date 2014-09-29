

class Informer:
    def __init__(self):
        super(Informer, self).__init__()
        self.registered_receivers = {}

    def fire(self, event_name, **keywords):
        if event_name in self.registered_receivers:
            for callback in self.registered_receivers[event_name]:
                callback(keywords)

    def register(self, event_name, callback):
        if event_name in self.registered_receivers:
            self.registered_receivers[event_name].append(callback)

    def add_event(self, event_name):
        if event_name not in self.registered_receivers:
            self.registered_receivers[event_name] = []

    def remove_event(self, event_name):
        if event_name in self.registered_receivers:
            del self.registered_receivers[event_name]