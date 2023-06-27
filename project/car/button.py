from gpiozero import Button, LED
import time
import signal

bt = Button(23)
idle = LED(24)
forward = LED(25)
backward = LED(26)

def handler(signum, frame):
    print("forward")
    raise Exception("timed out")

def for_back_handler():
    i=0
    print("round:",i)
    bt.wait_for_press()
    print("pressed")
    time.sleep(0.5)
    idle.on()
    signal.signal(signal.SIGALRM, handler)
    signal.alarm(10)
    try:
        i+=1
        print("round:",i)
        bt.wait_for_press()
        time.sleep(0.5)
        signal.alarm(0)
        idle.off()
        time.sleep(0.5)
        backward.on()
        time.sleep(0.5)
        print("forward")
    except Exception as e:
        idle.off()
        time.sleep(0.5)
        forward.on()
        time.sleep(0.5)
        print("backward")
        
    
for_back_handler()
print("finish")
time.sleep(10)
idle.off()
forward.off()
backward.off()