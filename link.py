import numpy as np
import textwrap

from RFanalyzer import constants

class Link:
    def __init__(self, receiver: "Receiver", transmitter: "Transmitter",
                 distance: float | np.ndarray, frequency: float | np.ndarray) -> None:
        '''
        Create a link between a receiver and transmitter system

        receiver    - Receiver object

        transmitter - Transmitter object

        distance    - Distance between receiver and transmitter in meters

        frequency   - Operating frequency in Hz
        '''
        self.rx = receiver
        self.tx = transmitter
        self.distance = distance
        self.frequency = frequency
    
    def __str__(self) -> str:
        '''
        Evaluate link details
        '''
        # EIRP
        eirp = self.tx.EIRP
        # Power at receiver
        P_receiver = self.powerAtReceiver()
        # Received power
        P_received = self.receivedPower()
        # Link margin
        margin = self.linkMargin()

        link_str = f'''EIRP = {eirp}
        Power at receiver = {P_receiver}
        Power received = {P_received}
        Link margin = {margin}'''

        return textwrap.dedent(link_str)
    
    def freeSpacePathLoss(self) -> float:
        '''
        Calculate free space path loss between the receiver and transmitter in dB
        '''
        wl = constants.c0/self.frequency
        return np.round(20*np.log10(4*np.pi*self.distance/wl), 3)
    
    def powerAtReceiver(self) -> float:
        '''
        Calculate power at the receiver
        '''
        return np.round(self.tx.EIRP-self.freeSpacePathLoss(), 3)

    def receivedPower(self) -> float:
        '''
        Calculate recieved power
        '''
        return np.round(self.powerAtReceiver()+self.rx.G, 3)

    def linkMargin(self) -> float:
        '''
        Calculate link margin in dB
        '''
        return np.round(self.powerAtReceiver()-self.rx.S, 3)