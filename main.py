
#Libraries used 
import time
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import vlc

#ID number example
ID_number = 584192445780

# Defining the name reader as a MFRC522 sensor
reader = SimpleMFRC522()

# defining the name mediaplayer as a medialistplayer object
media_player = vlc.MediaListPlayer()

# creating Instance class object
player = vlc.Instance()
media_player.get_media_player().audio_set_volume(80)

# creating a media list object for each Playlist
First_Playlist = vlc.MediaList()

# Importing songs from the directories
First_Folder = player.media_new("Directory")

#Ading those folders to their respective playlist
First_Playlist.add_media(First_Folder)

# Scanning the RFID IDs 
while True:
    try:
        id, text = reader.read()
        print(id)
        print(text)
        

    finally:
        GPIO.cleanup()
        time.sleep(2) 
        
# If statements to activate a certain playlist depending on the RFID tag 
# Repeat for each playlist or individual song 
    if id == ID_number:
        print("First_Playlist will play")
        media_player.set_media_list(First_Playlist)
        media_player.play()

# Features like: Next song, Pause and Resume, Stop, Mute and unmute, volume + , volume - 
# Next song   
    if id == different_ID:
        media_player.next()

# Pause and Resume    
    if id == different_ID:
        media_player.pause()
        
# Stop
    if id == different_ID:
        media_player.stop()
        
# Mute and unmute
    if id == different_ID:
        media_player.get_media_player().audio_toggle_mute()
    
# volume +    
    if id == different_ID:
        volume = media_player.get_media_player().audio_get_volume()
        volume = volume + 5
        media_player.get_media_player().audio_set_volume(volume)
    
# volume -     
    if id == different_ID:
        volume = media_player.get_media_player().audio_get_volume()
        volume = volume - 5
        media_player.get_media_player().audio_set_volume(volume)