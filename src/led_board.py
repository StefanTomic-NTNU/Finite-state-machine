from src.charlieplexer import Charlieplexer
from src.utils import signal_is_digit_0_to_5


class LED_board:
    """ Simulated LED board. Acts though Charlieplexer """
    def __init__(self, GPIO):
        self.GPIO = GPIO
        self.charlieplexer = Charlieplexer(self.GPIO)

    def light_led(self, led_nr):
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

    def flash_all_leds(self):
        pass

    def twinkle_all_leds(self):
        pass

    # Trenger også metoder som brukes for å skru av og på.