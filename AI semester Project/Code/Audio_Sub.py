import datetime
import time
import speech_recognition as sr
from os import path
#Inserting Audio File
AUDIO_FILE = path.join("english.wav")
#Setting recognizer
r = sr.Recognizer()
#Start Time for termination purpose
start_time = datetime.datetime(100,1,1,0,1,0)
#End Time for termination purpose
max_time = datetime.datetime(100,1,1,0,2,0)
#Blocks in SRT File starts from 0
block_num = 0
#Function Definition
def audio_to_srt(current_time, block):
    global sentence
    #Termnation Condition
    if current_time >= max_time:
        print("Subtitles generation is end.")
        return
    else:
        block += 1
        block_str = str(block)
        #Audio File Recording
        with sr.AudioFile(AUDIO_FILE) as source:
            print("Recording your audio file.")
            audio = r.record(source)
            #Adding some delay just for fun
            time.sleep(10)
        try:
            #Converting to text using Google
            print("Now converting recording into text.")
            sentence = (r.recognize_google(audio))
        #In case of errors like internet disconnecction or microphone error
        except sr.UnknownValueError:
            print("Sorry could not understand the audio")

        except sr.RequestError as e:
            print("Sorry could not request result internet issue; {0}".format(e))
        #Writing text to SRT File
        if sentence != "":
            #Counting Number of words in he text
            time_add = (len(sentence.split()))
            end_time = current_time + datetime.timedelta(0, time_add)


            str_current_time = str(current_time.time())
            str_end_time = str(end_time.time())


            #Writing on File
            with open(r"C:\Users\Adeel Khan\PycharmProjects\Subtitle_Generation_AI\subtitles.srt", "a") as f:
                f.write(block_str)
                f.write("\n")
                f.write(str_current_time)
                f.write("-->")
                f.write(str_end_time)
                f.write("\n")
                f.write(sentence)
                f.write(".")
                f.write("\n")
                f.write("\n")
                print("Subtitles generation is end.")
            return
#Function Calling
audio_to_srt(start_time, block_num)

