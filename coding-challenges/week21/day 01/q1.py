def longestCommonPrefix(my_str):
    if my_str == []:
        return ''
    if len(my_str) == 1:
        return my_str[0]
    my_str.sort()
    shortest = my_str[0]
    prefix = ''
    for i in range(len(shortest)):
        if my_str[len(my_str) - 1][i] == shortest[i]:
            prefix += my_str[len(my_str) - 1][i]
        else:
            break
    return prefix

my_list_1 = ['flower', 'flow', 'flight']
my_list_2 = ['dog', 'racecar', 'car']

print(longestCommonPrefix(my_list_1))

print(longestCommonPrefix(my_list_2))