

import subprocess
import tempfile


def runKlick(tempoMap):
    with tempfile.NamedTemporaryFile() as f:
        f.writelines(tempoMap)
        f.flush()
        subprocess.call(["klick", "-P", "-f", f.name])
