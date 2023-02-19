# -*- coding: utf-8 -*-

import collections


def findRange(num: int) -> int:
    cnt_dict = collections.Counter(list(str(num)))

    # maximum
    ma, temp = num, str(num)
    for cnt in cnt_dict:
        new_num = temp.replace(cnt, "9")
        if len(str(num)) != len(new_num):
            continue
        if int(new_num) > int(ma):
            ma = new_num

    # minimum
    mi, temp = num, str(num)
    for cnt in cnt_dict:
        new_num = temp.replace(cnt, "0")
        if new_num[0] == "0":
            continue
        if int(new_num) < int(mi):
            mi = new_num

    # final
    if str(mi)[0] != 1:
        new_num = temp.replace(temp[0], "1")
        if int(new_num) < int(mi):
            mi = new_num
    return int(ma) - int(mi)


print(findRange(111))
print(findRange(10018))
