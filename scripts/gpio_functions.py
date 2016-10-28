from gpiozero import Button
import git
import subprocess
from keyboard_simulator import keyboard

GIT_PATH = '/home/pi/projects/labrador/'
restart_supervisor = "supervisorctl reload"


def update():
    print("Update")
    g = git.cmd.Git(GIT_PATH)
    g.pull()
    process = subprocess.Popen(
        restart_supervisor.split(),
        stdout=subprocess.PIPE)
    output, error = process.communicate()
    print(output)

update_btn = Button(17)
update_btn.hold_time = 2
update_btn.when_held = update


refresh_button = Button(22)
refresh_button.when_released = keyboard.f_five


test_button = Button(27)
test_button.when_released = keyboard.test

while True:
    pass


# channel_list = [17, 22, 23, 27]
