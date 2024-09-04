import numpy as np

from RFanalyzer.transmission_lines.transmission_line import TransmissionLine
import RFanalyzer.constants as consts

class Microstrip(TransmissionLine):
    def __init__(self, length: float, width: float) -> None:
        '''
        Class for microstrip lines

        length      - Length of microstrip line (mm)

        width       - Width of microstrip line (mm)
        '''
        super().__init__(type="MS")

        self.L = length
        self.W = width
    
    def effectivePermittivity(self, stackup: "Stackup") -> float:
        '''
        Effective permittivity in a given substrate
        '''
        if self.W/stackup.H < 1:
            return (stackup.er + 1)/2 + (stackup.er - 1)/2 * (np.power(1 + 12*stackup.H/self.W, -0.5) + 0.04*(1 -self.W/stackup.H)**2)
        else:
            return (stackup.er + 1)/2 + (stackup.er - 1)/2 * np.power(1 + 12*stackup.H/self.W, -0.5)

    def impedance(self, stackup: "Stackup") -> float:
        '''
        Calculate impedance of microstrip line on a given stackup
        https://www.everythingrf.com/rf-calculators/microstrip-impedance-calculator
        '''
        e_eff = self.effectivePermittivity(stackup=stackup)
        if self.W/stackup.H < 1:
            return 60/np.sqrt(e_eff)*np.log(8*stackup.H/self.W+0.25*self.W/stackup.H)
        else:
            return 120*np.pi/(np.sqrt(e_eff)*(self.W/stackup.H+1.393+2/3*np.log(self.W/stackup.H+1.444)))
