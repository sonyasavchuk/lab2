import PySimpleGUI as sg
import Searcher
import xml.etree.ElementTree as xml

sg.theme('BrightColors')
column1 = [
    [sg.Checkbox('Name & Surname', size=(20, 1), key="CB_N&S"), sg.InputText(size=(22, 1), key="IT_N&S")],
    [sg.Checkbox('Faculty', size=(20, 1), key="CB_Faculty"),
     sg.InputCombo(('Cybernetics', 'Mechmat'), size=(20, 1), key="IC_Faculty")],
    [sg.Checkbox('Department', size=(20, 1), key="CB_Department"),
     sg.InputCombo(('CS', 'PI', 'AM', 'SA', 'KM', 'Maths'), size=(20, 1), key="IC_Department")],
    [sg.Checkbox('Course', size=(20, 1), key="CB_Course"),
     sg.InputCombo(('1', '2', '3', '4'), size=(20, 1), key="IC_Course")],
    [sg.Checkbox('Mark', size=(20, 1), key="CB_Mark"),
     sg.InputCombo(('1', '2', '3', '4', '5'), size=(20, 1), key="IC_Mark")],
    [sg.Radio('DOM', "Radio1", size=(20, 1), key='R_DOM'), sg.Radio('SAX', "Radio1", default=True, key='R_SAX')],
    [sg.Button('Search', size=(20, 1), key='B_Search'), sg.Button('Convert to HTML', size=(21, 1), key='B_HTML')]
]

layout = [[sg.Column(column1), sg.Multiline(size=(50, 15), key='ML_SearchRes')]]
window = sg.Window('Everything bagel', layout, default_element_size=(50, 1), grab_anywhere=False)

# xml_file=Searcher.XML('myfile.xml')
while True:
    event, values = window.read()
    filter = {}
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == "B_Search":
        if values['CB_N&S']:
            filter['Name']=values['IT_N&S']
        if values['CB_Faculty']:
            filter['Faculty']=values['IC_Faculty']
        if values['CB_Department']:
            filter['Department']=values ['IC_Department']
        if values['CB_Course']:
            filter['Course']=values['IC_Course']
        if values ['CB_Mark']:
            filter['Mark']=values['IC_Mark']
        if values['R_DOM']:
            students = Searcher.search('myfile.xml', Searcher.DOM_Searcher(), filter)
            window['ML_SearchRes'].update('')
            for student in students:
                window['ML_SearchRes'].write('Name: '+student.Name_Surname+'\n')
                window['ML_SearchRes'].write('Faculty: '+student.Faculty+'\n')
                window['ML_SearchRes'].write('Department: '+student.Department+'\n')
                window['ML_SearchRes'].write('Course: '+student.Course+'\n')
                window['ML_SearchRes'].write('Mark: '+student.Mark+'\n\n')

        elif values['R_SAX']:
            students =Searcher.search('myfile.xml', Searcher.SAX_Searcher(),filter)
            window['ML_SearchRes'].update('')
            for student in students:
                window['ML_SearchRes'].write('Name: ' + student.Name_Surname + '\n')
                window['ML_SearchRes'].write('Faculty: ' + student.Faculty + '\n')
                window['ML_SearchRes'].write('Department: ' + student.Department + '\n')
                window['ML_SearchRes'].write('Course: ' + student.Course + '\n')
                window['ML_SearchRes'].write('Mark: ' + student.Mark + '\n\n')

    elif event == 'B_HTML':
        Searcher.transform()


window.close()

