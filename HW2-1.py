stroka = input().split()
for i in stroka:
    if i.find('абв') !=1:
        stroka.remove(i)
print(stroka)