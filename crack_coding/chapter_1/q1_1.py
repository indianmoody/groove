
def way1(s):

    s = sorted(s)

    for i, c in enumerate(s[:-1]):
        if c == s[i+1]:
            return False # not unique

    return True # unique



def way2(s):

    if len(s) == 1:
        return True

    for i in range(0,len(s)-1):
        for j in range(i+1,len(s)):
            if s[i] == s[j]:
                return False

    if s[-2] == s[-1]: # above loop doesn't check equality of last two characters in string.
        return False

    return True # unique



def way3(s):

    ans = True if len(s) == len(set(s)) else False

    return ans


st = input("enter a string to check if it has all unique characters: ")
print("way1 answer: {}".format(way1(st)))
print("way2 answer: {}".format(way2(st)))
print("way3 answer: {}".format(way3(st)))

aa = way3(st)
print(aa)