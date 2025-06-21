def ith_row(string, n, x, ith_row_chars, ith_row_indices):
    if len(ith_row_chars) == x:
        print(str(ith_row_chars))
    else:
        for i in range(n):
            if i  > ith_row_indices[-1]:
                ith_row_chars.append(string[i])
                ith_row_indices.append(i)
                ith_row(string, n, x, ith_row_chars, ith_row_indices)
                ith_row_chars.pop()
                ith_row_indices.pop()


def nCx(string, x):
    '''Permutes the characters in the string variable at "x" positions'''
    str_len = len(string)
    
    if x<1 or x>str_len:
        return 'X value out of range!'
    
    if str_len == 0:
        return 'No characters to permute!'
    
    for i in range(str_len):
        ith_row(string, str_len, x, [string[i]], [i])
    
nCx('abcd', 2)
