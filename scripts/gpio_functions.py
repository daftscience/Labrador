from gpiozero import Button
import git
from time import sleep
from subprocess import Popen, PIPE
from keyboard_simulator import keyboard

GIT_PATH = '/home/pi/projects/labrador/'
restart_supervisor = "supervisorctl reload"


class GPIO_HANDLER:
    GIT = git.cmd.Git(GIT_PATH)

    def update(self):
        self.GIT.pull()
        _process = Popen(
            ['supervisorctl', 'reload'],
            stdout=PIPE)
        output, error = _process.communicate()
        sleep(2)
        keyboard.refresh()

if __name__ == '__main__':
    update_btn = Button(17)
    update_btn.when_released = GPIO_HANDLER.update

    while True:
        pass


# channel_list = [17, 22, 23, 27]
