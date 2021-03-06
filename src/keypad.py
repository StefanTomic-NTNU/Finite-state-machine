import GPIOSimulator_v5 as GPIOSimulator
from pynput.keyboard import Listener, Key
import time

    
def on_release(key):
    return False


class Keypad:
    
    def __init__(self, GPIO):
        self.GPIO = GPIO
        self.key = ""
    
    def set_key(self, key):
        self.key = key.char

    def setup(self):
        self.GPIO.setup(self.GPIO.PIN_KEYPAD_ROW_0, self.GPIO.OUT)
        self.GPIO.setup(self.GPIO.PIN_KEYPAD_ROW_1, self.GPIO.OUT)
        self.GPIO.setup(self.GPIO.PIN_KEYPAD_ROW_2, self.GPIO.OUT)
        self.GPIO.setup(self.GPIO.PIN_KEYPAD_ROW_3, self.GPIO.OUT)
        
        self.GPIO.setup(self.GPIO.PIN_KEYPAD_COL_0, self.GPIO.IN, state=self.GPIO.LOW)
        self.GPIO.setup(self.GPIO.PIN_KEYPAD_COL_1, self.GPIO.IN, state=self.GPIO.LOW)
        self.GPIO.setup(self.GPIO.PIN_KEYPAD_COL_2, self.GPIO.IN, state=self.GPIO.LOW)
    
    def do_polling(self):
        condition = False
        while(not condition):
            with Listener(on_press=self.set_key, on_release=on_release) as listener:
                listener.join()
            return self.key
            # if self.key == "q":
            #     condition = True

    def get_next_signal(self):
        pass


def main():
    keypad = Keypad()
    keypad.do_polling()


if __name__ == "__main__": 
    main()