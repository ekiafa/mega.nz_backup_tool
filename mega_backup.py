
import os
from mega import Mega


global current_directory
global destination_directory
global email
global password
global list_of_files
path=None

def upload(list_of_files,path):
  
    mega = Mega({'verbose': True})
    m = mega.login(email,password)
    #print(path)
    for src in list_of_files:
      print(src)
      srcFile = current_directory + src
      if os.path.isfile( srcFile ):

        
        #folder=m.find(path)
        
        
        #uppedFile = m.upload(src,folder[0])
        #else:
        uppedFile = m.upload(src, None)
        
        
        
        print("Successful upload!")
        print ('Upped File Link: ' + m.get_upload_link( uppedFile ))
      else:
        print("There is no source file with this name.Please check your input.")



def main():

  global current_directory
  global destination_directory
  current_directory = os.getcwd() + os.path.sep #get path name of the working directory
 
  
  

  if len(list_of_files)>=1 and path!=None:
    upload(list_of_files,path)
  
  

if __name__ == '__main__':
  print("------------------------------------------Upload file Mega.nz tool-------------------------------------------------")
  email=input("Please insert your Mega's account email: ")
  password=input("Please insert your Mega's account password :")
  list_of_files=input("Please insert file names separated by spaces :").split(" ")
  path=input("Please insert your destination path in Mega's Cloud Drive :")
  main()
  
