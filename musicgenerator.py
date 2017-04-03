import sys
import argparse
import generator


assert sys.version >= '3.0', "This program does not work with older versions of Python.\
 Please install Python 3.0 or later."


def parse():
    """Main entry point."""
    parser = argparse.ArgumentParser()
    parser.add_argument('--l', help='l - length of the music')
    parser.add_argument('--o', help='o - path to output file')
    parser.add_argument('--s', help='s - scale of chords choose from: \'minor\',\
                                    \'major\', \'C\', \'E\',\'AGH\', \'revolution\',\
                                     \'weird\', \'single\',\'dominant\', \'default\'')
    parser.add_argument('--bpm', help='bpm - beats per minute. Range 0-600. Best outcome using 100-400')
    args = parser.parse_args()
    args = vars(args)
    global time, scale, path, bpm

    print("Welcome to MusicGen!\n")

    time = args['l']
    if time is None:
        print("Using default value of time.\n")
        time = 60
    time = int(time)
    if time <= 0:
        print("Using default value of time.\n")
        time = 60

    scale = args['s']
    if scale is None:
        print("Using default scale.\n")
        scale = 'C'

    bpm = args['bpm']
    if bpm is None:
        print("Using default value of BPM.")
        bpm = 220
    bpm = int(bpm)
    if not (0 <= bpm <= 600):
        print("Wrong value. Using default value of BPM.")
        bpm = 220

    path = args['o']
    if path is None or not path.endswith(".mid"):
        print("Using default myfile.mid")
        path = "myfile.mid"


def main():
    parse()
    generator.generate_file(path, time, scale, bpm)

if __name__ == '__main__':
    main()

    if '--version' in sys.argv:
        print(musicgenerator.__version__)
