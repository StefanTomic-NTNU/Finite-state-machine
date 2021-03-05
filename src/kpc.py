from fsm import FSM
from src.keypad import Keypad
from src.led_board import LED_board


class KPC:

    def __init__(self, pathname):
        self.keypad = Keypad()
        self.fsm = FSM(self)
        self.led_board = LED_board()
        self.pathname = pathname
        self.override_signal = None

    def do_polling(self):
        while True:
            self.fsm.signal = self.keypad.do_polling()
            self.fsm.check_all_rules()
            print(self.fsm.signal)
            print(self.fsm.state)

    def reset_passcode_entry(self):
        pass

    def append_next_password_digit(self):
        pass

    def verify_password(self):
        pass

    def reset_agent(self):
        pass

    def fully_activate_agent(self):
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
