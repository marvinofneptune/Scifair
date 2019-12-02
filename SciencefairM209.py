
from m209.procedure import StdProcedure
from m209.keylist.config import read_key_list
import math
import time
from tqdm import tqdm
print('M-209: Science Fair 2019/2020 Aiden Lee')
targets=['IIPDU FHLAB NCLBG GLYDC IXXXX IIPDU FHLAB','IIPDU FHLAB LBXZU TOUEL XOSXX IIPDU FHLAB','IIPDU FHLAB XMTGW DISRX IIPDU FHLAB','IIPDU FHLAB AZBKB VSHSP VGPCX IIPDU FHLAB','IIPDU FHLAB XMDAL HEBFI VKAXX IIPDU FHLAB','IIPDU FHLAB AQNIY TTFXX IIPDU FHLAB','IIPDU FHLAB WWEKH ICYRD IIPDU FHLAB','IIPDU FHLAB OZLCY ZOJXX IIPDU FHLAB','IIPDU FHLAB XCSIA IIPDU FHLAB','IIPDU FHLAB OQOXY XUJTX IIPDU FHLAB']
times=[0,0,0,0,0,0,0,0,0,0]
sums=[0,0,0,0,0,0,0,0,0,0]
filepath = r'C:\Users\MacWin\Desktop\english-words-master\english-words-master\words_alpha.txt'
line =''
cnt = 1
trial=0
trialsToDo=5
key_list = read_key_list('m209keys.cfg', 'AB')
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
           proc = StdProcedure(key_list=key_list)
           ciphertext= proc.encrypt(line.upper().strip(), spaces=True, ext_msg_ind='PDUFHL', sys_ind='I')
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
