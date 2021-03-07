""" File containing the Rule class """
from utils import \
    signal_is_digit, \
    signal_is_Y, \
    signal_is_star, \
    signal_is_hashtag, \
    signal_is_digit_0_to_5


class Rule:
    """ Rules represent the arcs in the FSM """
    def __init__(self, s1, signal, s2, action):
        self.s1 = s1
        self.signal = signal
        self.s2 = s2
        self.action = action

    #
    def verify_signal(self, signal):
        """
        Checks if given signal matches Rule signal
        :param: signal
        :returns: true if the self.signal is equal to the signal
        """
        if self.signal == "all_digits" and signal_is_digit(signal):
            return True
        elif self.signal == "all_signals":
            return True
        elif self.signal == "*" and signal_is_star(signal):
            return True
        elif self.signal == "Y" and signal_is_Y(signal):
            return True
        elif self.signal == "#" and signal_is_hashtag(signal):
            return True
        elif self.signal == "digit_in_0-5" and signal_is_digit_0_to_5(signal):
            return True
        return False

    def perform_action(self):
        """ Takes in the agent and performs the action """
        self.action()

    def match(self, state, signal):
        """ Matches the state and the signal """
        if state == self.s1 and self.verify_signal(signal):
            return True
        return False
