from .binary import install_fuff, check_fuff_installed
from .binary import *
from .args import *

if not check_fuff_installed():
    install_fuff()