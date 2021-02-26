from keypad.Rule import Rule
from keypad.State import State

class FSM:

    def __init__(self):
        #example from text, table end of page 9
        rules = []
        rule1 = Rule(State.S_int, "all_signals", State.S_Read, "KPC.reset_password_accumulator")
        rules.append(rule1)
        rule1 = Rule(State.S_Read, "all_digits", State.S_Read, "KPC.append_next_password_digit")
        rules.append(rule1)
        rule1 = Rule(State.S_Read, "*", State.S_Verify, "KPC.verify_password")
        rules.append(rule1)
        rule1 = Rule(State.S_Read, "all_signals", State.S_init, "KPC.reset_agent")
        rules.append(rule1)
        rule1 = Rule(State.S_Verify, "Y", State.S_Active, "KPC.fully_activate_agent")
        rules.append(rule1)
        rule1 = Rule(State.S_Verify, "all_signals", State.S_Active, "KPC.reset_agent")
        rules.append(rule1)
    
    def add_rule(self, rule):
        self.rules.append(rule)
    
    def get_next_singal(self):
        pass

    def run(self):
        pass

    def match(self, state, signal):
        pass
    
    def fire(self):
        pass
    

    

