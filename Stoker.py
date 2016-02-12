import urllib2
import json
import Sensor
import Blower


class Stoker:

    def __init__(self, stoker):
        self.stoker_address = stoker
        self.sensors = []
        self.blowers = []
        self.data = {}

    def setup(self):
        self.set_stoker_data()
        self.set_sensors()
        self.set_blowers()

    def set_stoker_data(self):

        url = "http://{0}/stoker.json".format(self.stoker_address)
        response = urllib2.urlopen(url).read()
        self.data = json.loads(response)

    def set_sensors(self):

        if self.data:
            for sensor in self.data["stoker"]["sensors"]:
                self.sensors.append(Sensor.Sensor(sensor, self.stoker_address))

    def set_blowers(self):

        if self.data:
            for blower in self.data["stoker"]["blowers"]:
                self.blowers.append(Blower.Blower(blower, self.stoker_address))