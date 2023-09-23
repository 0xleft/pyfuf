# A simple wrapper for fuff fuzzer in python

## Install!

```bash
pip install pyfuf
```

or 

```bash
git clone git@github.com:0xleft/pyfuf.git
cd pyfuf
pip install .
```

## Usage

There is a good example in `example.py` file.

```python
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
```

# TODO

- Add tests
- Add docs
- Make codebase cleaner