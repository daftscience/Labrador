import subprocess
import time
import RPi.GPIO as GPIO

# list of BCM channels from RPO.GPIO (printed on the Adafruit PCB next to each button)
channel_list = [17, 22, 23, 27]
backlightOn = True

# event handler to toggle the TFT backlight
def toggleBacklight(channel):
    global backlightOn
    if backlightOn:
        backlightOn = False
        backlight.start(0)
    else:
        backlightOn = True
        backlight.start(100)

# event handler to manage button presses
def buttonEvent(channel):
    startTime = time.time()
    while GPIO.input(channel) == GPIO.LOW:
        time.sleep(0.02)
    print "Button #%d pressed for %f seconds." % (channel, time.time() - startTime)

# event handler to manage Pi shutdown
def poweroff(channel):
    startTime = time.time()
    while GPIO.input(channel) == GPIO.LOW:
        time.sleep(0.02)
    if (time.time() - startTime) &amp;amp;amp;gt; 2:
        subprocess.call(['poweroff'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# initialize GPIO library
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel_list, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(18, GPIO.OUT)
backlight = GPIO.PWM(18, 1000)
backlight.start(100)

print "Button #17 exits."
print "Button #22 toggles the TFT backlight."
print "Button #23 displayed the time the button is pressed."
print "!!! Pressing button #27 for at least 2 seconds, powers down the Pi !!!"

GPIO.add_event_detect(22, GPIO.FALLING, callback=toggleBacklight, bouncetime=200)
GPIO.add_event_detect(23, GPIO.FALLING, callback=buttonEvent, bouncetime=200)
GPIO.add_event_detect(27, GPIO.FALLING, callback=poweroff, bouncetime=200)

try:
    GPIO.wait_for_edge(17, GPIO.FALLING)
    print "Exit button pressed."

except:
    pass

# exit gracefully
backlight.stop()
GPIO.cleanup()
