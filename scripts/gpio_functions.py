from gpiozero import Button
import git
from time import sleep
from subprocess import Popen, PIPE
from keyboard_simulator import keyboard
import uinput


GIT_PATH = '/home/pi/projects/labrador/'
restart_supervisor = "supervisorctl reload"


class GPIO_HANDLER:
    GIT = git.cmd.Git(GIT_PATH)
    DEVICE = uinput.Device([uinput.KEY_F5])

    def refresh(self):
        print("f5")
        self.DEVICE.emit_click(uinput.KEY_F5)

    def update(self):
        self.GIT.pull()
        _process = Popen(
            ['supervisorctl', 'reload'],
            stdout=PIPE)
        output, error = _process.communicate()
        sleep(2)
        self.DEVICE.refresh()

if __name__ == '__main__':
    update_btn = Button(17)
    update_btn.when_released = GPIO_HANDLER.update

    while True:
        pass


# channel_list = [17, 22, 23, 27]
