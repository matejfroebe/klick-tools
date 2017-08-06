
import argparse

import klick


parser = argparse.ArgumentParser(description='Run klick with a template file for tempo map.')
parser.add_argument('BPM', type=int, nargs='+', help='tempo (BPM)')
parser.add_argument('-f', '--filename', help='filename')


args = parser.parse_args()
BPM = args.BPM[0]

with open(args.filename) as f:
    linesIn = f.readlines()

linesOut = [line.replace("$T", str(BPM)) for line in linesIn]

print linesOut


klick.runKlick(linesOut)
