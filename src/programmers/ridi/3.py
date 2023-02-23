# -*- coding: utf-8 -*-


def solution(movie):
    cnt = {}
    for m in movie:
        if m not in cnt:
            cnt[m] = 1
        else:
            cnt[m] += 1
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
