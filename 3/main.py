with open("input.txt","r") as f1:
    s = {int((i.split()[-1])):i.split()[:-1] for i in f1}
with open("output.txt","w", encoding='utf-8') as f2:
    f2.write("Имя самого младшего: "+s[sorted(s)[0]][0]+" "+s[sorted(s)[0]][1]+". Возраст: "+str(sorted(s)[0])+"\n")
    f2.write("Имя самого страшего: " + s[sorted(s)[-1]][0] + " " + s[sorted(s)[-1]][1] + ". Возраст: " + str(sorted(s)[-1]))
f1.close()
f2.close()
