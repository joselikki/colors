from typing import List
from colors.rgb import RGB
from colors.utils import split_str

class Gradient:
    step_list : RGB =[]

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





def gradiently(grad : Gradient, string: str) -> str:

    END_SEQ = f"\x1b[0m"
    s = split_str(string, grad.len())
    output = ""

    for i in range(len(s)):
        c = grad.steps[i]
        rgb_seq = f"\x1b[38;2;{c.r};{c.g};{c.b}m"
        output += rgb_seq +s[i]

    return output + END_SEQ