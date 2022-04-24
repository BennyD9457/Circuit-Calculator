def getCurrent():
    resistors = int(input('Number of resistors: '))
    volt = float(input('Volt: '))
    
    return totalRisitance(resistors, volt), volt
    
    
def totalRisitance(resistors, volt):
    temp = 0
    
    for i in range(resistors):
        strength = float(input('Resistor[{}] Strength: '.format(i+1)))
        temp += volt/strength
        
    return temp