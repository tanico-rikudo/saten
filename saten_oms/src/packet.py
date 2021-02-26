class OrderDataPacket(object):
    def __init__(self):
        self.side = None
        self.size = -1
        self.sym = None
        self.executionType = 'LIMIT'
        self.timeInForce = None
        self.losscutPrice = 0
        self.price = 0
        self.order_args = ["sym","side", "executionType","timeInForce","losscutPrice", "price","size"]

    # Gettter/Setter
    @property
    def side(self):
        return self.side
    
    @side.setter
    def side(self, side):
        if self.validate_side(side):
           self.side = side
        return 

    @property
    def size(self):
        return self.size
    
    @size.setter
    def size(self, size):
        if self.validate_size(size):
            self.size = size

    @property
    def sym(self):
        return self.sym
    
    @sym.setter
    def sym(self, sym):
        if self.validate_sym(sym):
            self.sym = sym

    # Validator
    def validate_side(self, side):
        if side  in  ['B','S']:
            return True
        else:
            return False

    def validate_size(self, size, **kwargs):
        if size < 0:
            return False
        if 'upper' in kwargs.keys():
            if size > kwargs['upper']:
                return  False
        return True

    def validate_sym(self, sym, **kwargs):
        #todo
        pass
        return True
    
class MarketDataPacket(object):
    def __init__(self,info_type, signal):
        self.info_type = info_type
        self.signal = signal