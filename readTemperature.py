import RPi.GPIO as GPIO
import i2cIO
import time


GPIO.setmode(GPIO.BOARD)

i2c = i2cIO.I2C(channelAmount=1)


try:
    while True:
        now, temp, _ = i2c.getTempAndHumidity()
        print(f'{now}:: {temp}C')

        time.sleep(60)


except KeyboardInterrupt:
    GPIO.cleanup()
