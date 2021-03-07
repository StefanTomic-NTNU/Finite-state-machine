""" File contains the FSM class """
from rule import Rule
from state import State


class FSM:
    """
    Finite State Machine which represents
    the internal logic of the Keypad.

    It keeps track of the state as well as
    current signal.
    It contains a list of Rules which represent
    the arcs in the FSM graph
    It also contains the current state signal.
    The Signal is given by the KPC, and the
    state is only changed bt the FSM itself
    by the firing of rules.
    """

    def __init__(self, master_kpc):

        # The list of rules represent the arcs in the FSM.
        # Most are taken from the diagrams in the assignment.
        # A diagram of the entire FSM can be found in the repo.
        self.rules = []

        # Initial state represents being logged out.
        self.add_rule(State.S_Init, "all_signals", State.S_Read_1, master_kpc.reset_init_passcode_entry)

        # The state of Read_1 represents trying to log in.
        self.add_rule(State.S_Read_1, "*", State.S_Verify, master_kpc.verify_password)
        self.add_rule(State.S_Read_1, "all_digits", State.S_Read_1, master_kpc.append_next_password_digit)
        self.add_rule(State.S_Read_1, "all_signals", State.S_Init, master_kpc.reset_agent)

        # The verification state is changed by the KPC (NOT the user).
        self.add_rule(State.S_Verify, "Y", State.S_Active, master_kpc.fully_activate_agent)
        self.add_rule(State.S_Verify, "all_signals", State.S_Init, master_kpc.reset_agent)

        # The active state represents the state of being logged in.
        self.add_rule(State.S_Active, "*", State.S_Read_2, master_kpc.reset_passcode_entry)
        self.add_rule(State.S_Active, "#", State.S_Logout, master_kpc.exit_action)
        self.add_rule(State.S_Active, "digit_in_0-5", State.S_LED, master_kpc.choose_led)

        # S_Read_2 represents the user trying to change the password.
        self.add_rule(State.S_Read_2, "*", State.S_Read_3, master_kpc.cache_cumulative_password)
        self.add_rule(State.S_Read_2, "#", State.S_Active, master_kpc.exit_action)
        self.add_rule(State.S_Read_2, "all_digits", State.S_Read_2, master_kpc.append_next_password_digit)
        self.add_rule(State.S_Read_2, "all_signals", State.S_Active, master_kpc.fully_activate_agent)

        # S_Read_3 requires the user to confirm the password.
        self.add_rule(State.S_Read_3, "*", State.S_Active, master_kpc.validate_password_change)
        self.add_rule(State.S_Read_3, "#", State.S_Active, master_kpc.exit_action)
        self.add_rule(State.S_Read_3, "all_digits", State.S_Read_3, master_kpc.append_next_password_digit)
        self.add_rule(State.S_Read_3, "all_signals", State.S_Active, master_kpc.fully_activate_agent)

        # S_LED is a state where the user has specified a LED to be lit
        self.add_rule(State.S_LED, "*", State.S_Time, master_kpc.choose_time)
        self.add_rule(State.S_LED, "#", State.S_Active, master_kpc.exit_action)
        self.add_rule(State.S_LED, "digit_in_0-5", State.S_LED, master_kpc.choose_led)

        # S_Time is the state where the user can define the time for the LED to be lit.
        self.add_rule(State.S_Time, "*", State.S_Active, master_kpc.activate_led)
        self.add_rule(State.S_Time, "#", State.S_Active, master_kpc.exit_action)
        self.add_rule(State.S_Time, "all_digits", State.S_Time, master_kpc.add_letter_to_time)

        # S_Logout is the state where the user may confirm logging out
        self.add_rule(State.S_Logout, "#", State.S_Init, master_kpc.reset_agent)
        self.add_rule(State.S_Logout, "all_signals", State.S_Active, master_kpc.fully_activate_agent)

        self.state = State.S_Init
        self.signal = None
        self.master_kpc = master_kpc

    def add_rule(self, state1, signal, state2, action):
        """
        Constructs Rule and adds it to rules.
        Rules represent the arcs in the FSM
        """
        rule = Rule(state1, signal, state2, action)
        self.rules.append(rule)

    def check_all_rules(self):
        """
        Checks if the FSMs state and signal matches
        that of any rule in rules. If so, fire rule.
        """
        for rule in self.rules:
            if rule.match(self.state, self.signal):
                self.fire(rule)
                break

    def fire(self, rule):
        """
        Fires Rule by changing the FSMs
        state according to the Rule.
        It also calls the method stored
        as "action" in the rule.
        This method is performed by the KPC
        """
        rule.perform_action()
        self.state = rule.s2
