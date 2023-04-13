# Library imports
from tkinter import Tk, filedialog as fd
from widgets import *


# uploads the image and resizes it to the frame
def upload_file():
    filename = fd.askopenfilename(filetypes=[("jpeg", ".jpg .jpeg"),
                                             ("png", ".png"),
                                             ("bitmap", "bmp"),
                                             ("gif", ".gif")])
    photo_frame_widget.upload_picture(filename)


# applies a the watermark text and a logo if checked
def apply_watermark():
    watermark_text = apply_btn.wm_text_var.get()
    watermark_cb_value = apply_btn.wm_register_bnt_var.get()
    photo_frame_widget.update_watermark(watermark_text, watermark_cb_value)


# saves the image at project directory
def save_image():
    image_to_save = photo_frame_widget.image.convert('RGB')
    image_to_save.save('watermarked_image.jpg')


# Set up window
window = Tk()
window.geometry("810x525")
window.title("Watermark")
window.resizable(False, False)

# Place widgets
tile_sub_widget = TextAreaWidget(window, "WaterMark App", "A simple tkinter application to apply watermark")
tile_sub_widget.grid(row=0, column=0, columnspan=3)
photo_frame_widget = ImageFrameWidget(window)
photo_frame_widget.grid(row=1, column=0, rowspan=3)
upload_btn = UploadButtonWidget(window, callback=upload_file)
upload_btn.grid(row=1, column=2, padx=20, pady=10)
apply_btn = ApplyButtonWidget(window, callback=apply_watermark)
apply_btn.grid(row=2, column=2, padx=20, pady=10)
save_btn = SaveButtonWidget(window, callback=lambda: save_image())
save_btn.grid(row=3, column=2, padx=20, pady=10)

window.mainloop()
