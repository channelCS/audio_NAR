"""
Created on Sun Jan 14 15:31:02 2018

@author: Aditya Arora
"""
import glob
import config as cfg

cfg.CreateFolder(cfg.audio_folder)
cfg.CreateFolder(cfg.kitchen_folder)
cfg.CreateFolder(cfg.nonverbal_folder)
cfg.CreateFolder(cfg.office_folder)
cfg.CreateFolder(cfg.speech_folder)

for f in glob.glob(cfg.orig_dataset_path):
    g=f.split('\\')[-1]
    if g in cfg.kitchen_array:
        cfg.MoveFolder(f, cfg.kitchen_folder+'/'+g)
    elif g in cfg.nonverbal_array:
        cfg.MoveFolder(f, cfg.nonverbal_folder+'/'+g)
    elif g in cfg.office_array:
        cfg.MoveFolder(f, cfg.office_folder+'/'+g)
    elif g in cfg.speech_array:
        cfg.MoveFolder(f, cfg.speech_folder+'/'+g)
    
