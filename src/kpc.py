""" File contains the KPC class """
import GPIOSimulator_v5 as GPIOSimulator
from fsm import FSM
from keypad import Keypad
from led_board import LED_board


class KPC:
    """
    The Keypad controller coordinates the
    Keypad, the FSM and the GPIO-Simulator.
    It is the main class of the project.

    It polls the Keypad for input. This input
    is stored in the FSM as a signal. Upon
    storing the signal, the FSM will check which
    of it's rules should fire, and change state
    accordingly. Once a rule is fired, it calls
    for the KPC to perform a method (action).

    Most of the methods in this class are actions
    that are to be called from the Rules that are
    fired.

    These actions often involve the manipulation of
    LEDs in the GPIOsimulator. This is done through
    the led_board, which in turn calls upon methods
    in the Charlieplexer to change the state of
    the GPIOsimulator.
    """

    def __init__(self, pathname):
        # Initializes main components of the program
        self.fsm = FSM(self)
        self.GPIO = GPIOSimulator.GPIOSimulator()
        self.keypad = Keypad(self.GPIO)
        self.led_board = LED_board(self.GPIO)

        # This password is only used if there is no file
        self.current_password = "1234"
        self.pathname = pathname
        self.read_password_from_file()
        self.cumulative_password = ""
        self.old_cumulative_password = ""
        self.override_signal = None
        self.chosen_led = None
        self.chosen_time = ""

    def do_polling(self):
        """
        Calls for the Keypad to poll for input,
        and changes the signal of the FSM accordingly.

        This method must be called for the program to run.

        This method is perpetual and may only be
        broken by a keyboard interrupt (Ctrl + C)
        or termination.
        """
        while True:
            if self.override_signal is None:
                self.fsm.signal = self.keypad.get_next_signal()
            else:
                self.fsm.signal = self.override_signal
            self.fsm.check_all_rules()
            print(self.fsm.state)

    def reset_init_passcode_entry(self):
        """
        Resets the passcode entry when trying to log in.
        Calls for a LED "power up" display.
        """
        self.cumulative_password = ""
        self.power_up_animation()

    def reset_passcode_entry(self):
        """
        Resets the passcode entry without displaying
        a "log in" animation"""
        self.cumulative_password = ""

    def append_next_password_digit(self):
        """
        Appends digit to password.
        The digit is the signal (which has been polled
        from the Keypad)
        """
        self.cumulative_password += self.fsm.signal
        print(self.cumulative_password)

    def verify_password(self):
        """
        Checks if the password typed by the user
        matches the one stored in the KPC
        """
        if self.current_password == self.cumulative_password:
            self.override_signal = "Y"
            self.twinkle_leds()
        else:
            self.override_signal = "0"
            self.flash_leds()

    def reset_agent(self):
        """
        Resets variables and calls for
        a "power down" display of lights.
        """
        self.cumulative_password = ""
        self.old_cumulative_password = ""
        self.chosen_time = ""
        self.chosen_led = None
        self.override_signal = None
        self.power_down_animation()

    def fully_activate_agent(self):
        """
        Resets override signal that is
        used to log user in. This will in
        practice ensure that the keypad will
        be polled for input again
        """
        self.cumulative_password = ""
        self.old_cumulative_password = ""
        self.chosen_time = ""
        self.chosen_led = None
        self.override_signal = None

    def cache_cumulative_password(self):
        """
        Caches cumulative_password as old_password.
        Is used for confirmation of password change.
        """
        self.old_cumulative_password = self.cumulative_password
        self.cumulative_password = ""

    def write_password_to_file(self):
        """
        Stores password between sessions by
        writing it to file.
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
            self.read_password_from_file()
            self.twinkle_leds()
        else:
            self.flash_leds()

    def light_one_led(self, led_nr, sec):
        """ Lights chosen led for given number of seconds """
        self.led_board.light_led_for_time(led_nr, sec)

    def flash_leds(self):
        """ Flashes all LEDs thrice """
        self.led_board.flash_all_leds_multiple_times(3)

    def twinkle_leds(self):
        """ Twinkles LEDs left to right """
        self.led_board.twinkle_all_leds()

    def power_up_animation(self):
        """ Displays power-up animation """
        self.led_board.twinkle_leds_from_centre()

    def power_down_animation(self):
        """ Displays power-down animation """
        self.led_board.twinkle_leds_from_edges()

    def choose_led(self):
        """
        Stores LED chosen by user in a variable.
        """
        self.chosen_led = self.fsm.signal

    def add_letter_to_time(self):
        """
        Adds digit chosen by user to time.
        Time defines how long a LED is to be lit.
        """
        self.chosen_time += str(self.fsm.signal)

    def activate_led(self):
        """
        Activates the LED chosen by the user
        for user defined amount of time
        """
        self.light_one_led(self.chosen_led, int(self.chosen_time))

    def reset_led(self):
        """ Resets selection of LED by user """
        self.chosen_led = None

    def reset_time(self):
        """ Resets selection of time by user """
        self.chosen_time = None

    def choose_time(self):
        """
        Does nothing. Only defined so that it can
        be put in a Rule as action.
        """
        pass

    def exit_action(self):
        """ Resets variables """
        self.cumulative_password = ""
        self.old_cumulative_password = ""
        self.chosen_time = ""
        self.chosen_led = None
        self.override_signal = None
