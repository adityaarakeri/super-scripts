import time
import random
import string

from pymouse import PyMouse
from pykeyboard import PyKeyboard

m = PyMouse()
k = PyKeyboard()

### Automate the mouse ###
def automouse():
	while True:
		time.sleep(0.5)

		### Click on random location ###
		x, y = m.screen_size()
		x, y = random.randint(0, x), random.randint(0, y)
		m.move(x, y)
		# m.click(x,y)		# uncomment this at your own risk

		### Other stuff you can do ###
		# p = m.position() # gets mouse current position coordinates
		# m.press(x,y) # mouse button press
		# m.release(x,y) # mouse button release
		

### Automate the keyboard
def autokeyboard():
	N = 100
	s = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))

	time.sleep(2) # while this sleeps, go to somewhere where the script will type
	
	for i in s:
		k.press_key(i)
		k.release_key(i) # dont forget to release key after pressing
		time.sleep(0.1)


if __name__ == "__main__":
	### Uncomment/comment function to run
	automouse()
	# autokeyboard()
