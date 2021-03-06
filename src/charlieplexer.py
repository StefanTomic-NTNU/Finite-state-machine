""" Contains Charlieplexer class """
import GPIOSimulator_v5 as GPIOSimulator


class Charlieplexer:
    """ Controls display of LEDs by charlieplexing """
    def __init__(self, GPIO):
        self.GPIO = GPIO

    def disable(self):
        self.GPIO.setup(GPIOSimulator.PIN_CHARLIEPLEXING_0, self.GPIO.IN)
        self.GPIO.setup(GPIOSimulator.PIN_CHARLIEPLEXING_1, self.GPIO.IN)
        self.GPIO.setup(GPIOSimulator.PIN_CHARLIEPLEXING_2, self.GPIO.IN)

    def fire_led_0(self):
        self.GPIO.setup(GPIOSimulator.PIN_CHARLIEPLEXING_0, self.GPIO.OUT, state=self.GPIO.HIGH)
        self.GPIO.setup(GPIOSimulator.PIN_CHARLIEPLEXING_1, self.GPIO.OUT, state=self.GPIO.LOW)
        self.GPIO.setup(GPIOSimulator.PIN_CHARLIEPLEXING_2, self.GPIO.IN)

    def fire_led_1(self):
        self.GPIO.setup(GPIOSimulator.PIN_CHARLIEPLEXING_0, self.GPIO.OUT, state=self.GPIO.LOW)
        self.GPIO.setup(GPIOSimulator.PIN_CHARLIEPLEXING_1, self.GPIO.OUT, state=self.GPIO.HIGH)
        self.GPIO.setup(GPIOSimulator.PIN_CHARLIEPLEXING_2, self.GPIO.IN)

    def fire_led_2(self):
        self.GPIO.setup(GPIOSimulator.PIN_CHARLIEPLEXING_0, self.GPIO.IN)
        self.GPIO.setup(GPIOSimulator.PIN_CHARLIEPLEXING_1, self.GPIO.OUT, state=self.GPIO.HIGH)
        self.GPIO.setup(GPIOSimulator.PIN_CHARLIEPLEXING_2, self.GPIO.OUT, state=self.GPIO.LOW)

    def fire_led_3(self):
        self.GPIO.setup(GPIOSimulator.PIN_CHARLIEPLEXING_0, self.GPIO.IN)
        self.GPIO.setup(GPIOSimulator.PIN_CHARLIEPLEXING_1, self.GPIO.OUT, state=self.GPIO.LOW)
        self.GPIO.setup(GPIOSimulator.PIN_CHARLIEPLEXING_2, self.GPIO.OUT, state=self.GPIO.HIGH)

    def fire_led_4(self):
        self.GPIO.setup(GPIOSimulator.PIN_CHARLIEPLEXING_0, self.GPIO.OUT, state=self.GPIO.HIGH)
        self.GPIO.setup(GPIOSimulator.PIN_CHARLIEPLEXING_1, self.GPIO.IN)
        self.GPIO.setup(GPIOSimulator.PIN_CHARLIEPLEXING_2, self.GPIO.OUT, state=self.GPIO.LOW)

    def fire_led_5(self):
        self.GPIO.setup(GPIOSimulator.PIN_CHARLIEPLEXING_0, self.GPIO.OUT, state=self.GPIO.LOW)
        self.GPIO.setup(GPIOSimulator.PIN_CHARLIEPLEXING_1, self.GPIO.IN)
        self.GPIO.setup(GPIOSimulator.PIN_CHARLIEPLEXING_2, self.GPIO.OUT, state=self.GPIO.HIGH)
