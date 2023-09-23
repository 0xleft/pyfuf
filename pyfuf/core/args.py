class FuffCommandBuilder:
    def __init__(self, starting_dir="/", extra_args=[]):
        self.starting_dir = starting_dir
        self.extra_args = extra_args

    def add_arg(self, arg: str):
        self.extra_args.append(arg)

    def set_wordlist(self, wordlist: str):
        self.wordlist = wordlist

    def set_url(self, url: str):
        self.url = url

    def set_starting_dir(self, starting_dir: str):
        self.starting_dir = starting_dir

    def set_extra_args(self, extra_args: list):
        self.extra_args = extra_args

    def build(self) -> list:
        if not hasattr(self, "url") or not hasattr(self, "wordlist"):
            raise Exception("URL or wordlist not set.")
        
        args = ["-w", self.wordlist, "-u", f"{self.url}{self.starting_dir}"] + self.extra_args
        
        # make better
        contains = False
        for arg in args:
            if "FUZZ" in arg:
                contains = True
                break

        if not contains:
            raise Exception("FUZZ not found in args.")
        
        return args