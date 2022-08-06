from typing import List
from colors.rgb import RGB
from colors.utils import split_str

class Gradient:
    steps : RGB =[]

    def len(self)->int:
        return len(self.colors)

    def add_color(self, color: RGB):
        self.steps.append(color)

    def add_colors(self, *args : RGB):
        for color in args:
            self.steps.append(color)
    
    @property
    def colors(self)-> List:
        return self.steps




def pgrad(grad : Gradient, string: str):

    END_SEQ = f"\x1b[0m"
    s = split_str(string, grad.len())

    for i in range(len(s)):
        c = grad.colors[i]
        rgb_seq = f"\x1b[38;2;{c.r};{c.g};{c.b}m"
        print(rgb_seq + s[i], end="")    

    print(END_SEQ)