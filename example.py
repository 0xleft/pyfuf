import pyfuf

# callback function when a line from fuff is parsed
def callback(line):
    # if the line is a finding, parse it
    if pyfuf.get_line_type(line) == pyfuf.LineType.FINDING:
        finding = pyfuf.parse_finding_line(line)
        # print the parsed finding object
        print(finding)

# arguments for fuff
args = pyfuf.FuffCommandBuilder(starting_dir="/FUZZ.php")
args.set_url("http://localhost")
args.set_wordlist("wordlist.txt")

# start fuzzing
pyfuf.fuzz(args, callback)