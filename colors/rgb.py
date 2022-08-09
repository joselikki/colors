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

    
def colorize(string: str, font : RGB = None, background: RGB = None) -> str:
    """
        Returns a string with rbg ANSII codes for color font and background
    """

    END_SEQ = f"\x1b[0m"
    rgb_frgnd = ""
    rgb_bkgnd = ""

    if font:
        rgb_frgnd = f"\x1b[38;2;{font.r};{font.g};{font.b}m"
    if background:
        rgb_bkgnd = f"\x1b[48;2;{background.r};{background.g};{background.b}m"

    return rgb_bkgnd + rgb_frgnd + string + END_SEQ
    