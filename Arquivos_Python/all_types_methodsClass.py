class Connection:
    def __init__(self, host = 'server_xyz'):
        self.host = host

    @classmethod
    def UserLocal(cls):
        return cls(host='localhost')
    
    @staticmethod
    def somar(*args):
        return sum(args)
    
connect = Connection()
print(connect.host)
connect_local = Connection.UserLocal()
print(connect_local.host)
print(connect.somar(1,2,3,4))

