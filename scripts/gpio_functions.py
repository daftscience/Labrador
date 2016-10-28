from gpiozero import Button


def update():
    print("Update")

update_btn = Button(17)
update_btn.hold_time = 7
update_btn.when_held = update

while True:
    pass


# channel_list = [17, 22, 23, 27]
