import numpy as np

from RFanalyzer.transmission_lines.transmission_line import TransmissionLine
import RFanalyzer.constants as consts

class Coax(TransmissionLine):
    def __init__(self, length: float, core_radius: float, dielectric_radius: float) -> None:
        '''
        Class for coax cables

        
        length              - Length of transmission line (mm)

        core_radius         - Radius of inner core

        dielectric_radius   - Radius of dielectric

        Units of the two radi should be similar
        '''
        super().__init__()

        self.L = length
        self.CORE_R = core_radius
        self.DIELECTRIC_R = dielectric_radius
    
    def impedance(self, stackup: "Stackup") -> float:
        '''
        Calculate impedance of coax cable

        Note, only the relative permittivity of the stackup is used!
        '''
        return 138*np.log10(self.CORE_R/self.DIELECTRIC_R)/np.sqrt(stackup.er)