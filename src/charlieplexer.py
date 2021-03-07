""" Contains Charlieplexer class """
import GPIOSimulator_v5 as GPIOSimulator


class Charlieplexer:
    """
    Controls display of LEDs in the GPIOsimulator
    by charlieplexing.

    Charlieplexing is a method of controlling multiple
    LEDs with only a few pins.

    NOTE: CHARLIEPLEXED CIRCUITS MAY ONLY FIRE ONE
          LED AT A TIME
    """
    def __init__(self, GPIO):
        self.GPIO = GPIO

    def disable(self):
        """ Disables all LEDs """
        self.GPIO.setup(GPIOSimulator.PIN_CHARLIEPLEXING_0, self.GPIO.IN)
        self.GPIO.setup(GPIOSimulator.PIN_CHARLIEPLEXING_1, self.GPIO.IN)
        self.GPIO.setup(GPIOSimulator.PIN_CHARLIEPLEXING_2, self.GPIO.IN)

    def fire_led_0(self):
        """
        Fires LED0.

        (Disables all other LEDs because the
        Charlieplexer can only fire one LED at a time)
        """
        self.GPIO.setup(GPIOSimulator.PIN_CHARLIEPLEXING_0, self.GPIO.OUT, state=self.GPIO.HIGH)
        self.GPIO.setup(GPIOSimulator.PIN_CHARLIEPLEXING_1, self.GPIO.OUT, state=self.GPIO.LOW)
        self.GPIO.setup(GPIOSimulator.PIN_CHARLIEPLEXING_2, self.GPIO.IN)

    def fire_led_1(self):
        """
        Fires LED1.

        (Disables all other LEDs because the
        Charlieplexer can only fire one LED at a time)
        """
        self.GPIO.setup(GPIOSimulator.PIN_CHARLIEPLEXING_0, self.GPIO.OUT, state=self.GPIO.LOW)
        self.GPIO.setup(GPIOSimulator.PIN_CHARLIEPLEXING_1, self.GPIO.OUT, state=self.GPIO.HIGH)
        self.GPIO.setup(GPIOSimulator.PIN_CHARLIEPLEXING_2, self.GPIO.IN)

    def fire_led_2(self):
        """
        Fires LED2.

        (Disables all other LEDs because the
        Charlieplexer can only fire one LED at a time)
        """
        self.GPIO.setup(GPIOSimulator.PIN_CHARLIEPLEXING_0, self.GPIO.IN)
        self.GPIO.setup(GPIOSimulator.PIN_CHARLIEPLEXING_1, self.GPIO.OUT, state=self.GPIO.HIGH)
        self.GPIO.setup(GPIOSimulator.PIN_CHARLIEPLEXING_2, self.GPIO.OUT, state=self.GPIO.LOW)

    def fire_led_3(self):
        """
        Fires LED3.

        (Disables all other LEDs because the
        Charlieplexer can only fire one LED at a time)
        """
        self.GPIO.setup(GPIOSimulator.PIN_CHARLIEPLEXING_0, self.GPIO.IN)
        self.GPIO.setup(GPIOSimulator.PIN_CHARLIEPLEXING_1, self.GPIO.OUT, state=self.GPIO.LOW)
        self.GPIO.setup(GPIOSimulator.PIN_CHARLIEPLEXING_2, self.GPIO.OUT, state=self.GPIO.HIGH)

    def fire_led_4(self):
        """
        Fires LED4.

        (Disables all other LEDs because the
        Charlieplexer can only fire one LED at a time)
        """
        self.GPIO.setup(GPIOSimulator.PIN_CHARLIEPLEXING_0, self.GPIO.OUT, state=self.GPIO.HIGH)
        self.GPIO.setup(GPIOSimulator.PIN_CHARLIEPLEXING_1, self.GPIO.IN)
        self.GPIO.setup(GPIOSimulator.PIN_CHARLIEPLEXING_2, self.GPIO.OUT, state=self.GPIO.LOW)

    def fire_led_5(self):
        """
        Fires LED5.

        (Disables all other LEDs because the
        Charlieplexer can only fire one LED at a time)
        """
        self.GPIO.setup(GPIOSimulator.PIN_CHARLIEPLEXING_0, self.GPIO.OUT, state=self.GPIO.LOW)
        self.GPIO.setup(GPIOSimulator.PIN_CHARLIEPLEXING_1, self.GPIO.IN)
        self.GPIO.setup(GPIOSimulator.PIN_CHARLIEPLEXING_2, self.GPIO.OUT, state=self.GPIO.HIGH)
