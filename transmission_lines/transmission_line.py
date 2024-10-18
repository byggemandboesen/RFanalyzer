from abc import abstractmethod
import numpy as np

from RFanalyzer.component import Component
import RFanalyzer.constants as consts
# https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Microwave_and_RF_Design_II_-_Transmission_Lines_(Steer)/03%3A_Planar_Transmission_Lines

class TransmissionLine(Component):
    def __init__(self) -> None:
        '''
        Parent class for all transmission lines
        '''
        super().__init__(type="TL")
    
    @abstractmethod
    def effectivePermittivity(self, stackup: "Stackup") -> float:
        '''
        Placeholder method for calculating effective permittivity of TL
        '''
        raise NotImplementedError("Not implemented for this type of transmission line!")
    
    @abstractmethod
    def impedance(self, stackup: "Stackup") -> float:
        '''
        Placeholder method for calculating impedance of TL
        '''
        raise NotImplementedError("Not implemented for this type of transmission line!")
    
    def inputImpedance(self, stackup: "Stackup", load_impedance: np.complex128,
                       frequency: float | np.ndarray) -> np.complex128 | np.ndarray:
        '''
        Placeholder method for calculating input impedance of TL
        '''
        Z0 = self.impedance(stackup=stackup)
        ZL = load_impedance
        L = self.L/10**3 # Convert to m
        
        e_eff = self.effectivePermittivity(stackup=stackup)
        omega = 2*np.pi*frequency
        beta = omega*np.sqrt(e_eff)/consts.c0

        Zin = Z0*(ZL+1j*Z0*np.tan(beta*L))/(Z0+1j*ZL*np.tan(beta*L))
        return Zin