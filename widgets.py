# import Libraries
from tkinter import Button, Entry, Frame, Label, Image, StringVar, LEFT, IntVar, Checkbutton
from PIL import ImageTk, Image, ImageDraw, ImageFont


# widget of title and subtitle text
class TextAreaWidget(Frame):
    def __init__(self, parent, title, subtitle):
        super().__init__(parent)
        self.title_label = Label(self, text=title, font=("Arial 18 bold"), anchor="center")
        self.title_label.grid(row=0, column=0, padx=10, pady=10)
        self.subtitle_label = Label(self, text=subtitle, font=("Arial", 13), anchor="center")
        self.subtitle_label.grid(row=1, column=0, padx=5, pady=5)


# widget of the frame where the uploaded phto is being placed
class ImageFrameWidget(Label):
    def __init__(self, parent):
        super().__init__(parent)
        self.image = Image.new(mode="RGBA", size=(520, 400), color="grey")
        self.photo = ImageTk.PhotoImage(self.image)
        self.configure(image=self.photo, padx=5, pady=5)

    # based on filepath,it updates the image on the frame and resizes it
    def upload_picture(self, selected_filepath):
        self.image = Image.open(selected_filepath).convert("RGBA")
        self.image = self.image.resize((520, 400))
        self.photo = ImageTk.PhotoImage(self.image)
        self.configure(image=self.photo)

    # Applies the watermark based on user inputs
    def update_watermark(self, watermanrk_text, check_icon_var):
        draw = ImageDraw.Draw(self.image)
        w, h = self.image.size
        x, y = int(w / 2), int(h / 2)
        if x > y:
            font_size = y
        elif y > x:
            font_size = x
        else:
            font_size = x
        font = ImageFont.truetype("arial.ttf", int(font_size / 3))
        draw.text((x, y), watermanrk_text, fill=(201, 47, 36), font=font, anchor='ms')
        if check_icon_var == 1:
            icon_wm = Image.open("images/trademark.png")
            icon_wm.thumbnail((50, 50))
            self.image.paste(icon_wm, (470, 350))
        self.photo = ImageTk.PhotoImage(self.image)
        self.configure(image=self.photo)


# upload photo button widget
class UploadButtonWidget(Button):
    def __init__(self, parent, callback):
        super().__init__(parent)
        temp_image = Image.open("images/upload.png")
        self.image = temp_image.resize((36, 36))
        self.photo = ImageTk.PhotoImage(image=self.image)
        self.btn_text = "Upload Photo"
        self.configure(image=self.photo, text=self.btn_text, compound=LEFT, command=callback,
                       font=('Helvetica 13 bold'))


# Apply photo button widget
class ApplyButtonWidget(Frame):
    def __init__(self, parent, callback):
        super().__init__(parent)
        self.wm_text_var = StringVar()
        self.wm_register_bnt_var = IntVar()
        self.entry_label = Label(self, text="Enter WM", font=('Helvetica 13 bold'), anchor="w")
        self.entry_label.grid(row=0, column=0, padx=2, pady=5, rowspan=2)
        self.entry_textbox = Entry(self, textvariable=self.wm_text_var, font=('calibre', 10, 'normal'))
        self.entry_textbox.grid(row=0, column=1, pady=1)
        self.checkbtn = Checkbutton(self, text="Icon Watermark",
                                    font=('Helvetica 10 normal'),
                                    variable=self.wm_register_bnt_var,
                                    onvalue=1,
                                    offvalue=0,
                                    height=2,
                                    width=13, anchor="w")
        self.checkbtn.grid(row=1, column=1, padx=2, pady=1, sticky="w")

        temp_image = Image.open("images/apply.png")
        self.image = temp_image.resize((36, 36))
        self.photo = ImageTk.PhotoImage(image=self.image)
        self.btn_apply = Button(self, text="Apply watermark", compound=LEFT, command=callback,
                                font=('Helvetica 13 bold'), image=self.photo, anchor="w")
        self.btn_apply.grid(row=2, column=0, columnspan=2)


# Saves the watermarked photo button widget
class SaveButtonWidget(Button):
    def __init__(self, parent, callback):
        super().__init__(parent)
        temp_image = Image.open("images/save.png")
        self.image = temp_image.resize((36, 36))
        self.photo = ImageTk.PhotoImage(image=self.image)
        self.btn_text = "Download"
        self.configure(image=self.photo, text=self.btn_text, compound=LEFT, command=callback,
                       font=('Helvetica 13 bold'))
