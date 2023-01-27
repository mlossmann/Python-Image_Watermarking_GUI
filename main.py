from tkinter import *

# function to watermark image
def watermark_img():
    print(f"The watermark text is: {watermark_textbox.get()}")
    print(f"The Path of the image is: {image_path_textbox.get()}")
    print(f"The watermark text is: {conv_image_path_textbox.get()}")

# tkinter config
window = Tk()
window.title("Image Watermarking Application")
window.minsize(width=500, height=300)


my_label = Label(text="Image Watermarking Application", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0, columnspan=3)

watermark_text_label = Label(text="Watermark text: ")
watermark_text_label.grid(column=0, row=1)

watermark_textbox = Entry(width=25)
watermark_textbox.grid(column=1, row=1)

image_path_label = Label(text="Image Path: ")
image_path_label.grid(column=0, row=2)

image_path_textbox = Entry(width=25)
image_path_textbox.grid(column=1, row=2)

conv_image_path_label = Label(text="Converted Image Path: ")
conv_image_path_label.grid(column=0, row=3)

conv_image_path_textbox = Entry(width=25)
conv_image_path_textbox.grid(column=1, row=3)

convert_button = Button(text='Watermark Image', command=watermark_img)
convert_button.grid(column=1, row=4)

window.mainloop()
