import urllib
import urllib2
import json

ALARM_NONE        = 0
ALARM_FOOD        = 1
ALARM_FIRE        = 2
CHANGE_NAME       = 'na'
CHANGE_TEMP       = 'ta'
CHANGE_ALARM_HIGH = 'th'
CHANGE_ALARM_LOW  = 'tl'
CHANGE_BLOWER     = 'sw'


class Sensor:

    def __init__(self, data, ip):

        self.ip = ip
        self.id = data["id"]
        self.name = data["name"]
        self.alarm = data["al"]
        self.targetTemp = data["ta"]
        self.highTemp = data["th"]
        self.lowTemp = data["tl"]
        self.currentTemp = data["tc"]
        self.blower = data["blower"]

    def set_target_temp(self, temp):

        url = "http://{0}/stoker.Post_Handler".format(self.ip)
        action = '%s%s' % (CHANGE_TEMP, self.id)
        data = urllib.urlencode([(action, temp)])
        urllib.urlopen(url, data=data)
        self.targetTemp = temp

    def set_high_temp(self, temp):

        url = "http://{0}/stoker.Post_Handler".format(self.ip)
        action = '%s%s' % (CHANGE_ALARM_HIGH, self.id)
        data = urllib.urlencode([(action, temp)])
        urllib.urlopen(url, data=data)
        self.highTemp = temp

    def set_low_temp(self, temp):

        url = "http://{0}/stoker.Post_Handler".format(self.ip)
        action = '%s%s' % (CHANGE_ALARM_LOW, self.id)
        data = urllib.urlencode([(action, temp)])
        urllib.urlopen(url, data=data)
        self.lowTemp = temp

    def assign_blower(self, blower):

        url = "http://{0}/stoker.Post_Handler".format(self.ip)
        action = '%s%s' % (CHANGE_BLOWER, self.id)
        data = urllib.urlencode([(action, blower.id)])
        urllib.urlopen(url, data=data)
        self.blower = blower

    def unassign_blower(self):

        url = "http://{0}/stoker.Post_Handler".format(self.ip)
        action = '%s%s' % (CHANGE_BLOWER, self.id)
        data = urllib.urlencode([(action, "null")])
        urllib.urlopen(url, data=data)
        self.blower = None

    def set_name(self, name):

        url = "http://{0}/stoker.Post_Handler".format(self.ip)
        action = '%s%s' % (CHANGE_NAME, self.id)
        data = urllib.urlencode([(action, name)])
        urllib.urlopen(url, data=data)
        self.name = name

    def get_current_temp(self):

        url = "http://{0}/stoker.json".format(self.ip)
        response = urllib2.urlopen(url).read()
        data = json.loads(response)

        for sensor in data["stoker"]["sensors"]:
            if sensor["name"] == self.name:
                self.currentTemp = sensor["tc"]
                
        return self.currentTemp
