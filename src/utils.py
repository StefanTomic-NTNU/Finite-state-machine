""" File containing helper methods. Mostly used by Rules """


def signal_is_digit(signal):
    """ Checks if the signal is a digit {0-9} """
    return 48 <= ord(signal) <= 57


def signal_is_star(signal):
    """ Checks if the signal is a star (asterisk) """
    return ord(signal) == 42


def signal_is_Y(signal):
    """
    Checks if the signal is a Y
    (Y is a token which may be sent from the KPC)
    """
    return ord(signal) == 89 or ord(signal) == 121


def signal_is_hashtag(signal):
    """
    Checks if the signal is a hashtag.
    This is used as a "canceling signal"
    in the FSM.
    """
    return ord(signal) == 35


def signal_is_digit_0_to_5(signal):
    """
    Checks if the signal is a digit from
    0 to 5. This is useful because we have
    LEDs 0 to 5.
    """
    return 48 <= ord(signal) <= 53
