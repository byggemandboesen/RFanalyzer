import numpy as np

from RFanalyzer.component import Component

class LumpedComponent(Component):
    def __init__(self, type: str, capacitance: float = 0, inductance: float = 0, resistance: float = 0) -> None:
        '''
        Lumped component parent class
        '''
        super().__init__(type="Lumped")
        self.lumped_type = type
        self.C = capacitance
        self.L = inductance
        self.R = resistance
    
    def impedance(self, f: float | np.ndarray) -> np.complex128 | np.ndarray:
        '''
        Calculate impedance of lumped component
        '''
        omega = 2*np.pi*f
        match self.lumped_type:
            case 'C':
                impedance = -1j/(omega*self.C)
            case 'L':
                impedance = omega*self.L*1j
            case 'R':
                impedance = self.R
            case _:
                raise ValueError(f"Unexpected error occured when parsing lumped component type: \"{self.type}\"")
            
        return impedance