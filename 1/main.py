with open("input.txt") as file1:
    num = [int(i) for i in file1.readline().split()]
pr = 1
for i in range(len(num)):
    pr*=num[i]
with open("outut.txt",'w') as file2:
    file2.write(str(pr))
file1.close()
file2.close()
