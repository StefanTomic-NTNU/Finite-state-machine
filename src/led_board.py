""" Contains LED board class """
import time
from datetime import datetime, timedelta
from charlieplexer import Charlieplexer
from utils import signal_is_digit_0_to_5


class LED_board:
    """ Simulated LED board. Acts though Charlieplexer """
    def __init__(self, GPIO):
        self.GPIO = GPIO
        self.charlieplexer = Charlieplexer(self.GPIO)

    def light_led(self, led_nr):
        """
        Lights selected LED. LED stays lit
        until disabled or another LED is lit.
        """
        fire_led = {
            '0': self.charlieplexer.fire_led_0,
            '1': self.charlieplexer.fire_led_1,
            '2': self.charlieplexer.fire_led_2,
            '3': self.charlieplexer.fire_led_3,
            '4': self.charlieplexer.fire_led_4,
            '5': self.charlieplexer.fire_led_5
        }
        if signal_is_digit_0_to_5(str(led_nr)):
            fire_led[str(led_nr)]()
            self.GPIO.show_leds_states()

    def light_led_for_time(self, led_nr, sec):
        """ Lights selected LED for given number of seconds """
        self.light_led(led_nr)
        time.sleep(sec)
        self.disable_all_leds()

    def flash_all_leds_once(self):
        """
        Fires alle leds for 1 second

        Since the charlieplexer does not allow
        multiple LEDs to be fired simultaneously,
        LEDs are fired one at a time in rapid succession.
        IRL this will give the appearance of all LED being
        lit simultaneously.
        """
        self.fire_leds_for_seconds((0, 1, 2, 3, 4, 5), 1)
        self.disable_all_leds()

    def flash_all_leds_multiple_times(self, times):
        """
        Flashes LEDs in 300ms intervals, given number
        of times.

        Since the charlieplexer does not allow
        multiple LEDs to be fired simultaneously,
        LEDs are fired one at a time in rapid succession.
        IRL this will give the appearance of all LED being
        lit simultaneously.
        """
        for i in range(times):
            self.fire_leds_for_seconds((0, 1, 2, 3, 4, 5), 0.3)
            if i != times-1:
                self.disable_all_leds_for_seconds(0.3)
            else:
                # This minimizes the time the user cannot interact with the Keypad
                # Yet it makes sure all leds are disabled by the end of the flashing
                self.disable_all_leds()

    def twinkle_all_leds(self):
        """ Lights all LEDs in succession, left to right """
        for i in range(6):
            self.light_led(i)
            time.sleep(0.5)
        self.disable_all_leds()

    def fire_leds_for_seconds(self, leds, sec):
        """
        Flashes given tuple of LEDs for given number
        of seconds.

        Since the charlieplexer does not allow
        multiple LEDs to be fired simultaneously,
        LEDs are fired one at a time in rapid succession.
        IRL this will give the appearance of all LED being
        lit simultaneously.
        """
        end_time = datetime.now() + timedelta(seconds=sec)
        while datetime.now() < end_time:
            for led in leds:
                self.light_led(led)

    def disable_all_leds(self):
        """ Disables all LEDs """
        self.charlieplexer.disable()
        self.GPIO.show_leds_states()

    def disable_all_leds_for_seconds(self, sec):
        """
        Disables all LEDs for given number of seconds.
        This will spam the console.
        """
        end_time = datetime.now() + timedelta(seconds=sec)
        while datetime.now() < end_time:
            self.charlieplexer.disable()
            self.GPIO.show_leds_states()

    def twinkle_leds_from_centre(self):
        """
        Twinkles all LEDs form the centre like so:

            --
           -  -
          -    -

        Since the charlieplexer does not allow
        multiple LEDs to be fired simultaneously,
        LEDs are fired one at a time in rapid succession.
        IRL this will give the appearance of all LED being
        lit simultaneously.
        """
        self.twinkle_led_combinations(((2, 3), (1, 4), (0, 5)))

    def twinkle_leds_from_edges(self):
        """
        Twinkles all LEDs form the edges like so:

          -    -
           -  -
            --

        Since the charlieplexer does not allow
        multiple LEDs to be fired simultaneously,
        LEDs are fired one at a time in rapid succession.
        IRL this will give the appearance of all LED being
        lit simultaneously.
        """
        self.twinkle_led_combinations(((0, 5), (1, 4), (2, 3)))

    def twinkle_led_combinations(self, combinations):
        """
        Helper method to aid with twinkling of
        multiple lights in succession.

        Since the charlieplexer does not allow
        multiple LEDs to be fired simultaneously,
        LEDs are fired one at a time in rapid succession.
        IRL this will give the appearance of all LED being
        lit simultaneously
        """
        for combination in combinations:
            self.fire_leds_for_seconds(combination, 0.5)
        self.disable_all_leds()
