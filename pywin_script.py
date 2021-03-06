from pywinauto.application import Application
from time import gmtime, strftime


# Run notepad application
app = Application().start('notepad.exe')

# Set focuse on test filed
app.UntitledNotepad.Edit.set_keyboard_focus()

# Type some test
app.UntitledNotepad.Edit.send_keystrokes("First Line of the text {ENTER}Second line of the text", with_spaces = True)

# Go to the menu
app.UntitledNotepad.menu_select("Format->Font...")

# Select font style from the list
app.Font.ComboBox.Select(u'Comic Sans MS')

# Select font type from the list
app.Font.ComboBox2.Select(u'Bold Italic')

# Select font size from the list and close the menu
app.Font.Edit3.set_keyboard_focus()
app.Font.Edit3.send_keystrokes(u"17", with_spaces = True)
app.Font.OK.Click()

# Page setup
app.UntitledNotepad.menu_select("File->Page setup...")
app.Dialog.ComboBox.Select(u'A5')
#My printer has not A3 format so I used A5
app.Dialog.OK.Click()

# Printing
# I have installed http://www.win8pdf.com/pdf-printer.html PDF printer

app.UntitledNotepad.menu_select("File->Print...")
app.Print.FolderView.GetItem("PDF Printer").Click()
app.Print[u'&Print'].Click()

#Connecting to PDF printer
app2 = Application().connect(path=r"C:\Program Files\PDF Printer for Windows 8\PDFPrinter.exe")
app2.SaveAs.Wait('ready')

#Saving PDF File
app2.SaveAs.Wait('ready')
app2.SaveAs.Edit.SetFocus()

#Creating Unique Filename
filename = strftime("%Y-%m-%d_%H-%M-%S", gmtime())
filename = filename + ".PDF"
app2.SaveAs.Edit.send_keystrokes(filename)

#Saving
app2.SaveAs.Save.Click()




