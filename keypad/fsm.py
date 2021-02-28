from keypad.Rule import Rule
from keypad.State import State

class FSM:

    def __init__(self):
        #example from text, table end of page 9
        self.rules = []
        rule1 = Rule(State.S_int, "all_signals", State.S_Read, "KPC.reset_password_accumulator")
        self.rules.append(rule1)
        rule1 = Rule(State.S_Read, "all_digits", State.S_Read, "KPC.append_next_password_digit")
        self.rules.append(rule1)
        rule1 = Rule(State.S_Read, "*", State.S_Verify, "KPC.verify_password")
        self.rules.append(rule1)
        rule1 = Rule(State.S_Read, "all_signals", State.S_init, "KPC.reset_agent")
        self.rules.append(rule1)
        rule1 = Rule(State.S_Verify, "Y", State.S_Active, "KPC.fully_activate_agent")
        self.rules.append(rule1)
        rule1 = Rule(State.S_Verify, "all_signals", State.S_Active, "KPC.reset_agent")
        self.rules.append(rule1)
        self.fsm_state = rule1[0].s1
    
    def add_rule(self, state1, signal, state2, action):
        rule = Rule(state1, signal, state2, action)
        self.rules.append(rule)
    
    def get_next_singal(self):
        #query the agent 
        pass

    def run(self):
        pass
    
    def fire(self):
        pass
    

    

