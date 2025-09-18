from dataclasses import dataclass
from typing import Union

class ExpresionAritmetica:

    Number = Union[float,int]

    x:Number
    y:Number

    @staticmethod
    def suma(x:Number,y:Number):
        return x+y
    
    @staticmethod
    def prod(x:Number,y:Number):
        return x*y

if __name__ == "__main__":
    print(ExpresionAritmetica.suma(2,5.8))
    print(ExpresionAritmetica.prod(2,2))



