""" File contains the KPC class """
import GPIOSimulator_v5 as GPIOSimulator
from fsm import FSM
from src.charlieplexer import Charlieplexer
from src.keypad import Keypad
from src.led_board import LED_board


class KPC:
    """
    The Keypad controller coordinates the
    Keypad, the FSM and the GPIO-Simulator.
    I handles all the actions that the FSM
    requests (i/e password verification).
    """

    def __init__(self, pathname):
        self.fsm = FSM(self)
        self.GPIO = GPIOSimulator.GPIOSimulator()
        self.keypad = Keypad(self.GPIO)
        self.led_board = LED_board(self.GPIO)
        self.pathname = pathname
        self.override_signal = None
        # self.current_password = "1234"
        self.read_password_from_file()
        self.cumulative_password = ""
        self.old_cumulative_password = ""
        self.chosen_led = None
        self.chosen_time = ""

    def do_polling(self):
        """
        Calls for the Keypad to poll for input,
        and changes the signal of the FSM accordingly
        """
        while True:
            if self.override_signal is None:
                self.fsm.signal = self.keypad.get_next_signal()
            else:
                self.fsm.signal = self.override_signal
            self.fsm.check_all_rules()
            print(self.fsm.state)

    def reset_init_passcode_entry(self):
        self.cumulative_password = ""
        self.power_up_animation()

    def reset_passcode_entry(self):
        self.cumulative_password = ""

    def append_next_password_digit(self):
        self.cumulative_password += self.fsm.signal
        print(self.cumulative_password)

    def verify_password(self):
        if self.current_password == self.cumulative_password:
            self.override_signal = "Y"
            self.twinkle_leds()
        else:
            self.override_signal = "0"
            self.flash_leds()

    def reset_agent(self):
        self.cumulative_password = ""
        self.override_signal = None
        self.power_down_animation()

    def fully_activate_agent(self):
        self.override_signal = None

    def get_next_signal(self):
        pass

    def cache_cumulative_password(self):
        self.old_cumulative_password = self.cumulative_password
        self.cumulative_password = ""

    def write_password_to_file(self):
        """
        Writes cumulative_password to file
        """
        with open(self.pathname, 'w') as file:
            file.write(self.cumulative_password)

    def read_password_from_file(self):
        """
        Reads the password from file and
        sets current_password accordingly
        """
        with open(self.pathname) as file:
            self.current_password = file.read()

    # def verify_login(self):
    #     pass

    def validate_password_change(self):
        """
        Checks if the passwords that the user has input
        are the same. If they are, the input password
        is written to file.
        """
        if self.old_cumulative_password == self.cumulative_password:
            self.write_password_to_file()
            self.cumulative_password = ""
            self.old_cumulative_password = ""

    def light_one_led(self, led_nr, sec):
        self.led_board.light_led_for_time(led_nr, sec)

    def flash_leds(self):
        self.led_board.flash_all_leds_multiple_times(3)

    def twinkle_leds(self):
        self.led_board.twinkle_all_leds()

    def power_up_animation(self):
        self.led_board.twinkle_leds_from_centre()

    def power_down_animation(self):
        self.led_board.twinkle_leds_from_edges()

    def choose_led(self):
        self.chosen_led = self.fsm.signal

    def choose_time(self):
        pass

    def add_letter_to_time(self):
        self.chosen_time += str(self.fsm.signal)

    def activate_led(self):
        self.light_one_led(self.chosen_led, int(self.chosen_time))

    def reset_led(self):
        self.chosen_led = None

    def reset_time(self):
        self.chosen_time = None

    def exit_action(self):
        pass
