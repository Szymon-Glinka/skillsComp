import customtkinter as ctk
from PIL import Image
from customtkinter import filedialog
import cv2
from datetime import datetime
from backend import basicFix, fixBlur, fixPos, markQRcode

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        #==== Window settings ====
        self.title("Color Detection.py")
        self.geometry(f"{1100}x{580}")
        widthWin = round(self.winfo_width()/3)

        #==== Window grid ====
        self.grid_rowconfigure((0, 1), weight=3)
        self.grid_rowconfigure((2, 3), weight=1)
        self.grid_columnconfigure((0, 1, 2), weight=1)

        #==== Buttons ====
        #--- button to open image ---
        self.buttonOpen = ctk.CTkButton(self, text="Open Image", command=self.open_image)
        self.buttonOpen.grid(row=3, column=0, padx=10, pady=10, sticky="sew")

        #--- button to delete image ---
        self.buttonPlot = ctk.CTkButton(self, text="Plot Data", command=self.printData)
        self.buttonPlot.grid(row=3, column=2, padx=10, pady=10, sticky="sew")

        #--- button to detect qr ---
        self.buttonDetect = ctk.CTkButton(self, text="Detect QR", command=self.detect_qr)
        self.buttonDetect.grid(row=3, column=1, pady=10, sticky="sew")

        #==== Frames ====
        #--- frame to display image ---
        self.imageFrame = ctk.CTkFrame(self, fg_color="transparent")
        self.imageFrame.grid(row=0, rowspan=2, column=0, columnspan=3, padx=10, pady=10, sticky="new")

        #--- frame to display info ---
        self.infoFrame = ctk.CTkFrame(self, height=50)
        self.infoFrame.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky="sew")
        
        #--- label to display info ---
        self.labelData = ctk.CTkLabel(self.infoFrame, text="Disclaimer: Detecting QR codes might take a while", font=("Arial", 15))
        self.labelData.place(rely=0.5, relx=0.05, anchor="w")


    #function to open image
    def open_image(self):
        self.detectedQr = False

        #--- delete previous image and info ---
        try:
            self.labelImgNormal.destroy()
            self.labelImgMark.destroy()
            self.labelData.destroy()
        except:
            pass

        self.filepath = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")]) #ask user for image
        
        #==== display image ====
        if self.filepath:
            image = Image.open(self.filepath) #open image
        
            #--- resize image ---
            self.heightImg = round(self.winfo_height()/1.5)
            self.widthImg = round((self.winfo_width()-50)/2)
            image.thumbnail((self.widthImg, self.heightImg))
            self.widthFixedImg, self.heightFixedImg = image.size

            #--- display image ---
            photo = ctk.CTkImage(image, size=(self.widthFixedImg, self.heightFixedImg))
            self.labelImgNormal = ctk.CTkLabel(self.imageFrame, text=None, image=photo)
            self.labelImgNormal.pack(side="left", anchor="w")


    #function to plot data
    def printData(self):
        #==== if QR have been scaned do otherwise wait ====
        if self.detectedQr:
            directory = filedialog.asksaveasfilename(defaultextension=".txt") #ask user for directory

            #--- get current time ---
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")

            #--- save data to file ---
            try:
                with open(directory, "w") as file:
                    #--- write dictionary to file ---
                    textDictionary = f"{current_time} - QRcode's data: {self.dataDisplay}"
                    file.write(textDictionary)
            except:
                pass


    #function to detect qr codes
    def detect_qr(self):
        check = False
        image = cv2.imread(self.filepath) #Load the image
        self.detectedQr = True

        #==== Fixing images to try and detect qr code ====
        #--- using fixPos to fix normal image ---
        if check == False:
            infoFpos, imageFpos = fixPos(image)
            if infoFpos != None:
                finalImage = markQRcode(imageFpos)
                check = True
                self.dataDisplay = infoFpos

        #--- using basicFix to fix normal image ---
        if check == False:
            infoFbasic, imageFbasic = basicFix(image)
            if infoFbasic != None:
                finalImage = markQRcode(imageFbasic)
                check = True
                self.dataDisplay = infoFbasic

        #--- using fixBlur to fix normal image ---
        if check == False:
            infoFblur, imageFblur = fixBlur(image)
            if infoFblur != None:
                finalImage = markQRcode(imageFblur)
                check = True
                self.dataDisplay = infoFblur

        #--- using basicFix to fix fixedPos image ---
        if check == False:
            infoFbasic, imageFbasic = basicFix(imageFpos)
            if infoFbasic != None:
                finalImage = markQRcode(imageFbasic) 
                check = True
                self.dataDisplay = infoFbasic

        #--- using fixBlur to fix fixedPos image ---
        if check == False:
            infoFblur, imageFblur = fixBlur(imageFpos)
            if infoFblur != None:
                finalImage = markQRcode(imageFblur)
                check = True
                self.dataDisplay = infoFblur

        #--- Returning normal image and no data if qr code not detected ---
        if check == False:
            finalImage = markQRcode(image)
            check = True
            self.dataDisplay = "No QR code detected"

        #--- display image ---
        photoMark = ctk.CTkImage(finalImage, size=(self.widthFixedImg, self.heightFixedImg)) #convert to customtkinter image
        self.labelImgMark = ctk.CTkLabel(self.imageFrame, text=None, image=photoMark) 
        self.labelImgMark.pack(side="right", anchor="w")

        #--- display info ---
        self.labelData = ctk.CTkLabel(self.infoFrame, text=f"Text read: {self.dataDisplay}", font=("Arial", 15))
        self.labelData.place(rely=0.5, relx=0.95, anchor="e")


#==== Main ====
if __name__ == "__main__":
    app = App()
    app.mainloop()