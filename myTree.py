#!/path/to/python/interpreter
import os
from colorama import init

# init from colorama replaces ANSI escape sequences with Win32 equivalents
init()

root = os.getcwd()

def tree(path):
	subdirs = [entry for entry in os.scandir(path) if entry.is_dir()]
	if not subdirs:
		depth = path.count('\\') - root.count('\\')
		for entry in os.scandir(path):
			print('\033[1;37m{}|__{}'.format('  '*depth, entry.name))
	else:
		for entry in subdirs:
			depth = path.count('\\') - root.count('\\')
			print('\033[1;33m{}{}'.format('  '*depth, entry.name))
			tree(entry.path)

tree(root)

for entry in os.scandir(root):
	if not entry.is_dir():
		print('\033[1;37m{}'.format(entry.name))
