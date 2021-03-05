from src.utils import *


class Rule:

    def __init__(self, s1, signal, s2, action):
        self.s1 = s1
        self.signal = signal
        self.s2 = s2
        self.action = action

    # takes in a signal returns true if the self.signal is equal to the signal
    def verify_signal(self, signal):
        if self.signal == "signal_is_digit" and signal_is_digit(signal):
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

    # takes in the agent and performs the action
    def perform_action(self):
        self.action()

    # matches the state and the signal
    def match(self, state, signal):
        if state == self.s1 and self.verify_signal(signal):
            return True
        return False
