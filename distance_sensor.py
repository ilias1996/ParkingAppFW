#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import requests


try:
      GPIO.setmode(GPIO.BOARD)
      PIN_TRIGGER = 7
      PIN_ECHO = 11
      GPIO.setup(PIN_TRIGGER, GPIO.OUT)
      GPIO.setup(PIN_ECHO, GPIO.IN)     
      GPIO.output(PIN_TRIGGER, GPIO.LOW)
      print (" Waiting for sensor to settle ")
      time.sleep(2)
      print ("Calculating distance")
      GPIO.output(PIN_TRIGGER, GPIO.HIGH)
      time.sleep(0.00001)
      GPIO.output(PIN_TRIGGER, GPIO.LOW)
      while GPIO.input(PIN_ECHO)==0:
            pulse_start_time = time.time()
      while GPIO.input(PIN_ECHO)==1:
            pulse_end_time = time.time()
      pulse_duration = pulse_end_time - pulse_start_time
      distance = round(pulse_duration * 17150, 2)
      print ("Distance:",distance,"cm")
      url = "http://dtsl.ehb.be/~ilias.benchikh/database%20final%20work/api/Device/update.php"
      if distance > 40:
         r = requests.post(url, data={'Id': 1, 'IsBezet': 0})
         print(r.status_code, r.reason)
         print(r.text[:300] + '...')
      else:
         r = requests.post(url, data={'Id': 1, 'IsBezet': 1})
         print(r.status_code, r.reason)
         print(r.text[:300] + '...')     
      

finally:
      GPIO.cleanup()