import tkinter as tk
from PIL import Image, ImageTk

def resize_image(event):
    global original_image, background_image, image_item
    new_width = event.width
    new_height = event.height
    resized_image = original_image.resize((new_width, new_height))
    background_image = ImageTk.PhotoImage(resized_image)
    canvas.itemconfig(image_item, image=background_image)
    canvas.config(width=new_width, height=new_height)


def start_button_pressed():
    print("Game started")
    start_button.place_forget()
    label = tk.Label(root, text="Game started")
    label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)




root = tk.Tk()
root.title("HANGMAN Demo")
root.geometry("600x400")

canvas = tk.Canvas(root)
canvas.place(relwidth=1.0, relheight=1.0)

# Load the original image
original_image = Image.open("GRAPHICS/background.png")

# Resize the image to fit the window
window_width = root.winfo_width()
window_height = root.winfo_height()
resized_image = original_image.resize((window_width, window_height))
background_image = ImageTk.PhotoImage(resized_image)

# Display the image on the canvas
image_item = canvas.create_image(0, 0, anchor=tk.NW, image=background_image)

# Bind the resize event to the canvas
canvas.bind("<Configure>", resize_image)

#start button
start_image = Image.open("GRAPHICS/Start.png")
start_image = ImageTk.PhotoImage(start_image)
start_button = tk.Button(root, image=start_image,command= start_button_pressed)
start_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)



# Run the main loop
root.mainloop()
