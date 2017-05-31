
import argparse
import random

import klick


parser = argparse.ArgumentParser(description='generate random rhythm made of nSeq sequences of 1 to sMax notes')
parser.add_argument('BPM', type=int, nargs='+',
                    help='BPM')
parser.add_argument('nSeq', type=int, nargs='+',
                    help='number of sequences')
parser.add_argument('sMax', type=int, nargs='+',
                    help='maximum number of notes in a sequence')


args = parser.parse_args()

BPM = args.BPM[0]
nSeq = args.nSeq[0]
sMax = args.sMax[0]


rhythm = ".".join(["x"*random.randint(1,sMax) for _ in range(nSeq)])
length = len(rhythm)
lines = ["1 {}/16 {} {}\n".format(length, BPM, rhythm)]
#print lines

nextAction = "r"
while nextAction != "q":
    if nextAction == "r":
        klick.runKlick(lines)
    elif nextAction == "s":
        print rhythm
    nextAction = raw_input("(r)epeat, (s)how or (q)uit:")

print rhythm
