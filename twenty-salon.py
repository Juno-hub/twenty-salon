from tkinter import *

def set_screen():
    # Set screen icon
    iconphoto = PhotoImage(file = 'twenty-salon\스무살롱.png').subsample(2,2)
    root.wm_iconphoto(False, iconphoto)

    # Set screen title
    root.title("스무살롱")

    # Get screen dimensions
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Setting screen size
    app_width = 680
    app_height = 480

    # Calculate window position
    x = (screen_width - app_width) // 2
    y = (screen_height - app_height) // 2

    # Set screen geometry
    root.geometry(f"{app_width}x{app_height}+{x}+{y}")

# Create root window
root = Tk()

# Configure screen setting
set_screen()

root.mainloop()