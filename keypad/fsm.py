import keypad.kpc as kpc
from keypad.rule import Rule
from keypad.state import State


class FSM:
    def __init__(self):
        #example from text, table end of page 9
        self.rules = []
        self.rules.append(Rule(State.S_int, "all_signals", State.S_Read, kpc.reset_password_accumulator))
        self.rules.append(Rule(State.S_Read, "all_digits", State.S_Read, kpc.append_next_password_digit))
        self.rules.append(Rule(State.S_Read, "*", State.S_Verify, kpc.verify_password))
        self.rules.append(Rule(State.S_Read, "all_signals", State.S_init, kpc.reset_agent))
        self.rules.append(Rule(State.S_Verify, "Y", State.S_Active, kpc.fully_activate_agent))
        self.rules.append(Rule(State.S_Verify, "all_signals", State.S_Active, kpc.reset_agent))
        self.fsm_state = State.S_init
    
    def add_rule(self, state1, signal, state2, action):
        rule = Rule(state1, signal, state2, action)
        self.rules.append(rule)
    
    def get_next_singal(self):
        # query the agent
        pass

    def run(self):
        pass
    
    def fire(self):
        pass
    

    

