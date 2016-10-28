from gpiozero import Button


def update():
    print("Update")

update = Button(17)
update.hold_time = 7
update.when_held = update

while True:
    pass


# channel_list = [17, 22, 23, 27]
