f = open(r'D:\Python Course\02-Python Practice\W3resource\19-File IO\my_text.txt','r')

input = f.read()
count = 0
#print(input)
# for i in input:
#     if count > 30:
#         count = 0
#         print(i)
#     else:
#         print(i)
#         count += 1

## transfering each para in each file 
para = [ i for i in input.split('\n\n') if i.strip()]
print(len(para))
for i in range(len(para)):
    str = f'19-File IO/output{i}.txt'
    with open(str,"w") as r:
        r.write(para[i])
        print("Done")
    r.close()
f.close()