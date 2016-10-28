import uinput


class keyboard:
    DEVICE = uinput.Device([
        uinput.KEY_E,
        uinput.KEY_H,
        uinput.KEY_L,
        uinput.KEY_O,
    ])

    @classmethod
    def f_five(cls, key):
        cls.DEVICE.emit_click(uinput.KEY_H)
