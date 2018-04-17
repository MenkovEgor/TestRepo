from pywinauto.application import Application
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
app.Dialog[u'L&andscape'].Click()
app.Dialog.ComboBox.Select(u'A5')
app.Dialog.OK.send_keystrokes("{ENTER}")
# Printing
#app.UntitledNotepad.menu_select("File->Print...")

# Click on a button
#app.AboutNotepad.OK.click()
# Type a text string
