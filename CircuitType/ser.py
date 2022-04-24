import circuitType.sers.serCurrent as serCurrent
import circuitType.sers.serResistance as serResistance
import circuitType.sers.serVoltage as serVoltage

def ohmsLawStart():
    formula = input('What are you looking for (c/v/r)? ')
    
    if (formula == 'c'):
        print('Current: ', serCurrent.getCurrent())
        
    elif (formula == 'r'):
        print('Resistance: ', serResistance.getResistance())
        
    elif (formula == 'v'):
        print('Voltage: ', serVoltage.getVolt())
        
    else:
        print('Invalid')
        ohmsLawStart()