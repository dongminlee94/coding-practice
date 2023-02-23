# -*- coding: utf-8 -*-

import re


def getFinalString(s: str) -> str:
    while True:
        s = re.sub("AWS", "", s)
        if s == "":
            return "-1"
        elif not "AWS" in s:
            return s


assert getFinalString("AAWSWS") == -1
assert getFinalString("AWAWSSG") == "G"
