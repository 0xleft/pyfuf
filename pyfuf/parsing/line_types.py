from enum import Enum
from .utils import fix_line

class LineType(Enum):
    PROGRESS = 1
    FINDING = 2
    ERROR = 3
    COMMENT = 4
    UNKNOWN = 5

def get_line_type(line: str):
        line = fix_line(line)
        if line.startswith("::Progress:"):
            return LineType.PROGRESS
        if line.startswith("#"):
            return LineType.COMMENT
        if not line.startswith("#") and "[Status:" in line:
            return LineType.FINDING
        return LineType.UNKNOWN