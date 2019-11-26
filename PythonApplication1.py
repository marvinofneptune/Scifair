import math
targets=['brumalia']
filepath = r'C:\Users\MacWin\Desktop\english-words-master\english-words-master\words_alpha.txt'
cracked=0
line =''
cnt = 1
def cipher(x):
    return x
with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   while line:
       per=math.floor((cnt/370103)*100000)/1000
       print("Testing line {} of 370103 ({}%): {}".format(cnt,per, line.strip()))
       for i in targets:
            if cipher(line.strip()) == "brumalia":
             cracked=cnt
             print('found')
             break
       line=fp.readline()
       cnt += 1
print("found on line:{}".format(cracked))