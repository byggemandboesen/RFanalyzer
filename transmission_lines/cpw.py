import numpy as np

from RFanalyzer.transmission_lines.transmission_line import TransmissionLine
import RFanalyzer.constants as consts

class CPW(TransmissionLine):
    def __init__(self, length: float, width: float, separation: float, grounded: bool = True) -> None:
        '''
        TODO - Class for coplanar waveguides

        
        length      - Length of transmission line (mm)

        width       - Width of signal line (mm)

        separation  - Separation between gnd and signal trace

        grounded    - Is it grounded on one side of the PCB (default=True)
        '''
        super().__init__()

        self.L = length
        self.W = width
        self.S = separation
        self.G = grounded
    
    def effectivePermittivity(self, stackup: "Stackup") -> float:
        pass
    
    def impedance(self, stackup: "Stackup") -> float:
        pass