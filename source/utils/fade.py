from time import sleep as sl


def fade_out(self):
    for i in range(100, 0, -10):
        if not self.winfo_exists():
            break
        self.attributes("-alpha", i / 100)
        self.update()
        sl(1 / 100)

    self.attributes("-alpha", 0)


def fade_in(self):
    for i in range(0, 100, 10):
        if not self.winfo_exists():
            break
        self.attributes("-alpha", i / 100)
        self.update()
        sl(1 / 100)

    self.attributes("-alpha", 1)

