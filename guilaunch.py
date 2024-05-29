from customtkinter import *
from tkinter import filedialog
from os import getenv, path
from auto_udd import get_all_udds

# Setuping

def saveTxtToFile(text, filename, lines):
    with open(f"data/{filename}", "w") as file:
        if lines:
            file.writelines(text)
        else:
            file.write(text)

def saveTxtFromFile(filename):
    with open(f'data/{filename}', "r") as file:
        file_content = file.read()

        return file_content
    
def changeTxtLine(text, lineNum, filename):
    file_content = saveTxtFromFile(filename).splitlines()
    file_content[lineNum - 1] = text
    file_content = [line if line.endswith('\n') or line == file_content[len(file_content) - 1] else line + '\n' for line in file_content]
    saveTxtToFile(file_content, filename, True)

def getTxtLine(line, filename):
    file_content = saveTxtFromFile(filename).splitlines()

    return file_content[line - 1]

def openFileDialog(typ, titl):
        if typ == 'File':
            arch = filedialog.askopenfilename(title=titl)
        elif typ == 'Folder':
            arch = filedialog.askdirectory(title=titl)
        return arch

# Main

lcp = 'chromium/chrome.exe'
vidType = "Auto"
vidLang = "en"
uddFile = getTxtLine(3, 'data.txt')
uddFile = uddFile if uddFile != 'None' else None
chromium = getTxtLine(4, 'data.txt')
chromium = chromium if chromium != lcp else lcp
uddSelections = ['None', *(list(get_all_udds().keys())), *([uddFile] if uddFile else [])]
useLimitLenght = False
subsList = []

def launchMainGUI(res):

    def setVideoType(value):
        vidType = value
        changeTxtLine(vidType, 1, 'data.txt')
    
    def setVideoLang(value):
        vidLang = value
        changeTxtLine(vidLang, 2, 'data.txt')

    def setUDD(value):
        uddFile = value
        changeTxtLine(value, 3, 'data.txt')
        if value == 'None':
            uddFile = None

    def setBwr(value):
        chromium = value
        changeTxtLine(value, 4, 'data.txt')
        if value == "Auto(local)":
            chromium = lcp

    def toggleLimitLenght():
        useLimitLenght = CheckerVideoLimit.get()

        if useLimitLenght == 1:
            VideoLenghtTextBox.configure(state='normal')
        else:
            VideoLenghtTextBox.configure(state='disabled')

    def saveSubs():
        saveTxtToFile(SubsTextBox.get("1.0", "end-1c"), 'subs.txt')

    def SelectUserDDir():
        tempVar = openFileDialog('Folder', "Select User Data Directory")
        if tempVar:
            uddFile = tempVar
            changeTxtLine(uddFile, 3, 'data.txt')
            selUDD.configure(values=["None", uddFile])
            selUDD.set(uddFile)

    def selectBrowserExe():
        tempvar = openFileDialog('File', "Select browser executable")
        if tempvar:
            chromium = tempvar
            changeTxtLine(chromium, 4, 'data.txt')
            selBrowser.configure(values=["Auto(local)", chromium])
            selBrowser.set(chromium)

    app = CTk()
    app.geometry(f"{res[0]}x{res[1]}")
    app.title("LDRVG")

    titLabel = CTkLabel(master=app, text="LDRVG", font=('Arial', 28), text_color='#D5AF32')
    SVTLabel = CTkLabel(master=app, text="Video Type", font=('Arial', 17))
    SVLLabel = CTkLabel(master=app, text="Video Lang", font=('Arial', 17))
    UDDLabel = CTkLabel(master=app, text="User Data Dir", font=('Arial', 17))
    Blabel = CTkLabel(master=app, text="Chromium", font=('Arial', 17))
    genVidBut = CTkButton(master=app, text="Generate Video", corner_radius=5)
    selectUDDbut = CTkButton(master=app, text="Select Folder", corner_radius=5, width=100, height=20, command=SelectUserDDir)
    selectBBtn = CTkButton(master=app, text="Select File", corner_radius=5, width=100, height=20, command=selectBrowserExe)
    selVidType = CTkComboBox(master=app, values=["Auto", "Long", "Shorts"], command=setVideoType)
    selVidLang = CTkComboBox(master=app, values=["en", "pt", "es"], command=setVideoLang)
    selUDD = CTkComboBox(master=app, values=uddSelections, command=setUDD)
    selBrowser = CTkComboBox(master=app, values=["Auto(local)", *([chromium] if chromium != "Auto(local)" else [])], command=setBwr)
    CheckerVideoLimit = CTkCheckBox(master=app, text="Limit Video Length?", command=toggleLimitLenght)
    VideoLenghtTextBox = CTkEntry(master=app, placeholder_text="Length limit")
    SubsTextBox = CTkTextbox(master=app, width=180, height=180, wrap=None)
    SaveSubsBtn = CTkButton(master=app, text="Save Subreddits", corner_radius=5, width=180, command=saveSubs)

    titLabel.place(relx=0.5, rely=0.04, anchor='center')
    genVidBut.place(relx=0.85, rely=0.05, anchor='center')
    selVidType.place(relx=0.15, rely=0.08, anchor='center')
    SVTLabel.place(relx=0.18, rely=0.03, anchor='e')
    CheckerVideoLimit.place(relx=0.15, rely=0.15, anchor='center')
    VideoLenghtTextBox.place(relx=0.15,rely=0.2, anchor='center')
    SubsTextBox.place(relx=0.15, rely=0.85, anchor='center')
    SaveSubsBtn.place(relx=0.15, rely=0.67, anchor='center')
    SVLLabel.place(relx=0.18, rely=0.26, anchor='e')
    selVidLang.place(relx=0.15, rely=0.31, anchor='center')
    selectUDDbut.place(relx=0.85, rely=0.16, anchor='center')
    selUDD.place(relx=0.85, rely=0.205, anchor='center')
    UDDLabel.place(relx=0.85, rely=0.12, anchor='center')
    Blabel.place(relx=0.85, rely=0.26, anchor='center')
    selectBBtn.place(relx=0.85, rely=0.295, anchor='center')
    selBrowser.place(relx=0.85, rely=0.34, anchor='center')

    vidType = getTxtLine(1, 'data.txt')
    vidLang = getTxtLine(2, 'data.txt')
    subsList = saveTxtFromFile('subs.txt')

    SubsTextBox.delete("1.0", "end")
    SubsTextBox.insert("1.0", subsList)

    selVidType.set(vidType)
    selVidLang.set(vidLang)
    selUDD.set(getTxtLine(3, 'data.txt'))
    selBrowser.set(getTxtLine(4, 'data.txt'))

    app.mainloop()