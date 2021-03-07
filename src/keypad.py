import GPIOSimulator_v5 as GPIOsim
from datetime import datetime, timedelta
import time


#TODO implement CTRL + C somewhere and clear all the leds etc.... 

#def on_release(key):
#    return False


class Keypad:
    def __init__(self, GPIO):
        self.GPIO = GPIO
        self.key = ''

        self.inv_key_coord = {
            '(3, 7)': '1',
            '(3, 8)': '2',
            '(3, 9)': '3',
            '(4, 7)': '4',
            '(4, 8)': '5',
            '(4, 9)': '6',
            '(5, 7)': '7',
            '(5, 8)': '8',
            '(5, 9)': '9',
            '(6, 7)': '*',
            '(6, 8)': '0',
            '(6, 9)': '#'
        }

        self.setup()
    
    def set_key(self, key):
        self.key = key.char

    def setup(self):
        self.GPIO.setup(GPIOsim.PIN_KEYPAD_ROW_0, self.GPIO.OUT)
        self.GPIO.setup(GPIOsim.PIN_KEYPAD_ROW_1, self.GPIO.OUT)
        self.GPIO.setup(GPIOsim.PIN_KEYPAD_ROW_2, self.GPIO.OUT)
        self.GPIO.setup(GPIOsim.PIN_KEYPAD_ROW_3, self.GPIO.OUT)
        
        self.GPIO.setup(GPIOsim.PIN_KEYPAD_COL_0, self.GPIO.IN, state=self.GPIO.LOW)
        self.GPIO.setup(GPIOsim.PIN_KEYPAD_COL_1, self.GPIO.IN, state=self.GPIO.LOW)
        self.GPIO.setup(GPIOsim.PIN_KEYPAD_COL_2, self.GPIO.IN, state=self.GPIO.LOW)

    def do_polling(self):
        # pressed_key = None
        end_time = datetime.now() + timedelta(seconds=0.1)
        while datetime.now() < end_time:
            time.sleep(0.01)
            for row in GPIOsim.keypad_row_pins:
                self.set_all_rows_to_low()
                self.GPIO.output(row, self.GPIO.HIGH)
                for col in GPIOsim.keypad_col_pins:
                    if self.GPIO.input(col) == self.GPIO.HIGH:
                        self.key = self.inv_key_coord[str((row, col))]
                        if(ord(self.key) == 39): # if press ' then we get * because we don't have a numpad
                            self.key = ''
                        elif(ord(self.key) == 43): # if press + then we get # because we don't have a numpad
                            self.key = '#'
                        return self.key
        return "N"

    def set_all_rows_to_low(self):
        self.GPIO.output(GPIOsim.PIN_KEYPAD_ROW_0, self.GPIO.LOW)
        self.GPIO.output(GPIOsim.PIN_KEYPAD_ROW_1, self.GPIO.LOW)
        self.GPIO.output(GPIOsim.PIN_KEYPAD_ROW_2, self.GPIO.LOW)
        self.GPIO.output(GPIOsim.PIN_KEYPAD_ROW_3, self.GPIO.LOW)

    def get_next_signal(self):
        input_stream = ""
        while len(input_stream) < 2 or input_stream[0] == input_stream [-1]:
            last_letter = self.do_polling()
            if last_letter != "N":
                input_stream += last_letter
            if last_letter == "N" and len(input_stream) > 0:
                break
        return input_stream[0]
