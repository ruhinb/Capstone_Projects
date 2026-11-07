from gpiozero import LED
from time import sleep

def led(risk):
    if risk == 'No Risk':
        green = LED(12)
        green.on()
        sleep(5)
        green.off()
    
    if risk == 'Moderate Risk':
        yellow = LED(16)
        yellow.on()
        sleep(5)
        yellow.off()
        
    if risk == 'High Risk':
        red = LED(20)
        red.on()
        sleep(5)
        red.off()

def led_try():
        blue = LED(21)
        blue.on()
        sleep(2)
        blue.off()

# def main(risk):
#     led(risk)

# if __name__ == '__main__':
#     main(risk)