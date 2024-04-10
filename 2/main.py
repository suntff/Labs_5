with open('input.txt') as f1:
    num = [int(i) for i in f1]
num.sort()
with open('output.txt','w') as f2:
    for i in range(len(num)):
        f2.write(str(num[i])+"\n")
f1.close()
f2.close()
