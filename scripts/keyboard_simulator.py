import uinput


class keyboard:
    DEVICE = uinput.Device([
        uinput.KEY_E,
        uinput.KEY_H,
        uinput.KEY_L,
        uinput.KEY_O,
    ])
   @staticmethod
   def f_five(key):
		device.emit_click(uinput.KEY_H)
