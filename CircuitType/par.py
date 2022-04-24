import circuitType.pars.parCurrent as parCurrent
import circuitType.pars.parResistance as parResistance

def ohmsLawStart():
    formula = input('What are you looking for (c/r)? ')
    formula = formula.lower()
    
    if (formula == 'c'):
        current, volt = parCurrent.getCurrent()
        print('Current: ', current)
        
    elif (formula == 'r'):
        print('Resistance: ', parResistance.getResistance())

    else:
        
        print('Invalid')
        ohmsLawStart()