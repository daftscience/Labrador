import uinput


class keyboard:
    DEVICE = uinput.Device([uinput.KEY_F5])

    @classmethod
    def refresh(cls, key):
        print("f5")
        cls.DEVICE.emit_click(uinput.KEY_F5)

    @classmethod
    def test(cls, key):
        print("test")
        cls.DEVICE.emit_click(uinput.KEY_E)
