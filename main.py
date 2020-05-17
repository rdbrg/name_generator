import tkinter as tk
import tkinter.ttk as ttk
import random
import names_list
import copypaste as cp


class Main(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.title(self, "Name Generator")
        w = 300
        h = 130
        tk.Tk.geometry(self, f"{w}x{h}")
        tk.Tk.resizable(self, False, False)

        self.init_widgets()

    def init_widgets(self):
        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(padx=X, pady=Y, expand=1, fill=tk.BOTH)

        self.lab_output = ttk.Label(self.main_frame, font=20)
        self.lab_output.grid(row=0, column=0, sticky=tk.W, columnspan=3)

        self.var_ch = tk.StringVar()
        self.var_ch.set("male")
        cb_sex_choice_male = ttk.Radiobutton(self.main_frame, text="Male", variable=self.var_ch, value="male")
        cb_sex_choice_male.grid(row=1, column=0, sticky=tk.W)

        cb_sex_choice_female = ttk.Radiobutton(self.main_frame, text="Female", variable=self.var_ch, value="female")
        cb_sex_choice_female.grid(row=2, column=0, sticky=tk.W)

        btn_generate = ttk.Button(self.main_frame, text="Generate", command=self.generate_name)
        btn_generate.grid(row=3, column=0, sticky=tk.W)

        self.lab_status_bar = ttk.Label(self, text="Press Generate", relief=tk.SUNKEN)
        self.lab_status_bar.pack(side=tk.LEFT, expand=1, fill=tk.X)

        btn_copy = ttk.Button(self.main_frame, text="Copy", command=self.copy_output)
        btn_copy.grid(row=3, column=1, sticky=tk.W)

    def generate_name(self):
        if self.var_ch.get() == "male":
            self.lab_output.configure(text=f"{random.choice(names_list.name_male_list)} "
                                           f"{random.choice(names_list.surname_male_list)}")
        else:
            self.lab_output.configure(text=f"{random.choice(names_list.name_female_list)} "
                                           f"{random.choice(names_list.surname_female_list)}")

        self.lab_status_bar.configure(text="Press Copy")

    def copy_output(self):
        cp.copy(self.lab_output.cget('text'))
        self.lab_status_bar.configure(text="Name copy to clipboard")


if __name__ == '__main__':
    X = 20
    Y = 10
    app = Main()
    app.mainloop()
