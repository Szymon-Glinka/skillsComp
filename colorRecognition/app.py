import customtkinter as ctk
from PIL import  Image
from customtkinter import filedialog

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        #========== Init ==========
        #setting up the main window
        self.title("CustomTkinter complex_example.py")
        self.geometry(f"{1100}x{580}")

        #setting up the grid system
        self.grid_rowconfigure((0, 1, 2), weight=1)
        self.grid_columnconfigure((0, 1, 2), weight=1)
    
        #========== Buttons ==========
        #button to open image
        self.buttonOpen = ctk.CTkButton(self, text="Open Image", command=self.open_image)
        self.buttonOpen.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="new")

        #button to delete image
        self.buttonDel = ctk.CTkButton(self, text="Clear", command=self.del_image)
        self.buttonDel.grid(row=0, column=1, padx=0, pady=(10, 0), sticky="new")

        #button to detect colors
        self.buttonDetect = ctk.CTkButton(self, text="Detect colors", command=self.detect_colors)
        self.buttonDetect.grid(row=0, column=2, padx=10, pady=(10, 0), sticky="new")

        #========== Labels ==========
        #label to display image
        self.imageFrame = ctk.CTkFrame(self, fg_color="transparent")
        self.imageFrame.grid(row=1, column=0, columnspan = 3, padx=10, pady=10, sticky="nesw")

        #label to display data
        self.dataFrame = ctk.CTkFrame(self)
        self.dataFrame.grid(row=2, column=0, columnspan = 3, padx=10, pady=(0, 10), sticky="nesw")
        

    #========== Functions ==========
    #function to open image
    def open_image(self):
        self.filepath = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")]) #ask user for image
        if self.filepath:
            image = Image.open(self.filepath)

            #resize image
            self.heightImg = round(self.winfo_height()/3)
            self.widthImg = round(((self.winfo_width()-50)/3))
            
            #display image
            photo = ctk.CTkImage(image, size=(self.widthImg, self.heightImg))
            self.labelImgNormal = ctk.CTkLabel(self.imageFrame, text=None, image=photo)
            self.labelImgNormal.pack(side="left", anchor="nw")

    #function to delete image  
    def del_image(self):
        self.labelImgNormal.destroy()
        self.labelImgOutline.destroy()
        self.labelImgPosition.destroy()

    #function to detect colors
    def detect_colors(self):
        '''
        #display outlined colors
        self.labelImgOutline = ctk.CTkLabel(self.imageFrame, text=None, image=photo)
        self.labelImgOutline.pack(side="right", anchor="nw")

        #dipslay positions
        self.labelImgPosition = ctk.CTkLabel(self.imageFrame, text=None, image=photo)
        self.labelImgPosition.pack(side="left", anchor="nw", padx=15)
        '''

#========== Main ==========
if __name__ == "__main__":
    app = App()
    app.mainloop()