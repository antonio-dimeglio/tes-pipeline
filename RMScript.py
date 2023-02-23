import argparse 
from os import listdir
from os.path import isfile, abspath
from argparse import RawTextHelpFormatter
from subprocess import Popen, PIPE, CalledProcessError

RMFLAGS = [
	'-e ncbi',
	'-pa 8',
	'-gff',
	'-no_is',
	'-nolow',
	'-norna',
	'-s'
]

description = '''\
This script is used to utilize the RepeatMasker tool given its path
it requires the path to the merged library and the path where all 
assemblies will be found
'''

if __name__ == '__main__':
	parser = argparse.ArgumentParser(
		prog='RMPipeline',
		description=description,
		formatter_class=RawTextHelpFormatter
	)

	parser.add_argument(
		'rmpath',
		help='Path to the RepeatMasker executable'
	)

	parser.add_argument(
		'lib_path',
		help='Path to the library'
	)
	
	parser.add_argument(
		'asm_path',
		help='Path to the assemblies folder'
	)
	

	args = parser.parse_args()
	
	entries = listdir(args.asm_path)

	command = f"{args.rmpath} -lib {args.lib_path} {' '.join(RMFLAGS)} {args.asm_path}" 

	for entry in entries:
		# Check if file extension is .fna		
		if (entry.endswith('.fna')):
			cmd = f"{command}{entry}"
			print(f"Currently working with file {entry}...")

			with Popen(cmd, stdout=PIPE, bufsize=1, universal_newlines=True, shell=True) as p:
				for line in p.stdout:
					print(line, end='')
			
			if p.returncode != 0:
				raise CalledProcessError(p.returncode, p.args)
