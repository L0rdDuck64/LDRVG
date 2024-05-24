from customtkinter import *

# Setuping

vidType = "Auto"
useLimitLenght = False

# Functions

def saveTxtToFile(textbox, filename):
    text_content = textbox.get("1.0", "end-1c")
    with open(f"data/{filename}", "w") as file:
        file.write(text_content)

def saveTxtFromFile(filename, textbox):
    with open(f'data/{filename}', "r") as file:
        file_content = file.read()
        textbox.delete("1.0", "end")
        textbox.insert("1.0", file_content)

def launchMainGUI(res):

    def setVideoType(value):
        vidType = value

    def toggleLimitLenght():
        useLimitLenght = CheckerVideoLimit.get()

        if useLimitLenght == 1:
            VideoLenghtTextBox.configure(state='normal')
        else:
            VideoLenghtTextBox.configure(state='disabled')

    def saveSubs():
        saveTxtToFile(SubsTextBox, 'subs.txt')

    app = CTk()
    app.geometry(f"{res[0]}x{res[1]}")
    app.title("LDRVG")

    titLabel = CTkLabel(master=app, text="LDRVG", font=('Arial', 28), text_color='#D5AF32')
    SVTLabel = CTkLabel(master=app, text="Video Type", font=('Arial', 17))
    genVidBut = CTkButton(master=app, text="Generate Video", corner_radius=5)
    selVidType = CTkComboBox(master=app, values=["Auto", "Long", "Shorts"], command=setVideoType)
    CheckerVideoLimit = CTkCheckBox(master=app, text="Limit Video Lengtht?", command=toggleLimitLenght)
    VideoLenghtTextBox = CTkEntry(master=app, placeholder_text="Length limit")
    SubsTextBox = CTkTextbox(master=app, width=180, height=180, wrap=None)
    SaveSubsBtn = CTkButton(master=app, text="Save Subreddits", corner_radius=5, width=180, command=saveSubs)

    titLabel.place(relx=0.5, rely=0.04, anchor='center')
    genVidBut.place(relx=0.85, rely=0.05, anchor='center')
    selVidType.place(relx=0.15, rely=0.08, anchor='center')
    SVTLabel.place(relx=0.18, rely=0.03, anchor='e')
    CheckerVideoLimit.place(relx=0.15, rely=0.15, anchor='center')
    VideoLenghtTextBox.place(relx=0.15,rely=0.2, anchor='center')
    SubsTextBox.place(relx=0.15, rely=0.7, anchor='center')
    SaveSubsBtn.place(relx=0.3, rely=0.52, anchor='e')

    saveTxtFromFile('subs.txt', SubsTextBox)

    app.mainloop()