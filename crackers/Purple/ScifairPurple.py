from purple.machine import Purple97

purple = Purple97.from_key_sheet(
       switches='9-1,24,6-23',
       alphabet='NOKTYUXEQLHBRMPDICJASVWGZF')

import math
import time
from tqdm import tqdm
print('PURPLE: Science Fair 2019/2020 Aiden Lee')
targets=['CTYUHLXACTV','BRPVVSVQRRJRB','DQSHJVKENQ','LPIPZXZDYSULTN','DQRYORFXXPUFX','LHZDDSMW','OUGPWBOANH','HPYRDZVP','DTODU','HHCBDTSPP']
times=[0,0,0,0,0,0,0,0,0,0]
sums=[0,0,0,0,0,0,0,0,0,0]
filepath = r'C:\Users\MacWin\Desktop\english-words-master\english-words-master\words_alpha.txt'
line =''
cnt = 1
trial=0
trialsToDo=5

print('Scheduled for {} trials'.format(trialsToDo))
for g in range(trialsToDo):
    print('\nTrial {} started'.format(g+1))
    fbidn=tqdm(total=370103,leave=True)
    with open(filepath) as fp:
        startTime=time.time()
        line=''
        line = fp.readline()
        cnt = 1
        while line:
           purple = Purple97([8, 0, 23, 5], fast_switch=2, middle_switch=3,alphabet='NOKTYUXEQLHBRMPDICJASVWGZF')
           ciphertext=purple.encrypt(line.strip().upper())
           #print("Testing line {} of 370103 ({}%): {} to {}".format(cnt,per,line.strip(),ciphertext)) 
           fbidn.update(1)  
           line=fp.readline()
           cnt += 1
           
           tmp=0
           for i in targets:
               if i == ciphertext:
                   times[tmp]=time.time()-startTime
                   sums[tmp]+=time.time()-startTime
               tmp+=1
    fbidn.close()
    print('Time taken: {} seconds'.format(time.time()-startTime))
    print('times:{}'.format(times))
print('avar times')
for i in sums:
    print(i/trialsToDo)
