def signal_is_digit(signal):
    return 48 <= ord(signal) <= 57


def signal_is_star(signal):
    return ord(signal) == 42

def signal_is_Y(signal):
    return ord(signal) == 89 or ord(signal) == 121


def signal_is_hashtag(signal):
    return ord(signal) == 35


def signal_is_digit_0_to_5(signal):
    return 48 <= ord(signal) <= 53
