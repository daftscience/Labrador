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

    @classmethod
    def refresh(cls):
        print("f5")
        cls.DEVICE.emit_click(uinput.KEY_F5)

    @classmethod
    def update(cls):
        cls.GIT.pull()
        _process = Popen(
            ['supervisorctl', 'reload'],
            stdout=PIPE)
        output, error = _process.communicate()
        sleep(10)
        cls.refresh()

if __name__ == '__main__':
    update_btn = Button(17)
    update_btn.when_released = GPIO_HANDLER.update

    update_btn = Button(22)
    update_btn.when_released = GPIO_HANDLER.refresh

    while True:
        pass


# channel_list = [17, 22, 23, 27]
