#! /usr/bin/python
# -*- coding:utf-8 -*-
import RPi.GPIO as GPIO
import time

def checkdist(trigPin, echoPin):
    #发出触发信号
    GPIO.output(trigPin,GPIO.HIGH)
    #保持10us以上
    time.sleep(0.000020)
    GPIO.output(trigPin,GPIO.LOW)
    while not GPIO.input(echoPin):
        pass
    #发现高电平时开时计时
    t1 = time.time()
    while GPIO.input(echoPin):
        pass
    #高电平结束停止计时
    t2 = time.time()
    #返回距离，单位为米
    return (t2-t1)*340/2

GPIO.setmode(GPIO.BCM)
trigPin = 6
echoPin = 12
GPIO.setup(trigPin, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(echoPin, GPIO.IN)

time.sleep(2)
try:
    while True:
        print 'Distance: %0.2f m' % checkdist(trigPin, echoPin)
        time.sleep(0.5)
except KeyboardInterrupt:
    GPIO.cleanup()