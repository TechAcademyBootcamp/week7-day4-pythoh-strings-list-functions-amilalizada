def writemid(a,s):
    return a[:int(len(a)/2)]+s+a[-int(len(a)/2):]
print(writemid('{{}}','PHP'))
print(writemid('[[]]','PYTHON'))
