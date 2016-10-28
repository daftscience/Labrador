from gpiozero import Button
import git

GIT_PATH = '/home/pi/projects/labrador/'

def update():
    print("Update")
    g = git.cmd.Git(GIT_PATH)
    g.pull()

update_btn = Button(17)
update_btn.hold_time = 7
update_btn.when_held = update

while True:
    pass


# channel_list = [17, 22, 23, 27]
