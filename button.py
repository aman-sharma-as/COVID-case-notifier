import tkinter as tk

class DemoApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(Windows1)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class Windows1(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Button(self, text="Next",
                  command=lambda: master.switch_frame(Windows2)).pack()

class Windows2(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Button(self, text="Back",
                  command=lambda: master.switch_frame(Windows1)).pack()

if __name__ == "__main__":
    app = DemoApp()
    app.mainloop()
