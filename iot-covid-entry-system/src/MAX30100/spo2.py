# -*- coding: utf-8 -*-
import time
from MAX30100 import max30100
#import max30100

def read_spo2():
    mx30 = max30100.MAX30100()
    mx30.enable_spo2()

    t_end = time.time() + 15
    while time.time() < t_end:
        mx30.read_sensor()

        mx30.ir, mx30.red

        hb = int(mx30.ir / 100)
        spo2 = int(mx30.red / 100)
        
        # if mx30.ir != mx30.buffer_ir :
        #     print("Pulse:",hb);
        # if mx30.red != mx30.buffer_red:
        #     print("SPO2:",spo2);

        #time.sleep(1)

    if mx30.red != mx30.buffer_red:
        print("SPO2:",spo2);
    
    return spo2

def main():
        read_spo2()

if __name__ == '__main__':
        main()
    
