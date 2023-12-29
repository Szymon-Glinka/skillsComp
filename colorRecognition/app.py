import customtkinter as ctk
from PIL import Image
from customtkinter import filedialog
from backend import detectColor_markOutlines, detectPositionsOfColors

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        #==== Window settings ====
        self.title("Color Detection.py")
        self.geometry(f"{1100}x{580}")

        #==== Window grid ====
        self.grid_rowconfigure((0, 1, 2), weight=1)
        self.grid_columnconfigure((0, 1, 2), weight=1)

        #==== Frames ====
        #--- label to display image ---
        self.imageFrame = ctk.CTkFrame(self, fg_color="transparent")
        self.imageFrame.grid(row=0, column=0, columnspan = 3, padx=10, pady=10, sticky="nsew")

        #--- label to display info ---
        self.infoFrame = ctk.CTkFrame(self)
        self.infoFrame.grid(row=1, column=0, columnspan = 3, padx=10, pady=0, sticky="sew")

        #--- label to display title ---
        self.labelT = ctk.CTkLabel(self.infoFrame, text="Detected colors:", font=("Arial", 17))
        self.labelT.place(relx=0.5, rely=0.1, anchor="center", relwidth=1, relheight=1)

        #==== Buttons ====
        #--- button to open image ---
        self.buttonOpen = ctk.CTkButton(self, text="Open Image", command=self.open_image)
        self.buttonOpen.grid(row=2, column=0, padx=10, pady=(0, 10), sticky="sew")

        #--- button to delete image ---
        self.buttonDel = ctk.CTkButton(self, text="Clear", command=self.del_image)
        self.buttonDel.grid(row=2, column=1, padx=0, pady=(0, 10), sticky="sew")

        #--- button to detect colors ---
        self.buttonDetect = ctk.CTkButton(self, text="Detect colors", command=self.detect_colors)
        self.buttonDetect.grid(row=2, column=2, padx=10, pady=(0, 10), sticky="sew")


    #function to open image
    def open_image(self):
        self.filepath = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")]) #ask user for image
        
        #--- display image ---
        if self.filepath:
            image = Image.open(self.filepath) #open image
        
            #--- resize image ---
            self.heightImg = round(self.winfo_height()/2)
            self.widthImg = round(((self.winfo_width()-50)/3))
            
            #--- display image ---
            photo = ctk.CTkImage(image, size=(self.widthImg, self.heightImg))
            self.labelImgNormal = ctk.CTkLabel(self.imageFrame, text=None, image=photo)
            self.labelImgNormal.pack(side="left", anchor="nw")


    #function to delete image
    def del_image(self):
        try:
            self.labelImgNormal.destroy()
            self.labelImgOutline.destroy()
            self.labelImgPosition.destroy()
            self.insideFrame.destroy()
        except:
            pass


    #function to detect colors
    def detect_colors(self):
        #==== outlines ====
        #--- mark outlines and convert to ctk image ---
        colors, photoOutlines, dim= detectColor_markOutlines(self.filepath) #detect colors and outlines
        photoOutlinesCtk = ctk.CTkImage(photoOutlines, size=(self.widthImg, self.heightImg)) #convert to customtkinter image

        #--- display outlines ---
        self.labelImgOutline = ctk.CTkLabel(self.imageFrame, text=None, image=photoOutlinesCtk)
        self.labelImgOutline.pack(side="left", anchor="nw", padx=15)

        #==== dipslay positions ====
        #--- mark positions and convert to ctk image ---
        info, photoPosition, dim = detectPositionsOfColors(self.filepath) #detect positions and markers
        photoPositionCtk = ctk.CTkImage(photoPosition, size=(self.widthImg, self.heightImg)) #convert to customtkinter image

        #--- display positions ---
        self.labelImgPosition = ctk.CTkLabel(self.imageFrame, text=None, image=photoPositionCtk)
        self.labelImgPosition.pack(side="right", anchor="nw")
        
        #==== display data ====
        counter = 0 #counter to calculate position of the label
        lengthDict = len(info) #length of the info dictionary
        windowWidth = self.winfo_width()-20 #width of the window

        #--- create frame for the labels ---
        self.insideFrame = ctk.CTkFrame(self.infoFrame, fg_color="transparent")
        self.insideFrame.place(relx=0.5, rely=0.5, anchor="center", relwidth=1, relheight=1)

        #--- label to display title ---
        self.labelT = ctk.CTkLabel(self.insideFrame, text="Detected colors:", font=("Arial", 17))
        self.labelT.place(relx=0.5, rely=0.1, anchor="center", relwidth=1, relheight=1)

        #--- loop through the info dictionary ---
        for color, data in info.items():
            positionX = counter*windowWidth//lengthDict+(windowWidth//(lengthDict*2)-50) #calculate position of the label

            #set text for the label
            infoText = f"""
                        Detected color: {color.upper()}
                        Position: {data[3].upper()} - {data[2].upper()}
                        Offset from center: {data[4]}, {data[5]}
                        Position of marker: {data[0]}, {data[1]}
                        (from top-left of image)
                        """
            #--- display the label ---
            self.labelPos = ctk.CTkLabel(self.insideFrame, text=infoText, font=("Arial", 15), width=100)
            self.labelPos.place(rely=0.5, anchor="center", relwidth=0.3, x=positionX)

            counter += 1 #increase counter to move to next column


#==== Main ====
if __name__ == "__main__":
    app = App()
    app.mainloop()