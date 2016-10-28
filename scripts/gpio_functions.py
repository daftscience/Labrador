from gpiozero import Button
import git
import subprocess

GIT_PATH = '/home/pi/projects/labrador/'
restart_supervisor = "supervisorctl reload"


def update():
    print("Update")
    g = git.cmd.Git(GIT_PATH)
    g.pull()
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    print(output)

update_btn = Button(17)
update_btn.hold_time = 7
update_btn.when_held = update

while True:
    pass


# channel_list = [17, 22, 23, 27]
