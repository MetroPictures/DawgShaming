import os, json, logging
from random import randint
from sys import argv, exit
from time import sleep

from core.api import MPServerAPI
from core.vars import DEFAULT_TELEPHONE_GPIO

ENDINGS = ["RandomEndMan.wav", "RandomEndScream.wav"]

class DawgShaming(MPServerAPI):
	def __init__(self):
		MPServerAPI.__init__(self)
		logging.basicConfig(filename=self.conf['d_files']['module']['log'], level=logging.DEBUG)

	def play_main_menu(self):
		choice = self.prompt(os.path.join("prompts", "BestFriendForeverMenu.wav"), release_keys=DEFAULT_TELEPHONE_GPIO)
		sleep(1)

		if self.say(os.path.join("prompts", ENDINGS[randint(0,1)]), interruptable=False):
			sleep(10)

		return self.play_main_menu()

	def run_script(self):
		super(DawgShaming, self).run_script()
		self.play_main_menu()

if __name__ == "__main__":
	res = False
	ds = DawgShaming()

	if argv[1] in ['--stop', '--restart']:
		res = ds.stop()
		sleep(5)

	if argv[1] in ['--start', '--restart']:
		res = ds.start()

	exit(0 if res else -1)


