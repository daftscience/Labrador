from gpiozero import Button


def update():
    print("Update")

class GPIO_Buttons:
    def __init__(self, pin, callback=none):
        self.b = Button(pin)
        self.b.when_released = callback


update = GPIO_Buttons(17, update)

while True:
    pass


# channel_list = [17, 22, 23, 27]
