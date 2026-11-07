import os
import time
from datetime import date
from RFID_RC522 import rfid
from Face_mask_detection import detect_mask_video
from MLX90614 import temp
from MAX30100 import spo2
import indicator
import upload_firebase_rpi

def workflow():
    print('Enter RFID Card: ')
    ID = rfid.read_rfid()
    if ID[0] is not None:
        masked = detect_mask_video.main()
        if masked == 1:
            while True:
                time.sleep(3)
                print('Place your finger for temperature: ')
                t = temp.read_temp()
                if t >= 95 and t < 108:
                    break
                else:
                    print("Try again")
                    indicator.led_try()
                    
            while True:
                print('Place your finger for oxygen saturation: ')
                ox_sat = spo2.read_spo2()
                if ox_sat >= 90 and ox_sat <= 100:
                    break
                else:
                    print("Try again")
                    indicator.led_try()

            # show risk factors
            if t <= 99 and ox_sat > 95:
              risk = 'No Risk'
            elif t > 99 and t < 100.4 and ox_sat > 95 or t < 99 and ox_sat < 95 or t > 100.4 and ox_sat > 95:
              risk = 'Moderate Risk'
            else:
              risk = 'High Risk'
              
            print("Entry Risk: ",risk)
            
            indicator.led(risk)
            
            # upload the data to firebase
            # getting date
            today = date.today()
            current_date = today.strftime("%b-%d-%Y")

            # getting time
            now = time.localtime()
            current_time = time.strftime("%H:%M:%S", now)

            user_data = {'ID': ID[0], 'Name': ID[1], 'Mask': 'Yes',
                         'Oxygen Sat': f'{ox_sat}%', 'Temperature': f'{t}F', 'Risk': risk,
                         'Date': current_date, 'Time': current_time}
            
            # push data to firebase
            upload_firebase_rpi.main(user_data)
             
            time.sleep(1)
            workflow()

        else:
            workflow()

    else:
        workflow()

def main():
    workflow()

if __name__ == '__main__':
    main()
