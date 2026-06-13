import time
import pydirectinput
import random
import keyboard

inputs = pydirectinput


keyboard.wait("alt")
for x in range(3):
	x += 1
	time.sleep(1)
	print(f"switch to the game now.. {x}")
	
while True:
	if keyboard.is_pressed("esc"):
		break
	
	def moving():
		def domove(key):
			inputs.keyDown(key)
			time.sleep(random.uniform(1.0,3.0))
			inputs.keyUp(key)
		r_key = random.randint(1, 4)
		if r_key == 1:
			domove("w")
		elif r_key == 2:
			domove("s")
		elif r_key == 3:
			domove("d")
		elif r_key == 4:
			domove("a")
		time.sleep(1)

	def shouting():
		r_mouse = random.randint(1, 2)
		if r_mouse == 1:
			inputs.keyDown("l")
			time.sleep(random.uniform(0.1, 0.3))
			inputs.keyUp("l")
		elif r_mouse == 2:
			inputs.press("k")
			time.sleep(random.uniform(0.1, 0.3))
			inputs.press("k")
		time.sleep(1)
			
	moving()
	shouting()
	
print("Cleaning up keyboard hooks...")
keyboard.unhook_all()
print("bye")

