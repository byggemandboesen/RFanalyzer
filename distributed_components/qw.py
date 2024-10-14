import numpy as np

from RFanalyzer.distributed_components.distributed_component import DistributedComponent
import RFanalyzer.constants as consts

class QW(DistributedComponent):
    def __init__(self, load_impedance: np.complex128, target_impedance: np.complex128, frequency: float) -> None:
        '''
        Create a QW transformer for a given center frequency

        load_impedance      - Load impedance to transform from

        target_impedance    - Impedance to transform to

        frequency           - Center frequency of operation
        '''
        super().__init__()

        self.ZL = load_impedance
        self.Zin = target_impedance
        self.Z0 = np.sqrt(self.ZL*self.Zin)
    
    def impedance(self) -> np.complex128:
        '''
        Impedance of QW transformer
        '''
        return self.Z0
    
    def inputImpedance(self, transmission_line: "TransmissionLine", stackup: "Stackup",
                       load_impedance: np.complex128, frequency: float | np.ndarray) -> np.complex128:
        '''
        Input impedance after QW transformer
        '''
        return transmission_line.inputImpedance(stackup=stackup, load_impedance=load_impedance, frequency=frequency)
    
    def length(self, transmission_line: "TransmissionLine", stackup: "Stackup",
               frequency: float | np.ndarray) -> float | np.ndarray:
        '''
        Length of the QW transformer in meters

        transmission_line   - TransmissionLine object to implement QW transformer (microstrip, coax etc)

        stackup             - Stackup on which the QW transformer is implemented

        frequency           - Frequency of the QW transformer
        '''
        er = transmission_line.effectivePermittivity(stackup=stackup)
        wl = consts.c0/(frequency*np.sqrt(er))

        return wl/4