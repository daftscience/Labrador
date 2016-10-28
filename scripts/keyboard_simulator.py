import uinput


class keyboard:
    DEVICE = uinput.Device([
        uinput.KEY_E,
        uinput.KEY_H,
        uinput.KEY_L,
        uinput.KEY_O,
        uinput.KEY_FN_F5
    ])

    @classmethod
    def f_five(cls, key):
        print("f5")
        cls.DEVICE.emit_click(uinput.KEY_FN_F5)
