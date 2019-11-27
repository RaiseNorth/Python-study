字符串=filter(str.isalpha,input().upper())
字典 = {}
for 字符 in 字符串:
    if 字符 not in 字典:字典[字符] = 1
    else:字典[字符] += 1
个数=list (字典.values())
个数.sort(reverse=True)
print (个数[0])