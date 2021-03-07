""" Contains Keypad class """
import GPIOSimulator_v5 as GPIOsim
from datetime import datetime, timedelta
import time


class Keypad:
    """
    The Keypad class acts as an interface between
    the GPIOsimulator and the KPC
    """
    def __init__(self, GPIO):
        self.GPIO = GPIO

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

        self.__setup()

    def __setup(self):
        """ Sets up all keypad-GPIO pins """
        self.GPIO.setup(GPIOsim.PIN_KEYPAD_ROW_0, self.GPIO.OUT)
        self.GPIO.setup(GPIOsim.PIN_KEYPAD_ROW_1, self.GPIO.OUT)
        self.GPIO.setup(GPIOsim.PIN_KEYPAD_ROW_2, self.GPIO.OUT)
        self.GPIO.setup(GPIOsim.PIN_KEYPAD_ROW_3, self.GPIO.OUT)
        
        self.GPIO.setup(GPIOsim.PIN_KEYPAD_COL_0, self.GPIO.IN, state=self.GPIO.LOW)
        self.GPIO.setup(GPIOsim.PIN_KEYPAD_COL_1, self.GPIO.IN, state=self.GPIO.LOW)
        self.GPIO.setup(GPIOsim.PIN_KEYPAD_COL_2, self.GPIO.IN, state=self.GPIO.LOW)

    def do_polling(self):
        """
        Polls keypad for input.

        If 100ms has passed without input, a token
        "N" is passed instead. This is so that the
        get_next_signal method can determine when
        the user has finished pressing a button.
        """
        # pressed_key = None
        end_time = datetime.now() + timedelta(seconds=0.1)
        while datetime.now() < end_time:
            time.sleep(0.01)
            for row in GPIOsim.keypad_row_pins:
                self.set_all_rows_to_low()
                self.GPIO.output(row, self.GPIO.HIGH)
                for col in GPIOsim.keypad_col_pins:
                    if self.GPIO.input(col) == self.GPIO.HIGH:
                        return self.inv_key_coord[str((row, col))]
        return "N"

    def set_all_rows_to_low(self):
        """ Sets all row-pins to LOW """
        self.GPIO.output(GPIOsim.PIN_KEYPAD_ROW_0, self.GPIO.LOW)
        self.GPIO.output(GPIOsim.PIN_KEYPAD_ROW_1, self.GPIO.LOW)
        self.GPIO.output(GPIOsim.PIN_KEYPAD_ROW_2, self.GPIO.LOW)
        self.GPIO.output(GPIOsim.PIN_KEYPAD_ROW_3, self.GPIO.LOW)

    def get_next_signal(self):
        """
        Retrieves a signal that can be returned to KPC.

        The signal is retrieved from the keypad through
        polling. The signal is then processed such that
        repeated polling of a single symbol only results in
        a single symbol being returned. This needs to be
        the because if the user presses a button we only
        want a single signal from that button, without
        it being repeated for each polling.
        """
        input_stream = ""
        while len(input_stream) < 2 or input_stream[0] == input_stream[-1]:
            last_letter = self.do_polling()
            if last_letter != "N":
                input_stream += last_letter
            if last_letter == "N" and len(input_stream) > 0:
                break
        return input_stream[0]
