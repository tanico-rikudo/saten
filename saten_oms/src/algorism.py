from abc import ABC, ABCMeta, abstractmethod
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__) '..'))
from commons.util.utils import *
from packet import OrderDataPacket

class Algorism(metaclass=ABCMeta):
    """
    Base class
    """
    def __init_(self,name):
        self.name = name

    def call(self, data):
        pass

    def predict(self):
        pass


class UnderShaft(Algorism):
    """
    15mins Up/Down/Neutral 
    """
    def __init__(self ,name):
        super().__init__(name='UnderShaft')
        self.model_filepath = path #config #todo
        self.load_model()

    def call(self,market_packet):
        input_X = market_packet['v'][:300]
        signal = self.predict(input_X)
        order_packet = OrderDataPacket()

        # Up
        if signal == '1':
            order_packet.side = 'B'

        # Down
        if signal == '2':
            order_packet.side = 'S'

        # neutral
        if signal == '0':
            pass

        return order_packet

    def load_model(self,filepath=None):
        filepath = self.model_filepath  if filepath is None else filepath
        self.model = loadJbl(filepath)

    def predict(self, input_data):
        signal = self.model.predict(input_data)
        return signal 

        




