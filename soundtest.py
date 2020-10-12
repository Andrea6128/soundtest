import tkinter
from tkinter import Label
import simpleaudio as sa


# setup
tk = tkinter.Tk(className=" PFUK Multimedia Room Sound Test")
tk.geometry("400x200")
label = Label(tk, text="Simple Sound Test", font=("Calibri", 30))
author = Label(tk, text="© 2020 Aja")

# define callbacks
def leftChannelCallback():
    filename = "assets/left.wav"
    wave_obj = sa.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()

def bothChannelCallback():
    filename = "assets/chord.wav"
    wave_obj = sa.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()

def rightChannelCallback():
    filename = "assets/right.wav"
    wave_obj = sa.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()

def rangeChannelCallback():
    filename = "assets/range.wav"
    wave_obj = sa.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()

def stopCallback():
    filename = "assets/range.wav"
    # play_obj = sa.WaveObject.from_wave_file(filename)
    play_obj = sa.play_buffer(0b0, 2, 2, 44100)
    play_obj.stop()


# show text
label.pack()
author.place(x=330, y=180)

# configure buttons
button1 = tkinter.Button(tk, text ="Left Channel", command = leftChannelCallback)
button2 = tkinter.Button(tk, text ="chord.wav", command = bothChannelCallback)
button3 = tkinter.Button(tk, text ="Right Channel", command = rightChannelCallback)
button4 = tkinter.Button(tk, text ="Range 44Hz - 20kHz", command = rangeChannelCallback)
button5 = tkinter.Button(tk, text ="Stop", command = stopCallback)

# show buttons
button1.place(x=30, y=60, height=50, width=100)
button2.place(x=150, y=60, height=50, width=100)
button3.place(x=270, y=60, height=50, width=100)
button4.place(x=140, y=130, height=50, width=120)
button5.place(x=10, y=130, height=30, width=80)


if __name__ == "__main__":
    tk.mainloop()