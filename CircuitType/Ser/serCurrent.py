import circuitType.sers.serVoltage as serVoltage

def getCurrent():
    volt = float(input('Voltage: '))
    resistors = int(input('Number of resistors: '))
    
    resistance = serVoltage.totalResistance(resistors)
    
    return volt / resistance