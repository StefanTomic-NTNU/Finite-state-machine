import GPIOSimulator_v5 as GPIOSimulator_v5
from pynput.keyboard import Listener, Key
import time

    
def on_release(key):
    return False

class Keypad:
    
    def __init__(self):
        self.GPIO = GPIOSimulator_v5.GPIOSimulator
        self.key = ""
    
    def set_key(self, key):
        self.key = key.char

    def setup(self):
        self.GPIO.setup(GPIO.PIN_KEYPAD_ROW_0, GPIO.OUT)
        self.GPIO.setup(GPIO.PIN_KEYPAD_ROW_1, GPIO.OUT)
        self.GPIO.setup(GPIO.PIN_KEYPAD_ROW_2, GPIO.OUT)
        self.GPIO.setup(GPIO.PIN_KEYPAD_ROW_3, GPIO.OUT)
        
        self.GPIO.setup(GPIO.PIN_KEYPAD_COL_0, GPIO.IN)
        self.GPIO.setup(GPIO.PIN_KEYPAD_COL_1, GPIO.IN)
        self.GPIO.setup(GPIO.PIN_KEYPAD_COL_2, GPIO.IN)
    
    def do_polling(self):
        condition = False
        while(not condition):
            with Listener(on_press=self.set_key, on_release=on_release) as listener:
                listener.join()
            print(self.key)
            if self.key == "q":
                condition = True

    def get_next_signal(self):
        pass

def main():
    keypad = Keypad()
    keypad.do_polling()

if __name__ == "__main__": 
    main()