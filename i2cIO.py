import smbus
import time, datetime


class I2C:
    def __init__(self, channelAmount):
        self.channel = smbus.SMBus(channelAmount)


    def getTime(self):
        now = datetime.datetime.fromtimestamp(time.time())
        nowString = now.strftime('%Y/%m/%d %H:%M:%S')
        return nowString


    def getTempAndHumidity(self):
        # request
        self.channel.write_i2c_block_data(0x44, 0x2c, [0x06])
        time.sleep(0.05)
        # read data
        data = self.channel.read_i2c_block_data(0x44, 0x00, 6)
        now = self.getTime()
        # Convert the data
        tempInC = ((((data[0] * 256.0) + data[1]) * 175) / 65535.0) - 45
        humidity = 100 * (data[3] * 256 + data[4]) / 65535.0
        return now, tempInC, humidity
