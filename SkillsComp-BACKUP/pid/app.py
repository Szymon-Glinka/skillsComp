import customtkinter as ctk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from pid import simulation
import logging
from PIL import Image

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        #==== Window settings ====
        self.title("PID")
        self.geometry(f"{1100}x{580}")

        #==== Window grid ====
        self.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9), weight=1)
        self.grid_columnconfigure((3, 4, 5), weight=3)
        self.grid_columnconfigure((0, 1, 2), weight=0)


        #==== kp, ki, kd ====
        #--- kp ---
        #kp slider
        self.sliderKP = ctk.CTkSlider(self, from_=0.0, to=1.0, orientation="horizontal", command=self.slider_kp, number_of_steps=100)
        self.sliderKP.grid(row=0, column=0, columnspan=2, sticky="new", padx=10, pady=(30, 0))
        #kp label
        self.labelKp = ctk.CTkLabel(self, text="kP: ")
        self.labelKp.grid(row=0, column=0, columnspan=2, sticky="new", padx=10, pady=(0, 10))
        #kp entry
        self.entryKp = ctk.CTkEntry(self, placeholder_text="Kp", width=70)
        self.entryKp.grid(row=0, column=2, sticky="new", padx=10, pady=(25, 0))

        #--- ki ---
        #ki slider
        self.sliderKI = ctk.CTkSlider(self, from_=0.0, to=1.0, orientation="horizontal", command=self.slider_ki, number_of_steps=100)
        self.sliderKI.grid(row=1, column=0, columnspan=2, sticky="new", padx=10, pady=(30, 0))
        #ki label
        self.labelKi = ctk.CTkLabel(self, text="kI: ")
        self.labelKi.grid(row=1, column=0, columnspan=2, sticky="new", padx=10, pady=(0, 10))
        #ki entry
        self.entryKi = ctk.CTkEntry(self, placeholder_text="Ki", width=70)
        self.entryKi.grid(row=1, column=2, sticky="new", padx=10, pady=(25, 0))

        #--- kd ---
        #kd slider
        self.sliderKD = ctk.CTkSlider(self, from_=0.0, to=1.0, orientation="horizontal", command=self.slider_kd, number_of_steps=100)
        self.sliderKD.grid(row=2, column=0, columnspan=2, sticky="new", padx=10, pady=(30, 0))
        #kd label
        self.labelKd = ctk.CTkLabel(self, text="kD: ")
        self.labelKd.grid(row=2, column=0, columnspan=2, sticky="new", padx=10, pady=(0, 10))
        #kd entry
        self.entryKd = ctk.CTkEntry(self, placeholder_text="Kd", width=70)
        self.entryKd.grid(row=2, column=2, sticky="new", padx=10, pady=(25, 0))

        #==== Other inputs ====
        #--- setpoint ---
        #setpoint entry
        self.entrySetpoint = ctk.CTkEntry(self, placeholder_text="Setpoint", width=100)
        self.entrySetpoint.grid(row=3, column=1, columnspan=2, sticky="ne", padx=0, pady=10)
        #setpoint label
        self.labelSetpoint = ctk.CTkLabel(self, text="Setpoint: default 100")
        self.labelSetpoint.grid(row=3, column=0, sticky="nw", padx=(10, 0), pady=10)

        #--- initial value ---
        #initial value entry
        self.entryInitialValue = ctk.CTkEntry(self, placeholder_text="Initial Value", width=100)
        self.entryInitialValue.grid(row=4, column=1, columnspan=2, sticky="ne", padx=0, pady=10)
        #initial value label
        self.labelInitialValue = ctk.CTkLabel(self, text="Initial Value: default 0")
        self.labelInitialValue.grid(row=4, column=0, sticky="nw", padx=(10, 0), pady=10)

        #--- step size ---
        #step size entry
        self.entryStepSize = ctk.CTkEntry(self, placeholder_text="Steps", width=100)
        self.entryStepSize.grid(row=5, column=1, columnspan=2, sticky="ne", padx=0, pady=10)
        #step size label
        self.labelStepSize = ctk.CTkLabel(self, text="Steps: default 250")
        self.labelStepSize.grid(row=5, column=0, sticky="nw", padx=(10, 0), pady=10)

        #--- delta T ---
        #delta T entry
        self.entryDeltaT = ctk.CTkEntry(self, placeholder_text="Delta T", width=100)
        self.entryDeltaT.grid(row=6, column=1, columnspan=2, sticky="ne", padx=0, pady=10)
        #delta T label
        self.labelDeltaT = ctk.CTkLabel(self, text="Delta T: default 0.1")
        self.labelDeltaT.grid(row=6, column=0, sticky="nw", padx=(10, 0), pady=10)

        #==== equation image====
        try:
            image = Image.open("pid.jpg") #open image
            photo = ctk.CTkImage(image, size=(100, 40))
            self.labelImgNormal = ctk.CTkLabel(self, text=None, image=photo)
            self.labelImgNormal.grid(row=9, column=0, columnspan=3, sticky="new", padx=10, pady=10)
        except:
            self.equation = ctk.CTkLabel(self, text="2s + 3s / 4")
            self.equation.grid(row=9, column=0, columnspan=3, sticky="new", padx=10, pady=10)

        #==== checkbox ====
        #--- checkbox 1 ---
        self.checkBox1_var = ctk.BooleanVar()
        self.checkBox1 = ctk.CTkCheckBox(self, text="Zeigler-nichols autotuning OFF", variable=self.checkBox1_var, command=self.onSelect)
        self.checkBox1.grid(row=7, column=0, sticky="nw", padx=10, pady=10)

        #==== submit button ====
        self.CTkButton = ctk.CTkButton(self, text="Submit", command=self.on_button_click)
        self.CTkButton.grid(row=8, column=0, columnspan=3, sticky="new", padx=10, pady=10)

    #==== Slider functions ====
    def slider_kp(self, value):
        self.kP_valueRead = value
        self.labelKp.configure(text=f"kP: {self.kP_valueRead}")

    def slider_ki(self, value):
        self.kI_valueRead = value
        self.labelKi.configure(text=f"kI: {self.kI_valueRead}")

    def slider_kd(self, value):
        self.kD_valueRead = value
        self.labelKd.configure(text=f"kD: {self.kD_valueRead}")

    #==== checkbox functions ====
    def onSelect(self):
        if self.checkBox1_var.get():
            self.checkBox1.configure(text="Zeigler-nichols autotuning ON")
        else:
            self.checkBox1.configure(text="Zeigler-nichols autotuning OFF")

        
    #==== Perform PID algorythm ====,,
    def on_button_click(self):
        #==== getting values for kp, ki, kd ===
        #--- getting values from sliders ---
        #try and except is used to prevent errors when the sliders are not used
        #kp
        try:
            self.kp = round(self.kP_valueRead, 2)
        except:
            self.kp = 0.5
            self.labelKp.configure(text=f"kP: {self.kp}")
        #ki
        try:
            self.ki = round(self.kI_valueRead, 2)
        except:
            self.ki = 0.5
            self.labelKi.configure(text=f"kI: {self.ki}")
        #kd
        try:    
            self.kd = round(self.kD_valueRead, 2)
        except:
            self.kd = 0.5
            self.labelKd.configure(text=f"kD: {self.kd}")

        #--- getting values from entries ---
        try:
            #--- kp ---
            self.kp = float(self.entryKp.get())
            self.entryKp.delete(0, "end")
            self.labelKp.configure(text=f"kP: {self.kp}")
            self.sliderKP.set(self.kp)

            #--- ki ---
            self.ki = float(self.entryKi.get())
            self.entryKi.delete(0, "end")
            self.labelKi.configure(text=f"kI: {self.ki}")
            self.sliderKI.set(self.ki)

            #--- kd ---
            self.kd = float(self.entryKd.get())
            self.entryKd.delete(0, "end")
            self.labelKd.configure(text=f"kD: {self.kd}")
            self.sliderKD.set(self.kd)
        except:
            logging.info("kP or kI or kD entry error, probably not a number OR slider used")

        #==== geting values for the rest of variables====
        #--- setpoint ---
        try:
            self.setpoint = float(self.entrySetpoint.get())
        except:
            self.setpoint = 100.0
            logging.info("Setpoint entry error, probably not a number OR left empty")
        self.labelSetpoint.configure(text=f"Setpoint: {self.setpoint}")

        #--- initial value ---
        try:
            self.initialValue = float(self.entryInitialValue.get())
        except:
            self.initialValue = 0.0
            logging.info("Initial value entry error, probably not a number OR left empty")
        self.labelInitialValue.configure(text=f"Initial Value: {self.initialValue}")

        #--- step size ---
        try:
            self.stepSize = int(self.entryStepSize.get())
        except:
            self.stepSize = 250
            logging.info("Step size entry error, probably not a number OR left empty")
        self.labelStepSize.configure(text=f"Steps : {self.stepSize}")

        #--- delta T ---
        try:
            self.deltaT = float(self.entryDeltaT.get())
        except:
            self.deltaT = 0.1
            logging.info("Delta T entry error, probably not a number OR left empty")
        self.labelDeltaT.configure(text=f"Delta T: {self.deltaT}")

        #==== Running simulation ====
        resList, timeList = simulation(self.kp, self.ki, self.kd, self.deltaT, self.stepSize, self.initialValue, self.setpoint, self.checkBox1_var.get())

        #==== Plotting graphs ====
        fig = Figure(figsize=(5, 4), dpi=100)

        #--- creating a list of ideal values ---
        idealValList = []
        idealValList.append(self.initialValue)
        for _ in range(self.stepSize-1):
            idealValList.append(self.setpoint)

        #--- creating two graphs ---
        graph = fig.add_subplot(111)
        real, =graph.plot(timeList, resList, color="orange", linewidth=3, label="Real/PID")             #create a graph of real values
        ideal, = graph.plot(timeList, idealValList, color="green", linestyle="dashed", label="Ideal")   #create a graph of ideal values
        graph.set_ylabel("X value")
        graph.set_xlabel("time (s)")
        graph.set_title("PID regulator simulation")
        graph.legend(handles=[real, ideal])                                                             #create a legend

        #--- Create canvas for ctk ---
        canvas = FigureCanvasTkAgg(fig)
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column=3, rowspan=10, columnspan=3, sticky="nesw", padx=10, pady=10)
        

#==== Main ====
if __name__ == "__main__":
    logging.basicConfig(level=logging.ERROR, format="%(asctime)s %(levelname)s %(message)s", datefmt="%y-%m-%d %H:%M") #logging setup
    app = App()
    app.mainloop()