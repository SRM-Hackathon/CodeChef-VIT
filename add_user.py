import RPi.GPIO as GPIO

import os

PIR_input = 29				#read PIR Output
LED = 32				#LED for signalling motion detected	
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)		#choose pin no. system
GPIO.setup(PIR_input, GPIO.IN)	
GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED, GPIO.LOW)

while True:
#when motion detected turn on LED
    if(GPIO.input(PIR_input)):
        GPIO.output(LED, GPIO.HIGH)

        os.system('fswebcam --no-banner src.jpg')
        print('made photo')
        os.system('scp src.jpg root@192.168.43.254:/CodeChef-VIT/images/src.jpg')

    else:
        GPIO.output(LED, GPIO.LOW)
        
