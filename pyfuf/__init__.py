import os
import sys

binary_path = os.path.join(__path__[0], "fuff.exe" if sys.platform == "win32" else "fuff")

from .fuzzing import *
from .parsing import *
from .core import *