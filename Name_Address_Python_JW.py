# Name and address program pp.713 Wiegman
import tkinter

class MyGUI:
    def __init__(self):
        # Creating the main window.
        self.main_window = tkinter.Tk()

        # Create StringVar to display name,
        # street, and city-state zip (csz).
        self.name_value = tkinter.StringVar()
        self.street_value = tkinter.StringVar()
        self.csz_value = tkinter.StringVar()

        # Create two frames.
        self.info_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        # Creating the label widgets for the
        # stringvar objects
        self.name_label = tkinter.Label(self.info_frame, \
        textvariable=self.name_value)
        self.street_label = tkinter.Label(self.info_frame, \
                                          textvariable=self.street_value)
        self.csz_label = tkinter.Label(self.info_frame, \
                                        textvariable=self.csz_value)
        # Must now pack the labels to default position stacked
        self.name_label.pack()
        self.street_label.pack()
        self.csz_label.pack()

        # Creating button widgets for GUI
        self.show_info_button = tkinter.Button(self.button_frame, \
                                          text='Show Info', \
                                          command=self.show)
        self.quit_button = tkinter.Button (self.button_frame, \
                                          text='Quit', \
                                          command=self.main_window.destroy)
        
        # Packing buttons
        self.show_info_button.pack(side='left')
        self.quit_button.pack(side='right')

        # Packing frames
        self.info_frame.pack()
        self.button_frame.pack()

        # Put tkinter in to start the main loop
        tkinter.mainloop()
# Must specify callback function for the button of Show Info
    def show(self):
        self.name_value.set('Matt Hoyle')
        self.street_value.set('123 Walnut Street')
        self.csz_value.set('Ashevile, NC 299999')

# Creating instance for MyGUI class
my_gui = MyGUI() 