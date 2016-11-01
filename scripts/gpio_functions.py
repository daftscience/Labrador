from gpiozero import Button
import git
from subprocess import Popen, PIPE
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
    def restart_supervisor(cls):
        _process = Popen(['supervisorctl', 'reread'], stdout=PIPE)
        _process = Popen(['supervisorctl', 'reload'], stdout=PIPE)
        output, error = _process.communicate()

    @classmethod
    def rebuild_css(cls):
        _process = Popen([
            'scss',
            '/home/pi/projects/labrador/labrador/static/scss/theme.scss',
            'theme.css'],
            stdout=PIPE)
        output, error = _process.communicate()

    @classmethod
    def update(cls):
        print("Pulling latest update")
        cls.GIT.pull()
        print("restarting Services")
        cls.restart_supervisor()
        cls.refresh()
        print("refreshing")
        cls.refresh()

if __name__ == '__main__':
    update_btn = Button(17)
    update_btn.when_released = GPIO_HANDLER.update

    update_btn = Button(22)
    update_btn.when_released = GPIO_HANDLER.refresh

    while True:
        sleep(100)
        pass


# channel_list = [17, 22, 23, 27]
