import pyfuf

# callback function when a line from fuff is parsed
def callback(line):
    # if the line is a finding, parse it
    if pyfuf.get_line_type(line) == pyfuf.LineType.FINDING:
        finding = pyfuf.parse_finding_line(line)
        # print the parsed finding object
        print(finding)

# arguments for fuff
args = pyfuf.FuffCommandBuilder()
args.set_target("http://localhost/FUZZ.php")
args.set_wordlist("wordlist.txt")
args.set_method("GET")
args.set_user_agent("PyFuf")
args.follow_redirects()
args.ignore_wordlist_comments()

# start fuzzing
pyfuf.fuzz(args, callback)