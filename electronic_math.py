import math

def ind_Rx (frequency, inductance):
     Rx = 2 * math.pi * frequency * inductance
     return Rx

def cap_Rx (frequency, capacitance):
     Rx = 1 / (2 * math.pi * frequency * capacitance)
     return Rx

def res_freq (capacitance, inductance):
     frequency = 1 / ( 2 * math.pi * math.sqrt(capacitance * inductance))
     return  frequency

def high_pass_freq (capacitance, resistance):
     pass_freq = 1 / (2 * math.pi * resistance * capacitance)
     return pass_freq

