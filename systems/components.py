import numpy as np
import textwrap

class FrontEndComponent:
    def __init__(self, gain: float, noise_temperature: float | None,
                 noise_figure: float | None) -> None:
        T0 = 290
        self.G = 10**(gain/10)

        if noise_temperature == None and noise_figure == None:
            # Assume no noise
            self.NF = 1
            self.NT = 0
        elif noise_temperature == None:
            self.NF = 10**(-noise_figure/10) # Convert to linear scale
            self.NT = (noise_figure-1)*T0
        elif noise_figure == None:
            self.NT = noise_temperature
            self.NF = 1+(noise_temperature/T0)
        else:
            raise ValueError("Only noise figure or -temperature should be given - not both!")
    
    def __str__(self) -> str:
        '''
        Print component properties
        '''
        component_str = f'''Gain = {np.round(10*np.log10(self.G), 3)}dB
        Noise figure = {np.round(10*np.log10(self.NF), 3)}dB
        Noise temperature = {np.round(self.NT, 3)}K
        '''

        return textwrap.dedent(component_str)

class Amplifier(FrontEndComponent):
    def __init__(self, gain: float, noise_temperature: float | None,
                 noise_figure: float | None) -> None:
        '''
        Amplifier class

        gain                - Gain of unit

        noise_temperature   - Noise temperature of unit (K)

        noise_figure        - Noise figure of unit (dB)
        '''
        super().__init__(gain=gain, noise_temperature=noise_temperature, noise_figure=noise_figure)

class Filter(FrontEndComponent):
    def __init__(self, insertion_loss: float) -> None:
        '''
        Filter class

        insertion_loss      - Insertion loss of unit (dB)
        '''
        # Insertion loss equal to noise figure
        # https://www.ittc.ku.edu/~jstiles/622/handouts/Noise%20Figure%20of%20Passive%20Devices.pdf
        super().__init__(gain=insertion_loss, noise_figure=insertion_loss)
