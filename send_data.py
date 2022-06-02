import datetime
import requests
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import psutil
import sys
#import buzzer
import time
import drivers
from time import sleep
import datetime
import bs4


signalPIN = 5
display = drivers.Lcd()
reader = SimpleMFRC522()

while True:
        
        try:
                
                id, text = reader.read()
                print(id)
                RFID = id

        finally:
                GPIO.cleanup()
                
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(signalPIN,GPIO.OUT)
        GPIO.output(signalPIN,0)
        GPIO.output(signalPIN,1)
        time.sleep(0.1)
        GPIO.output(signalPIN,0)
        
        display.lcd_display_string("Registreret", 1)
        sleep(2)
        
        display.lcd_clear()
        
        # Her laves vores dictionary variabl
        data_to_send = {}

        # Her Indsættes data i dictionary 
        data_to_send["date"] = str(datetime.datetime.now())
        data_to_send["ID"] = str(RFID)
        # Denne her bruger vi til at teste om pi kan fange RFID/date
        data_to_send["hukommelse"] = psutil.virtual_memory().percent

        print(data_to_send)

        r = requests.post("https://hook.eu1.make.com/cnf9ks9x9p4gqqp4r4muiiwypifllo9v", json = data_to_send)

        print(r.status_code)
        
        

