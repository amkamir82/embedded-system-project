import Adafruit_DHT as dht
from gpiozero import LED
from time import sleep

def temp_and_hum():
    led = LED(27)
    
    
    while True:
        humidity, temperature = dht.read_retry(dht.DHT22, 4)
        print(f"Temp={temperature} and Humidity={humidity}")
        if humidity > 40:
            print("========")
            led.on()
            sleep(0.5)
        else:
            led.off()
            sleep(0.5)

temp_and_hum()
