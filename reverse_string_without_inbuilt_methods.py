def reverse_the_string(string: str)->str:
    '''This method reverses the string without using inbuilt funcitons and return the reversed string'''
    i=len(string)-1
    new_string = ''
    while(i >= 0):
        new_string += string[i]
        i-=1
    return new_string

#check
string = 'india'
output = reverse_the_string(string)
print(output) #aidni
