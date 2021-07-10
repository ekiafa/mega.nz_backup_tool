
import os
from mega import Mega


global current_directory
global email
global password
global list_of_files

def upload(list_of_files,destination_folder):
  
    mega = Mega({'verbose': True})
    m = mega.login(email,password)
    for src in list_of_files:
      srcFile = current_directory + src
      if os.path.isfile( srcFile ):

        if destination_folder==None:
          uppedFile = m.upload(srcFile,None)
        else:
          folder=m.find(destination_folder)        
          uppedFile = m.upload(srcFile,folder[0])
        
        print("Successful upload!")
        print ('Upped File Link: ' + m.get_upload_link( uppedFile ))
      else:
        print("There is no source file with this name.Please check your input.")



def main():

  global current_directory
  global destination_directory
  current_directory = os.getcwd() + os.path.sep #get path name of the working directory
 
  
  if len(list_of_files)>=1:
    upload(list_of_files,destination_folder)
  
  

if __name__ == '__main__':
  print("------------------------------------------Upload file Mega.nz tool-------------------------------------------------")
  email=input("Please insert your Mega's account email: ")
  password=input("Please insert your Mega's account password :")
  list_of_files=input("Please insert file names separated by spaces :").split(" ")
  destination_folder=input("Please insert your destination folder in Mega's Cloud Drive :")
  main()
  
