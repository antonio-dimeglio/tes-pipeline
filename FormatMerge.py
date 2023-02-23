import argparse
from argparse import RawTextHelpFormatter
from os import listdir

def format_merge(files, path, new_path):
    new_file = open(f'{new_path}merged-library.fa', 'w')

    for file in files:
        # To edit a file it has to have an .fa extension and have a '-' has a separating character

        if file.lower().endswith('.fa') and '-' in file:

                print(f"Currently editing file {file}...")

                # The string before the '-' character corresponds to the specie name
                specie = file.split('-')[0]

                # To avoid filling the memory with the entire file it is read line by line and a new
                # temp file is created, using another Filestream object


                # Then, by iterating line by line in the file we either paste the whole line in the file
                # or we update the line adding the specie name to it and then write it
                with open(path + file, 'r') as fs:
                        for line in fs:
                                if line[0] == '>':
                                        line = '>' +  specie + '_' + line[1:]

                                new_file.write(line)
                fs.close()

    new_file.close()

description = '''\
This script assumes that all files follow a particular naming convention, i.e.
Specie-families.fa
The files produced will follow the naming convention:
Specie-families-up.fa
'''
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
            prog='InitialFormatting',
            description=description,
            formatter_class=RawTextHelpFormatter
    )

    parser.add_argument(
        'rm_output_path',
        help = 'Path to the folder containing the output of RepeatModeler'
    )
    parser.add_argument(
        'path_merged',
        help = 'Path to the folder where the new merged library will be put'
    )

    args = parser.parse_args()

    files = [f for f in listdir(args.rm_output_path)]

    format_merge(files, args.rm_output_path, args.path_merged)
