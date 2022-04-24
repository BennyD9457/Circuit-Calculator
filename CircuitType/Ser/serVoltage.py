def getVolt():
    resistors = int(input('Number of resistors: '))
    resistance = totalResistance(resistors)
    
    current = float(input('What is the current? '))
    
    return current * resistance
    

def totalResistance(resistors):
    temp = 0
    
    for i in range(resistors):
        strength = float(input('Resistor[{}] Strength: '.format(i+1)))
        temp += strength
        
    return temp