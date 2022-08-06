class RGB:


    def __init__(self, r,g,b):
        self.r = r
        self.g = g
        self.b = b


    def __str__(self) -> str:
        return f"<R:{self.r} G:{self.g} B:{self.b}>"


    @property
    def codes(self):
        return (self.r, self.g, self.b)

    


def pcolor(color : RGB, string: str, inline = False):
    rgb_seq = f"\x1b[38;2;{color.r};{color.g};{color.b}m"
    end_seq = f"\x1b[0m"
    print(rgb_seq, end="")
    print(string, end="")

    if (inline):
        print(end_seq + " ", end="")
    else:
        print(end_seq,)

