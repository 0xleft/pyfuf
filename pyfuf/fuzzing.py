from .core.args import FuffCommandBuilder
import subprocess
from . import binary_path

def fuzz(command_builder: FuffCommandBuilder, callback, end_callback=None, error_callback=None) -> None:
    process = subprocess.Popen([binary_path] + command_builder.build(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    while True:
        try:
            output = process.stdout.readline()
            if process.poll() is not None:
                break
            if output:
                callback(output.decode("utf-8").strip())
        except KeyboardInterrupt:
            if end_callback:
                end_callback()
            process.kill()
            print("Fuzzing stopped.")
            break
    rc = process.poll()
    if rc != 0:
        if error_callback:
            error_callback()
        raise Exception("Fuzzing failed.")
    return rc