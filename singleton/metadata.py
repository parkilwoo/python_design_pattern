from typing import Any

class MyInt(type):
    def __call__(cls, *args: Any, **kwds: Any) -> Any:
        print("***** Here's My int *****", args)
        print("Now do whaterver you want with these objects...")
        return type.__call__(cls, *args, **kwds)
    
class int(metaclass=MyInt):
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        
i = int(4, 5)