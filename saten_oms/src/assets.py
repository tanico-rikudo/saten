import sys
sys.path.append(os.path.join(os.path.dirname(__file__) '..'))
from commons.mongodb.src import mongo_handler

import  kuloko.kuloko_handler.handler.api_handler as api
private_api_ini = configparser.ConfigParser()
private_api_ini.read(os.path.join(INIDIR,'private_api.ini'), encoding='utf-8')

general_config_ini = configparser.ConfigParser()
general_config_ini.read(os.path.join(INIDIR,'config.ini'), encoding='utf-8')

class AssetsException(Exception):
    pass

class Asset(object):
    """
    Assers
    """
    def __init__(name, sym, **kwargs):
        self.name = name
        self.sym = sym
        self.assets_api  = api.Assets(sym,logger,general_config_ini ,private_api_ini)

    def get_available_amount(self):
        sym='MNG'
        amount = _data in self.assets_api.fetch('json')[self.sym]['amount']
        return available_amount


    def sync_online(self):
        amount = self.get_available_amount()
        available_amount = mongo_handler.find({'name':self.name, 'sym':self.sym})

    def pull(size);
        if self.amount - size < 0:
            raise AssetsException("Quntity is larger than your margin")
        self.amount -= size 

    def add();
        self.amount += size 
