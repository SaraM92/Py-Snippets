import RPi.GPIO as GPIO                  
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)                    
TRIG = 17
ECHO = 27
in1=16
in2=12
in3=21
in4=20
GPIO.setup(TRIG,GPIO.OUT)                  
GPIO.setup(ECHO,GPIO.IN)                      
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
def stop():
   print "stop"
   GPIO.output(in1, 0)
   GPIO.output(in2, 0)
   GPIO.output(in3, 0)
   GPIO.output(in4, 0)
def forward():
   GPIO.output(in1, 1)
   GPIO.output(in2, 0)
   GPIO.output(in3, 1)
   GPIO.output(in4, 0)
   print ("Forward")
def back():
   GPIO.output(in1, 0)
   GPIO.output(in2, 1)
   GPIO.output(in3, 0)
   GPIO.output(in4, 1)
   print ("back")
def left():
   GPIO.output(in1, 0)
   GPIO.output(in2, 0)
   GPIO.output(in3, 1)
   GPIO.output(in4, 0)
   print ("left")
def right():
   GPIO.output(in1, 1)
   GPIO.output(in2, 0)
   GPIO.output(in3, 0)
   GPIO.output(in4, 0)
   print ("right")
stop()
count=0
while True:
  GPIO.output(trig, True)
  time.sleep(0.00001) # 10 microseconds
  GPIO.output(trig, False)
  while GPIO.input(echo) == 0:
    pass
  start = time.time()
  while GPIO.input(echo) == 1:
    pass
  end = time.time()
  distance = ((end - start) * 34300) / 2
  print("distance:", distance, "cm")
  time.sleep(1)
  flag=0
  if distance < 15:      
     count=count+1
     stop()
     time.sleep(1)
     back()
     time.sleep(1.5)
     if (count%3 ==1) & (flag==0):
       right()
       flag=1
     else:
       left()
       flag=0
     time.sleep(1.5)
     stop()
     time.sleep(1)
  else:
     forward()
     flag=0
