import argparse
from argparse import RawTextHelpFormatter
from os import listdir, path, makedirs
from os.path import isfile
from subprocess import Popen, PIPE, CalledProcessError 


description = '''\
This script is used to automate the process of using RepeatCraft \
on a set of output files obtained via RepeatMasker.
It requires the path to the folder containing the outputs \ 
(.out files, .gff files) and the path to the cfg file used by RepeatMasker
By default RM will be launched in loose mode, to change this \
use the optional flag -s
'''
mode = 'loose'

def launch_repeatcraft(file_path, file_name, rc_path):
	out = f"{file_path}.out"
	gff = f"{out}.gff"

	cmd = f"python3 {rc_path}repeatcraft.py -r {gff} -u {out} -o ./RepeatCraftOutput/{file_name}_RC -c {rc_path}repeatcraft.cfg --mode {mode}"
	
	print(cmd)


if __name__ == '__main__':
	parser = argparse.ArgumentParser(
	prog = 'RCPipeline',
	description = description,
	formatter_class = RawTextHelpFormatter
	)

	parser.add_argument(
		'rc_path',
		help = 'Path to RepeatCraft folder'
	)

	parser.add_argument(
		'rmo_path',
		help = 'Path to RepeatMasker output files'
	)

	parser.add_argument(
		'-s',
		action='store_true',
		help = 'Use flag to set RC to strict mode'
	)
	
	args = parser.parse_args()
	
	files = [f for f in listdir(args.rmo_path) if f.endswith('.tbl')]
	
	# Get name of output file from '.tbl' file
	files = [f.rpartition('.')[0] for f in files]

	if args.s:
		mode == 'strict'
	
	if not path.exists('./RepeatCraftOutput'):
		makedirs('./RepeatCraftOutput')

	for file in files:
		launch_repeatcraft(args.rmo_path+file, file,  args.rc_path)

