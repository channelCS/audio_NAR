"""
Created on Sun Jan 14 15:31:02 2018

@author: channelCS
"""
import glob
import config as cfg
import os
from string import digits
import sys

if sys.platform[:3]=='win':
    splitr='\\'
else:
    splitr='/'

def move_files():
    x=os.listdir(path)
    print 'The folder has {} subfolders'.format(len(x))
    for folder in x:
        new_path=path+'/'+folder
        if os.path.isdir(new_path):
            y=os.listdir(new_path)
            if y == []:
                print 'Empty subfolder:',folder
            else:
                for file_ in y:
                    os.rename(new_path+'/'+file_,path+'/'+folder+'_'+file_)
                    if not os.listdir(new_path):
                        os.rmdir(new_path)

path=cfg.audio_folder


cfg.CreateFolder(cfg.audio_folder)
cfg.CreateFolder(cfg.kitchen_folder)
cfg.CreateFolder(cfg.nonverbal_folder)
cfg.CreateFolder(cfg.office_folder)
cfg.CreateFolder(cfg.speech_folder)

for f in glob.glob(cfg.orig_dataset_path):
    g=f.split(splitr)[-1]
    if g in cfg.kitchen_array:
        cfg.MoveFolder(f, cfg.kitchen_folder+'/'+g)
    elif g in cfg.nonverbal_array:
        cfg.MoveFolder(f, cfg.nonverbal_folder+'/'+g)
    elif g in cfg.office_array:
        cfg.MoveFolder(f, cfg.office_folder+'/'+g)
    elif g in cfg.speech_array:
        cfg.MoveFolder(f, cfg.speech_folder+'/'+g)
    


move_files()
move_files()

#Delete DS_Store files
for f in glob.glob(path+'/*'):
    x=f.split(splitr)[-1]
    if x[-4:]!='.wav':
        os.remove(path+'/'+x)
        
        
#Generating the meta file

str1=''
arr1=[]
for f in glob.glob(path+'/*'):
    x=f.split(splitr)[1]
    res = x.translate(None, digits).split('.')[0].split('_')[0]
    arr1.append(res)
    str1+='audio/'+x+'\t'+res+'\n'

file1 = open("meta.txt","w") 
 
file1.write(str1) 
 
file1.close() 
