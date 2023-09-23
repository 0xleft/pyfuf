from .core.args import FuffCommandBuilder
import subprocess
from . import binary_path

def fuzz(command_builder: FuffCommandBuilder, callback) -> None:
    process = subprocess.Popen([binary_path] + command_builder.build(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    while True:
        try:
            output = process.stdout.readline()
            if process.poll() is not None:
                break
            if output:
                callback(output.decode("utf-8").strip())
        except KeyboardInterrupt:
            process.kill()
            print("Fuzzing stopped.")
            break
    rc = process.poll()
    return rc