import numpy as np

# TODO - Optimize lumped component values for best matching
# TODO - Monte carlo sensitivity analysis on circuit

class Circuit:
    def __init__(self, components: list, stackup: "Stackup") -> None:
        '''
        Build a circuit from a list of components
        '''
        self.COMPONENTS = components
        self.STACKUP = stackup
    
    def inputImpedance(self, f: float | np.ndarray) -> np.complex128 | np.ndarray[np.complex128]:
        '''
        Calculate input impedance of circuit
        '''
        pass

    def returnLoss(self, f: float | np.ndarray) -> np.complex128 | np.ndarray[np.complex128]:
        '''
        Calculate return loss of circuit
        '''
        Z_in = self.inputImpedance(f=f)
        # Impedance of source load
        Z0 = self.COMPONENTS[0].impedance
        
        return (Z_in-Z0)/(Z_in+Z0)