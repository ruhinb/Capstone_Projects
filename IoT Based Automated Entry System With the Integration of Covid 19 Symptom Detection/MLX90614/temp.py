import board
import busio as io
import adafruit_mlx90614

from time import sleep

def read_temp():
    i2c = io.I2C(board.SCL, board.SDA, frequency=100000)
    mlx = adafruit_mlx90614.MLX90614(i2c)
    
    targetTemp = "{:.2f}".format(mlx.object_temperature)
    tempInt = float(targetTemp)
    finalTemp = ((tempInt)*(9/5))+32
    
    sleep(1)
    
    print("Target Temperature: {:.2f} °F".format(finalTemp))
    return finalTemp

def main():
    read_temp()
    
if __name__== '__main__':
    main()