import numpy as np
import textwrap

class System:
    def __init__(self, transmit_power: float | None, gain: float | None,
                 sensitivity: float | None, front_end_components: list["FrontEndComponent"]) -> None:
        '''
        Base class for a receiver/transmitter system
        '''
        self.TX_P = transmit_power
        self.G = gain
        self.S = sensitivity
        # TODO - System noise

class Receiver(System):
    def __init__(self, sensitivity: float, antenna: "Antenna",
                 front_end_components: list["FrontEndComponent"] | None = None) -> None:
        '''
        Create a receiver object from given receiver properties

        sensitivity             - Sensitivity of receiver module in dB

        antenna                 - Receiver antenna

        front_end_components    - List of front end components as seen from antenna
        '''
        total_gain = antenna.G if front_end_components == None else antenna.G+np.sum([component.G for component in front_end_components])
        super().__init__(transmit_power=0, gain=total_gain, sensitivity=sensitivity, front_end_components=front_end_components)

class Transmitter(System):
    def __init__(self, transmit_power: float, antenna: "Antenna",
                 front_end_components: list["FrontEndComponent"] | None = None) -> None:
        '''
        Create a transmitter object from given transmitter properties

        transmit_power          - Transmit power of the transmitter in dB

        antenna                 - Transmitter antenna
        
        front_end_components    - List of front end components as seen from power source
        '''
        total_gain = antenna.G if front_end_components == None else antenna.G+np.sum([component.G for component in front_end_components])
        super().__init__(transmit_power=transmit_power, gain=total_gain, sensitivity=None, front_end_components=front_end_components)
        
        self.EIRP = np.round(transmit_power+total_gain, 3)
