###########################################################

#Execution: python3 mega_backup.py <name of files> <path>

###########################################################
import sys,os,time
from mega import Mega


global current_directory
global destination_directory
global email
global password
global list_of_files
def upload(list_of_files,path):
  
    mega = Mega({'verbose': True})
    m = mega.login(email,password)
  
    for src in list_of_files:
      srcFile = current_directory + src
      if os.path.isfile( srcFile ):

        
        destination_directory=m.find(path)
        #print (destination_directory)
        uppedFile = m.upload(srcFile, destination_directory)
        
        print("Successful upload!")
        print ('Upped File Link: ' + m.get_upload_link( uppedFile ))



def main():

  global current_directory
  global destination_directory
  current_directory = os.getcwd() + os.path.sep #et path name of the working directory
  destination_directory = None
  
  if len(list_of_files)>=1 and path!=None:
    upload(list_of_files,path)
  
  

if __name__ == '__main__':
  print("------------------------------------------Upload file Mega.nz tool-------------------------------------------------")
  email=input("Please insert your Mega's account email: ")
  password=input("Please insert your Mega's account password :")
  list_of_files=input("Please insert file names separated by spaces :")
  path=input("Please insert your destination path in Mega's Cloud Drive :")
  main()
  
