import enum


class State(enum.Enum):
    S_init = 1
    S_Read_1 = 2
    S_Verify = 3
    S_Active = 4
    S_Read_2 = 5
    S_Read_3 = 6

