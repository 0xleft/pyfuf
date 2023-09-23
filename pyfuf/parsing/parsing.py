from .line_types import get_line_type, LineType
from .utils import fix_line

# force parsing of fuff output
# includes[Status:301,Size:309,Words:20,Lines:10,Duration:9ms]

def parse_finding_line(line: str) -> object:
    line = fix_line(line)

    finding = line.split("[Status:")[0]
    status = line.split("[Status:")[1].split(",")[0]
    size = line.split("Size:")[1].split(",")[0]
    words = line.split("Words:")[1].split(",")[0]
    lines = line.split("Lines:")[1].split(",")[0]
    duration = line.split("Duration:")[1].split("]")[0]

    return {
        "finding": finding,
        "status": status,
        "size": size,
        "words": words,
        "lines": lines,
        "duration": duration
    }