def list_(arg):
    res = [0]*len(arg)
    for i in range(len(arg)):
        res[i] = arg[i]
    return res

def str_(s):
    res = ""
    for item in s:
        res += item
    return res


def sort_(s):
    res = []
    s_dup = list_(s)
    for i in range(len(s_dup)-1):
        small = i
        for j in range(i+1, len(s_dup)):
            if s_dup[j]  < s_dup[small]:
                small = j
        s_dup[i], s_dup[small] = s_dup[small], s_dup[i]
    return str_(s_dup)

def is_anagram(s1, s2):
    """This function returns boolean value indicating the two input strings are anagram or not without using inbuilt methods."""
    s1_l = len(s1)
    s2_l = len(s2)

    if s1_l != s2_l:
        return False
    
    s1 = sort_(s1)
    s2 = sort_(s2)
   
    return s1 == s2

s1 = "abc"
s2 = "abc"

print(is_anagram(s1, s2))
