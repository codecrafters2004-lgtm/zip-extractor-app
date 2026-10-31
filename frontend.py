import FreeSimpleGUI as sg
from backend import archive_extractor


label1 = sg.Text("Select Compressed File")
input1 = sg.Input()
choose_button1 = sg.FileBrowse("Choose", key='archive')


label2 = sg.Text("Select Destination Folder")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key='destination')

extract_button = sg.Button("Extract")
success_message = sg.Text(key="output", text_color="green")


window = sg.Window("Archive Extractor", layout=[[label1, input1, choose_button1],
                                                [label2, input2, choose_button2],
                                                [extract_button, success_message]])


while True:

    event, value = window.read()
    filepath = value['archive']
    dest_dir = value['destination']
    archive_extractor(filepath, dest_dir)
    window['output'].update(value="Extraction Successfull")

    

window.close()
