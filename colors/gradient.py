from typing import List
from colors.rgb import RGB
from colors.utils import split_str

class Gradient:

    def __init__(self) -> None:
        self.step_list : RGB =[]

    def len(self)->int:
        return len(self.step_list)

    def add_step(self, color: RGB):
        self.step_list.append(color)

    def add_steps(self, *args : RGB):
        for color in args:
            self.step_list.append(color)
    
    @property
    def steps(self)-> List:
        return self.step_list

def fontgrad(string: str, grad : Gradient) -> str:
   
    output = ""
    #Spliting the string to apply a different RBG to each chunk
    s = split_str(string, grad.len())

    for i in range(len(s)):
        c = grad.steps[i]
        rgb_seq = f"\x1b[38;2;{c.r};{c.g};{c.b}m"
        output += rgb_seq +s[i]

    return output + "\x1b[0m" # reset ANSII sequence

    
def backgrad(string: str , background: Gradient, fcolor: RGB = None) -> str:
    

    font_col_seq = ""
    output = ""
    #Spliting the string to apply a different RBG to each chunk
    s = split_str(string, background.len())

    if fcolor:
        font_col_seq = f"\x1b[38;2;{fcolor.r};{fcolor.g};{fcolor.b}m"

    for i in range(len(s)):
        c = background.steps[i]
        rgbb_seq = f"\x1b[48;2;{c.r};{c.g};{c.b}m"
        output += rgbb_seq + s[i]


    return font_col_seq + output + "\x1b[0m" # reset ANSII sequence