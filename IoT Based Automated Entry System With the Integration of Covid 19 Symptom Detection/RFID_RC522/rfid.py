import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

def read_rfid():
        reader = SimpleMFRC522()
        try:
                id, text = reader.read()
                print(id)
                print(text)
        finally:
                GPIO.cleanup()
        return id, text

def main():
        read_rfid()

if __name__ == '__main__':
        main()