
import socket
import platform
 
PC_OS = platform.system()
PC_ID = socket.gethostname()

if PC_OS == 'Windows' and PC_ID == 'DESKTOP-G8P77K5':

    path_soundfile = 'C:\\Users\\manip\\Desktop\\RespiDriver_sound_pictures_bank\\son'
    path_images = 'C:\\Users\\manip\\Desktop\\RespiDriver_sound_pictures_bank\\images'

else:

    path_soundfile = '/home/jules/smb4k/CRNLDATA/crnldata/cmo/multisite/DATA_MANIP/EEG_Lyon_VJ/protocole/sound_pictures_bank/son'
    path_images = '/home/jules/smb4k/CRNLDATA/crnldata/cmo/multisite/DATA_MANIP/EEG_Lyon_VJ/protocole/sound_pictures_bank/images'

