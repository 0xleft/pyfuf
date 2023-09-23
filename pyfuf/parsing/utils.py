def fix_line(line: str):
    line = line.replace(" ", "")[4:-4]
    line = line.replace("\n", "").replace("\r", "").replace("\t", "")
    return line