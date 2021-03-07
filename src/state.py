""" File containing the State enum """
import enum


class State(enum.Enum):
    """ Enum representing the states in the FSM """
    S_Init = 1
    S_Read_1 = 2
    S_Verify = 3
    S_Active = 4
    S_Read_2 = 5
    S_Read_3 = 6
    S_LED = 7
    S_Time = 8
    S_Logout = 9
