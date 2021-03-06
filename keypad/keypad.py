from GPIOSimulator_v5 import GPIOSimulator
from pynput.keyboard import Listener, Key
import time

    
def on_release(key):
    return False

class Keypad:
    
    def __init__(self):
        self.GPIO = GPIOSimulator()
        self.key = ''

        self.key_coord = {'1' (3, 7),
                            '2' (3, 8),
                            '3' (3, 9),
                            '4' (4, 7),
                            '5' (4, 8),
                            '6' (4, 9),
                            '7' (5, 7),
                            '8' (5, 8),
                            '9' (5, 9),
                            '' (6, 7),
                            '0' (6, 8),
                            '#' (6, 9)}
        
        self.PIN_KEYPAD_ROW_0 = 3
        self.PIN_KEYPAD_ROW_1 = 4
        self.PIN_KEYPAD_ROW_2 = 5
        self.PIN_KEYPAD_ROW_3 = 6

        self.PIN_KEYPAD_COL_0 = 7
        self.PIN_KEYPAD_COL_1 = 8
        self.PIN_KEYPAD_COL_2 = 9
    
    def set_key(self, key):
        self.key = key.char

    def setup(self):
        self.GPIO.setup(self.PIN_KEYPAD_ROW_0, self.GPIO.OUT)
        self.GPIO.setup(self.PIN_KEYPAD_ROW_1, self.GPIO.OUT)
        self.GPIO.setup(self.PIN_KEYPAD_ROW_2, self.GPIO.OUT)
        self.GPIO.setup(self.PIN_KEYPAD_ROW_3, self.GPIO.OUT)
        
        self.GPIO.setup(self.PIN_KEYPAD_COL_0, self.GPIO.IN, state=self.GPIO.LOW)
        self.GPIO.setup(self.PIN_KEYPAD_COL_1, self.GPIO.IN, state=self.GPIO.LOW)
        self.GPIO.setup(self.PIN_KEYPAD_COL_2, self.GPIO.IN, state=self.GPIO.LOW)
    

    def do_polling(self):
        condition = False
        while(not condition):
            with Listener(on_press=self.set_key, on_release=on_release) as listener:
                listener.join()
            if(ord(self.key) == 39): # if press ' then we get  because we don't have a numpad
                self.key = ''
            elif(ord(self.key) == 43): # if press + then we get # because we don't have a numpad
                self.key = '#'
            coordinates = self.key_coord[self.key]
            row = coordinates[0]
            column = coordinates[1]
            self.GPIO.output(row, self.GPIO.HIGH)
            print(self.GPIO.input(column) == self.GPIO.HIGH)



            print(self.key)
            return self.key
            
            
            # if self.key == q
            #     condition = True

    def get_next_signal(self):
        signal = self.do_polling()


def main():
    keypad = Keypad()
    keypad.setup()
    keypad.do_polling()


if __name__ == "__main__":
    main()