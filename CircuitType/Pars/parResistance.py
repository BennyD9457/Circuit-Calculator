import circuitType.pars.parCurrent as parCurrent

def getResistance():
    c, volt = parCurrent.getCurrent()
    
    return volt/c