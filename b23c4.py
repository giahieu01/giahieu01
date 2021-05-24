s = input("Nhập câu của bạn: ")
d={"DIGITS":0, "LETTERS":0}
for c in s:
 if c.isdigit():
    d["DIGITS"]+=1
 elif c.isalpha():
        d["LETTERS"]+=1
 else:
     pass
print ("Số chữ cái là:", d["LETTERS"])
print ("Số chữ số là:", d["DIGITS"])