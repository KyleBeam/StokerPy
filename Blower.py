class Blower:

    def __init__(self, data, ip):

        self.data = data
        self.ip = ip
        self.id = data["id"]
        self.name = data["name"]
        self.on = data["on"]

    def set_name(self, name):

        self.name = name

    def turn_on(self):

        self.on = 1

    def turn_off(self):

        self.on = 0


