def file_lengthy(fname):
    with open(fname) as f:
        for i in enumerate(f):
            pass
    return i+1
print('So dong:',file_lengthy('cau7.txt'))