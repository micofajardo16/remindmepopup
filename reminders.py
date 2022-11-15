import time  
import tkinter as tk
from tkinter import ttk

global reminders 
reminders = False

class SetupWindow():
    def Submit(self):
        global oldtimeMew
        global oldtimePosture
        global oldtimeVision  
        global mewTime  
        global postureTime  
        global visionTime
        mewTime = self.mewEntry.get()
        mewTime = int(mewTime)
        postureTime = self.postureEntry.get()
        postureTime = int(postureTime)
        visionTime = self.visionEntry.get()
        visionTime = int(visionTime)
        oldtimeMew = time.time()
        oldtimePosture = time.time()
        oldtimeVision = time.time()  
        global reminders
        reminders = True
        self.root.destroy()

    def Exit(self):
        self.root.destroy()

    def __init__(self):
        self.root = tk.Tk()
        # self.root.eval('tk::PlaceWindow . center')
        self.root.geometry("500x150")
        # self.root.resizable(False, False)
        
        title = "Reminder Settings"
        self.root.title(title)
            
        self.root.columnconfigure(0, weight = 4)
        self.root.columnconfigure(1, weight = 1)

        self.mewLabel = ttk.Label(self.root, text="Set time interval for mew reminder (in s):")
        self.mewLabel.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

        self.mewEntry = ttk.Entry(self.root)
        self.mewEntry.insert(0, 300)
        self.mewEntry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)

        self.postureLabel = ttk.Label(self.root, text="Set time interval for posture reminder (in s):")
        self.postureLabel.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

        self.postureEntry = ttk.Entry(self.root)
        self.postureEntry.insert(0, 180)
        self.postureEntry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

        self.visionLabel = ttk.Label(self.root, text="Set time interval for vision reminder (in s):")
        self.visionLabel.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)

        self.visionEntry = ttk.Entry(self.root)
        self.visionEntry.insert(0, 1200)
        self.visionEntry.grid(column=1, row=2, sticky=tk.E, padx=5, pady=5)

        self.submit_button = tk.Button(
            self.root,
            text="Submit",
            command = self.Submit
        )
        self.submit_button.grid(column=1, row=3, sticky=tk.W, padx=5, pady=5)
        self.root.bind('<Return>', lambda e: self.Submit())

        self.exit_button = tk.Button(
            self.root,
            text="Exit",
            command = self.Exit
        )
        self.exit_button.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)

        self.root.mainloop()

class MewWindow():
    def Close(self):
        self.root.destroy()

    def Exit(self):
        global reminders
        reminders = False
        self.root.destroy()

    def __init__(self):
        self.root = tk.Tk()
        # self.root.eval('tk::PlaceWindow . center')
        self.root.geometry("220x50")
        self.root.resizable(False, False)

        title = "Mew Notification"
        self.root.title(title)

        self.frame_a = tk.Frame()
        self.frame_b = tk.Frame()

        self.label_a = tk.Label(
            master = self.frame_a, 
            text="Don't forget to mew"
        )
        self.label_a.pack()

        self.close_button = tk.Button(
            master = self.frame_b,
            text="Close",
            command = self.Close
        )
        self.close_button.pack(side = tk.LEFT)
        self.root.bind('<Return>', lambda e: self.Close())

        self.exit_button = tk.Button(
            master = self.frame_b,
            text="Exit",
            command = self.Exit
        )
        self.exit_button.pack(side = tk.LEFT)

        self.frame_a.pack()
        self.frame_b.pack()

        self.root.mainloop()

class PostureWindow():
    def Close(self):
        self.root.destroy()

    def Exit(self):
        global reminders
        reminders = False
        self.root.destroy()

    def __init__(self):
        self.root = tk.Tk()
        # self.root.eval('tk::PlaceWindow . center')
        self.root.geometry("250x50")
        self.root.resizable(False, False)

        title = "Posture Notification"
        self.root.title(title)

        self.frame_a = tk.Frame()
        self.frame_b = tk.Frame()

        self.label_a = tk.Label(
            master = self.frame_a, 
            text="Fix posture"
        )
        self.label_a.pack()

        self.close_button = tk.Button(
            master = self.frame_b,
            text="Close",
            command = self.Close
        )
        self.close_button.pack(side = tk.LEFT)
        self.root.bind('<Return>', lambda e: self.Close())

        self.exit_button = tk.Button(
            master = self.frame_b,
            text="Exit",
            command = self.Exit
        )
        self.exit_button.pack(side = tk.LEFT)

        self.frame_a.pack()
        self.frame_b.pack()

        self.root.mainloop()

class VisionWindow():
    def Close(self):
        self.root.destroy()

    def Exit(self):
        global reminders
        reminders = False
        self.root.destroy()

    def __init__(self):
        self.root = tk.Tk()
        # self.root.eval('tk::PlaceWindow . center')
        self.root.geometry("300x100")
        self.root.resizable(False, False)

        title = "Vision Notification"
        self.root.title(title)

        self.frame_a = tk.Frame()
        self.frame_b = tk.Frame()

        self.label_a = tk.Label(
            master = self.frame_a, 
            text="Every 20 minutes"
        )
        self.label_a.pack()

        self.label_b = tk.Label(
            master = self.frame_a, 
            text="Look at something 20 feet away"
        )
        self.label_b.pack()

        self.label_c = tk.Label(
            master = self.frame_a, 
            text="For 20 seconds"
        )
        self.label_c.pack()

        self.close_button = tk.Button(
            master = self.frame_b,
            text="Close",
            command = self.Close
        )
        self.close_button.pack(side = tk.LEFT)
        self.root.bind('<Return>', lambda e: self.Close())

        self.exit_button = tk.Button(
            master = self.frame_b,
            text="Exit",
            command = self.Exit
        )
        self.exit_button.pack(side = tk.LEFT)

        self.frame_a.pack()
        self.frame_b.pack()

        self.root.mainloop()


win = SetupWindow()
while(reminders):
    if time.time() - oldtimeMew > mewTime:
        win = MewWindow()
        oldtimeMew = time.time()

    if time.time() - oldtimePosture > postureTime:
        win = PostureWindow()
        oldtimePosture = time.time()

    if time.time() - oldtimeVision > visionTime:
        win = VisionWindow()
        oldtimeVision = time.time()