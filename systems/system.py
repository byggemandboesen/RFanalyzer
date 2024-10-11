import numpy as np

class System:
    def __init__(self, transmit_power: float | None, gain: float | None,
                 sensitivity: float | None) -> None:
        '''
        Base class for a receiver/transmitter system
        '''
        self.TX_P = transmit_power
        self.G = gain
        self.S = sensitivity

class Receiver(System):
    def __init__(self, gain: float, sensitivity: float) -> None:
        '''
        Create a receiver object from given receiver properties

        gain            - System gain

        sensitivity     - Sensitivity of receiver module in dB
        '''
        super().__init__(transmit_power=None, gain=gain, sensitivity=sensitivity)

class Transmitter(System):
    def __init__(self, transmit_power: float, gain: float) -> None:
        '''
        Create a transmitter object from given transmitter properties

        transmit_power  - Transmit power of the transmitter in dB
        
        gain            - System gain
        '''
        super().__init__(transmit_power=transmit_power, gain=gain, sensitivity=None)
        
        self.EIRP = np.round(transmit_power+gain, 3)
