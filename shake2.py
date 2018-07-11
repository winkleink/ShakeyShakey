import RPi.GPIO as GPIO
from time import sleep, time 
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(17,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

score = 0 
starttime = time()
duration = 30 
endtime = starttime + duration
print("Time is: " + str(starttime))
while time() < endtime:
    print("Time left: " +  str(endtime - time()))
    if GPIO.input(4):
        score =score +1
        sleep(0.005)
        print("Your score is: " + str(score))
        while not GPIO.input(17):
            sleep(0.005)
            
            
print("Your score is: " + str(score))
