from typing import Tuple

class RGB:

    def __init__(self, r,g,b):
        self.r = r
        self.g = g
        self.b = b


    def __str__(self) -> str:
        return f"<R:{self.r} G:{self.g} B:{self.b}>"


    @property
    def codes(self) -> Tuple:
        return (self.r, self.g, self.b)


    
def colorize(color : RGB, string: str) -> str:
    """
        prints "string" into the terminal in "RGB" color
    """

    rgb_seq = f"\x1b[38;2;{color.r};{color.g};{color.b}m"
    end_seq = f"\x1b[0m"
    

    return rgb_seq + string + end_seq



