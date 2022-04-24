import circuitType.ser as ser
import circuitType.par as par

def start():
    circuit = input("Circuit Type (s/p): ")
    
    if (circuit == 's'):
        ser.ohmsLawStart()
        
    elif (circuit == 'p'):
        par.ohmsLawStart()
        
    else:
        print("Invalid")
        start()