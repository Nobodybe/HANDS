from pymouse import PyMouse
from pykeyboard import PyKeyboard
import time
k = PyKeyboard()
m = PyMouse()
time.sleep(5)
k.tap_key(k.right_key)
