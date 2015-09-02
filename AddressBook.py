from javax.swing import *
from java.awt import *
from javax.swing.table import DefaultTableModel
import json
import os
FILEPATH = 'C:\Users\PV02594\Desktop\data.json'
#ERRORCODES:
EXISTS = 0
SUCCESS = 1
#Messages:
ALREADYEXIST = "Contact Already Exist"
ADDSUCCESS = "Successfully Added"
class Contact(object):
 filepath = ""
 def __init__(self, filepath):
  self.filepath = filepath
  self.checkFile(filepath)
  return
  
 def checkFile(self, file_path):
  try:
    fp = open(file_path)
  except IOError:
    # If not exists, create the file
    fp = open(file_path, 'w+')
  fp.close()
  return
  
 def addContact(self, Name, Mobile, Email):
  data = {}
  #Name =  raw_input("Name : ")
  #Mobile = raw_input("Mobile : ")
  #Email = raw_input("Email : ")
  value = {'Mobile': Mobile, 'Email': Email}
  data[Name] = value
#Load previous json file
  with open(self.filepath) as f:
   try:
    if os.path.getsize(self.filepath) > 0:
	 jsondata = json.load(f)
	 #print jsondata
	 if Name not in jsondata:
	  jsondata.update(data)
	 else:
	  return EXISTS
    else:
     jsondata = data # For First Contact added
   finally:
    f.close()
   
  with open(self.filepath, 'w') as f:
   try:
    json.dump(jsondata, f, indent = 4, ensure_ascii=False) #sort_keys = True can add this 
    
   finally:
    f.close()
  return SUCCESS
  
 def readContact(self):
  table = []
  if os.path.getsize(self.filepath) > 0:
   result = json.loads(open(self.filepath).read())
   for i in result:
    temp = []
    temp.append(i)
    temp.append(result[i].get("Mobile"))
    temp.append(result[i].get("Email"))
    table.append(temp)   
  return table

class GUIContacts(Contact):
 tableData = []
 frame =  ""
 def __init__(self):
  super(GUIContacts, self).__init__(FILEPATH)
  self.frame = JFrame("Contacts")
  self.frame.setSize(800, 450)
  self.frame.setLayout(BorderLayout())
  self.frame.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE)
  self.listContacts()
  return
 
 
 def setText(self,event):
  self.addContacts()
  return
  
 def addText(self,event):
  result = super(GUIContacts, self).addContact(self.name.text, self.mobile.text, self.email.text)
  self.listContacts()
  if result:
   label = JLabel("<html><font color='green'>"+ADDSUCCESS+"</font></html>")
  else:
   label = JLabel("<html><font color='red'>"+ALREADYEXIST+"</font></html>")
  label.setFont(Font("Serif", Font.PLAIN, 16))
  self.frame.add(label, BorderLayout.SOUTH)
  return
  
 def addContacts(self):
  
  self.frame.getContentPane().removeAll()
  #self.frame.getContentPane().add(pnl)
  self.frame.setSize(800, 450)
  self.frame.setLayout(BorderLayout())
  pnl = JPanel()
  pnl.setPreferredSize(Dimension(200,100))
  self.frame.add(pnl)
  self.name = JTextField('Name',15)#actionPerformed=self.addText
  pnl.add(self.name)
  self.mobile = JTextField('Mobile', 10)
  pnl.add(self.mobile)
  self.email = JTextField('Email', 25)
  pnl.add(self.email)
  addButton = JButton('Save',actionPerformed=self.addText)
  pnl.add(addButton)
  self.frame.add(pnl, BorderLayout.CENTER)
  #self.frame.pack()
  self.frame.setVisible(True)
  return
  
 def listContacts(self):
  self.frame.getContentPane().removeAll()
  self.frame.setSize(800, 450)
  self.frame.setLayout(BorderLayout())
  self.tableData = super(GUIContacts, self).readContact()
  colNames = ('Name','Mobile','Email')
  dataModel = DefaultTableModel(self.tableData, colNames)
  self.table = JTable(dataModel)
  scrollPane = JScrollPane()
  scrollPane.setPreferredSize(Dimension(600,200))
  scrollPane.getViewport().setView((self.table))
  
  
  label = JLabel('Your Contacts')
  label.setFont(Font("Serif", Font.PLAIN, 24))
  label.setForeground(Color.BLUE)
  toppanel = JPanel()
  toppanel.add(label,BorderLayout.CENTER)
  
  panel = JPanel()
  panel.add(scrollPane)
  button = JButton('Add',actionPerformed=self.setText)
  button.setPreferredSize(Dimension(60, 20))
  
  panel.add(button,BorderLayout.EAST)
  
  self.frame.add(toppanel, BorderLayout.NORTH)
  #self.frame.add(button, BorderLayout.EAST)
  self.frame.add(panel, BorderLayout.CENTER)
  self.frame.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE)
  self.frame.setVisible(True)
  return
 
if __name__ == '__main__':
 s = GUIContacts()
