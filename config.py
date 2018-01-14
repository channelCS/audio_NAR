
import os
from shutil import copytree

def CreateFolder( fd ):
    if not os.path.exists(fd):
        os.makedirs(fd)

def MoveFolder(source,destination):
    try:
        copytree(source,destination)
    except:
        print("Oops! Folder already exists...")
        return

# We define where does all the audio files reside
dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path=dir_path.replace('\\', '/')
orig_dataset_path=dir_path+'/NAR_dataset/*'

kitchen_array=['alarmfridge', 'alarmmicrowave', 'chair', 'closemicrowave', 'cuttlery', 'drawer', 'eat', 'openmicrowave', 'strugling', 'tap', 'toaster', 'water']
nonverbal_array=['fingerclap', 'handclap', 'tongue']
office_array=['doorclose', 'doorkey', 'doorknock', 'dooropen', 'paper', 'zipone', 'ziptwo']
speech_array=['eight', 'five', 'four', 'hello', 'left', 'move', 'nao', 'nine', 'no', 'one', 'right', 'seven', 'six', 'stop', 'ten', 'three', 'turn', 'two', 'what', 'yes']
audio_folder='audios'
kitchen_folder   = audio_folder + '/Kitchen'
nonverbal_folder = audio_folder + '/Nonverbal'
office_folder    = audio_folder + '/Office'
speech_folder    = audio_folder + '/Speech'



wav_fd = 'trim'
# These are the folders where various features will be extracted
fe_cqt_fd              = 'Fe/cqt'
fe_logmel_kong_fd      = 'Fe/logmel_kong'
fe_logmel_libd_fd      = 'Fe/logmel_lib_delta'
fe_mel_fd              = 'Fe/mel'

