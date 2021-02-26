from keypad.keypad import Keypad
from keypad.led_board import LED_board


class KPC:

    def __init__(self, pathname, override_signal):
        self.keypad = Keypad()
        self.led_board = LED_board()
        self.pathname = pathname
        self.override_signal = override_signal

    def reset_passcode_entry(self):
        pass

    def get_next_signal(self):
        pass

    def verify_login(self):
        pass

    def validate_passcode_change(self):
        pass

    def light_one_led(self):
        pass

    def flash_leds(self):
        self.led_board.flash_all_leds()

    def twinkle_leds(self):
        self.led_board.twinkle_all_leds()

    def exit_action(self):
        pass