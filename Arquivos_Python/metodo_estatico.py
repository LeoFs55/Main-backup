class Pessoa:
    @staticmethod
    def somar(*args):
        return sum(args)
    
p = Pessoa()

print(p.somar(1,2,3))