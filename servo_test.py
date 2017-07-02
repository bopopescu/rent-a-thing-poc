import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
p = GPIO.PWM(18, 50)
p.start(7.5)

try:
    while True:
#        p.ChangeDutyCycle(7.5) #90 deg
#        time.sleep(1)
        p.ChangeDutyCycle(2.5) #0 deg
        time.sleep(1)
#        p.ChangeDutyCycle(7.5)
#        time.sleep(1)
        p.ChangeDutyCycle(12.5) #180 deg
        time.sleep(1)

except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()

#duty = float(90) / 10.0 + 2.5
