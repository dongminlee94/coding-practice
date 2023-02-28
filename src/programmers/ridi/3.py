# -*- coding: utf-8 -*-

import collections


def solution(movie):
    cnt = collections.Counter(movie)
    return sorted(cnt.keys(), key=lambda m: (-cnt[m], m))


assert solution(movie=["spy", "ray", "spy", "room", "once", "ray", "spy", "once"]) == [
    "spy",
    "once",
    "ray",
    "room",
]
assert solution(movie=["spy", "ray", "spy", "room", "once", "ray", "spy", "once", "once", "room"]) == [
    "once",
    "spy",
    "ray",
    "room",
]
