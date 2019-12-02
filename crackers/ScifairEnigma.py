
import math
from enigma.machine import EnigmaMachine
import time
from tqdm import tqdm

targets=['DEDGEGNVLPO','AWXWSFUDNSWXI','YOADZZMTEE','GMBOHTJHYLJNZX','YOKEQLYWRDJVJ','GGQNBFQY','NDEOFJIVEB','KMDRBDUZ','YEONV','KGWMBXTZX']
times=[]
filepath = r'C:\Users\MacWin\Desktop\english-words-master\english-words-master\words_alpha.txt'
line =''
cnt = 1
trial=0

machine = EnigmaMachine.from_key_sheet(
       rotors='II IV V',
       reflector='B',
       ring_settings=[1, 20, 11],
       plugboard_settings='AV BS CG DL FU HZ IN KM OW RX')
machine.set_display('WXC')
msg_key = machine.process_text('KCH')
machine.set_display(msg_key)
print('Enigma Machine: Science Fair 2019/2020 Aiden Lee')
for g in range(10):
    print('\nTrial {} started'.format(g+1))
    fbidn=tqdm(total=370103,leave=True)
    with open(filepath) as fp:
        startTime=time.time()
        times.insert(trial,[])
        line=''
        line = fp.readline()
        cnt = 1
        while line:
           ciphertext=machine.process_text(line.strip())
           #print("Testing line {} of 370103 ({}%): {} to {}".format(cnt,per,line.strip(),ciphertext)) 
           fbidn.update(1)  
           line=fp.readline()
           cnt += 1
           machine.set_display('WXC')
           msg_key = machine.process_text('KCH')
           machine.set_display(msg_key)
           tmp=0
           for i in targets:
               if i == ciphertext:
                   times[trial].insert(tmp,time.time()-startTime)
               tmp+=1
    fbidn.close()
    print('Time taken: {} seconds'.format(time.time()-startTime))
