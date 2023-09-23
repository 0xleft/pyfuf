class FuffCommandBuilder:
    def __init__(self):
        self.extra_args = []

    def set_wordlist(self, wordlist: str):
        self.wordlist = wordlist

    def set_target(self, url: str):
        self.url = url

    def set_user_agent(self, user_agent: str):
        self.extra_args += ["-H", f"User-Agent:{user_agent}"]

    def set_data(self, data: str):
        self.extra_args += ["-d", data]

    def stop_all(self):
        self.extra_args += ["-sa"]

    def stop_on_403(self):
        self.extra_args += ["-sf"]

    def stop_on_errors(self):
        self.extra_args += ["-se"]

    def follow_redirects(self):
        self.extra_args += ["-r"]

    def http2(self):
        self.extra_args += ["-http2"]

    def ignore_wordlist_comments(self):
        self.extra_args += ["-ic"]

    def maxtime_process(self, seconds: int):
        self.extra_args += ["-maxtime", str(seconds)]

    def maxtime_job(self, seconds: int):
        self.extra_args += ["-maxtime-job", str(seconds)]

    def rate_limit(self, rps: int):
        self.extra_args += ["-rate", str(rps)]

    def threads(self, threads: int):
        self.extra_args += ["-t", str(threads)]

    def set_post_data(self, data: str):
        self.extra_args += ["-d", data]

    def set_method(self, method: str):
        self.extra_args += ["-X", method]

    def set_mode(self, mode: str):
        # Available modes: clusterbomb, pitchfork, sniper
        if mode not in ["clusterbomb", "pitchfork", "sniper"]:
            raise Exception("Invalid mode.")
        self.extra_args += ["-mode", mode]

    def set_header(self, header: str, value: str):
        self.extra_args += ["-H", f"{header}:{value}"]

    def set_cookie(self, cookie: str):
        self.extra_args += ["-b", cookie]

    def build(self) -> list:
        if not hasattr(self, "url") or not hasattr(self, "wordlist"):
            raise Exception("URL or wordlist not set.")
        
        args = ["-w", self.wordlist, "-u", f"{self.url}"] + self.extra_args
        
        # make better
        contains = False
        for arg in args:
            if "FUZZ" in arg:
                contains = True
                break

        if not contains:
            raise Exception("FUZZ not found in args.")
        
        return args