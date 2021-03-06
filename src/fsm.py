""" File contains the FSM class """
from src.rule import Rule
from src.state import State


class FSM:
    """
    Finite State Machine which represents
    the internal logic of the Keypad.
    It keeps track of the state as well as
    current signal.
    """

    def __init__(self, master_kpc):

        self.rules = []

        # example from text, table end of page 9
        self.add_rule(State.S_Init, "all_signals", State.S_Read_1, master_kpc.reset_init_passcode_entry)

        self.add_rule(State.S_Read_1, "all_digits", State.S_Read_1, master_kpc.append_next_password_digit)
        self.add_rule(State.S_Read_1, "u", State.S_Verify, master_kpc.verify_password)
        self.add_rule(State.S_Read_1, "all_signals", State.S_Init, master_kpc.reset_agent)

        self.add_rule(State.S_Verify, "Y", State.S_Active, master_kpc.fully_activate_agent)
        self.add_rule(State.S_Verify, "all_signals", State.S_Init, master_kpc.reset_agent)

        # example from Figure 4
        self.add_rule(State.S_Active, "u", State.S_Read_2, master_kpc.reset_passcode_entry)

        self.add_rule(State.S_Read_2, "u", State.S_Read_3, master_kpc.cache_cumulative_password)
        self.add_rule(State.S_Read_2, "all_digits", State.S_Read_2, master_kpc.append_next_password_digit)
        self.add_rule(State.S_Read_2, "all_signals", State.S_Active, master_kpc.fully_activate_agent)

        self.add_rule(State.S_Read_3, "u", State.S_Active, master_kpc.validate_password_change)
        self.add_rule(State.S_Read_3, "all_digits", State.S_Read_3, master_kpc.append_next_password_digit)
        self.add_rule(State.S_Read_3, "all_signals", State.S_Active, master_kpc.fully_activate_agent)

        self.state = State.S_Init
        self.signal = None
        self.master_kpc = master_kpc
    
    def add_rule(self, state1, signal, state2, action):
        rule = Rule(state1, signal, state2, action)
        self.rules.append(rule)

    def check_all_rules(self):
        for rule in self.rules:
            if rule.match(self.state, self.signal):
                self.fire(rule)
                break
    
    # def get_next_singal(self):
    #     # query the agent
    #     pass

    def run(self):
        pass
    
    def fire(self, rule):
        # print(f"{rule.s1} --> {rule.s2}")
        rule.perform_action()
        self.state = rule.s2
    

    

