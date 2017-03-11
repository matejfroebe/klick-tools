
import subprocess
import tempfile
import argparse



parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('startBPM', type=int, nargs='+',
                    help='starting BPM')
parser.add_argument('stopBPM', type=int, nargs='+',
                    help='stop BPM')
parser.add_argument('stepBPM', type=int, nargs='+',
                    help='step BPM')
parser.add_argument('meas', type=int, nargs='+',
                    help='number of measures of the same tempo')


args = parser.parse_args()
print(args)


startBPM = args.startBPM[0]
stepBPM = args.stepBPM[0]
stopBPM = args.stopBPM[0]
meas = args.meas[0]

lines = ["{} 8/8 {} Xxxxxxxx\n".format(meas, t) for t in range(startBPM, stopBPM+1, stepBPM)]
print lines

with tempfile.NamedTemporaryFile() as f:
    f.writelines(lines)
    f.flush()
    subprocess.call(["klick", "-P", "-f", f.name])

