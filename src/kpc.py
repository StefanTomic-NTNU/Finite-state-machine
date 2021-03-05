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
        self.current_password = "1234"
        self.cumulative_password = ""
        self.old_cumulative_password = ""

    def do_polling(self):
        while True:
            # print(self.override_signal)
            if self.override_signal is None:
                self.fsm.signal = self.keypad.do_polling()
            else:
                self.fsm.signal = self.override_signal
            self.fsm.check_all_rules()
            print(self.fsm.state)

    def reset_passcode_entry(self):
        self.cumulative_password = ""

    def append_next_password_digit(self):
        self.cumulative_password += self.fsm.signal
        print(self.cumulative_password)

    def verify_password(self):
        if self.current_password == self.cumulative_password:
            self.override_signal = "Y"
        else:
            self.override_signal = "0"

    def reset_agent(self):
        self.cumulative_password = ""
        self.override_signal = None

    def fully_activate_agent(self):
        self.override_signal = None

    def get_next_signal(self):
        pass

    # def verify_login(self):
    #     pass

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
