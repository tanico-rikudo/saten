import sys
sys.path.append(os.path.join(os.path.dirname(__file__) '..'))
from commons.mongodb.src import mongo_handler

import  kuloko.kuloko_handler.handler.api_handler as api
private_api_ini = configparser.ConfigParser()
private_api_ini.read(os.path.join(INIDIR,'private_api.ini'), encoding='utf-8')

general_config_ini = configparser.ConfigParser()
general_config_ini.read(os.path.join(INIDIR,'config.ini'), encoding='utf-8')


from queue import Queue
from threading import Thread
import time
from abc import ABC, ABCMeta, abstractmethod

class Worker(metaclass=ABCMeta):
    def __init__(self,queue_obj):
        self.queue_obj = queue_obj

    def get_queue(self):
        self.queue_ob.get()

    def set_queue(self):
        self.queue_ob.put()

    @abstractmethod
    def do(self):
        pass

    def main(self):
        # loop
        while True:
            # todo
            signal = self.do()
            if signal.code == 9:
                break
        
        # Terminate
        # todo
        return

class GMOExecution(object):

    def __init__(self, sym):
        # Set default value
        self.sym = sym
        self.side = None
        self.executionType = 'LIMIT'
        self.timeInForce = None
        self.losscutPrice = 0
        self.price = 0
        self.size = 0
        self.order_args = ["sym","side", "executionType","timeInForce","losscutPrice", "price","size"]

        # Set api
        self.execute_api  = api.Assets(sym,logger,general_config_ini ,private_api_ini)

    def execute(self,order_packet):
        if order_packet.side in ['BUY','SELL']:
            order_kwargs = copy.copy()
            for _key in self.order_args:
                order_kwargs
            order_kwargs = {
                "symbol": sym,
                "side": side,
                "executionType": executionType,
                "timeInForce": timeInForce,
                "price": price,
                "losscutPrice": losscutPrice,
                "size": size
            }
            self.execute_api.do_order(return_type='json',**order_kwargs)
        else:
            ValueError(order_packet.side)

class Executor(worker):
    def __init__(self,queue_obj, algorism):
        self.operator = AlgorismOperator(algorism)
        self.execution = Execution()
        pass

    def call_algo(self, market_packet):
        order_packet = self.operator.call(data)
        return order_packet


    def create_order(self,**kwargs):
        return order_packet


    def do():
        # fetch queue
        market_packet = self.get_queue()
        if market_packet is None:
            #todo
            return signal

        # ask algo
        algo_result = self.call_algo(market_packet)

        # create order
        order_packet = self.create_order(**{"algo_result":algo_result})

        # Execute
        self.execute(order_packet)

    
class Receiver(worker):
    def __init__(self, queue_obj):
        pass

    def fetch_data(self):
        # Fetch from DB
        pass

    def convert_data(self, data):
        # convert data for MarketDataPacket
        return  data

    def create_MarketDataPacket(self, data):
        # create MarketDataPacket  
        MarketDataPacket = MarketDataPacket(data)
        return  MarketDataPacket
        
    def do():
        # Fetch
        data = self.fetch_data()
        if data is None:
            pass
        
        # Create MarketDataPacket
        MarketDataPacket = self.create_packe(self.convert_data(data))

        # set queue
        if MarketDataPacket is not None:
            self.set_queue(MarketDataPacket)
            

class Signal(object):
    def __int__(code,content):
        self.code  = code
        self.content = content
        obj= {'code':code, 'content':content}
        if self.check(obj):
            return obj

    def check(obj):
        return True



if __name__ == '__main__':
    q = Queue()
    
    # lanch worker
    wokers = [ Executor(), Receiver()]
    for _woker in  wokers:
        thread = Thread(target=_worker, args=(q,))
        thread.setDaemon(True)
        thread.start()

    q.join()