color=['Red','Green','White','Black','Pink','Yellow']
with open('cau8',"w")as myfile:
    for c in color:
        myfile.write("%s\n"%c)
content=open('cau8.txt')
print(content.read())