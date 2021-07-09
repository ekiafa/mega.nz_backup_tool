###########################################################

#Execution: python3 mega_backup.py <name of files> <path>

###########################################################
import sys,os,time
from mega import Mega


global current_directory
global destination_directory

def upload(list_of_files,path):
  
    mega = Mega({'verbose': True})
    m = mega.login('eftihiakf@yahoo.gr', 'noinfneeded')
  
    for src in list_of_files:
      srcFile = current_directory + src
      if os.path.isfile( srcFile ):

        #print (srcFile)
        destination_directory=m.find(path)
        #print (destination_directory)
        uppedFile = m.upload(srcFile, destination_directory)
        print (uppedFile)
        print ('Upped File Link: ' + m.get_upload_link( uppedFile ))



def main():

  
  list_of_files=sys.argv[1:-1]
  path=sys.argv[-1]
  global current_directory
  global destination_directory
  current_directory = os.getcwd() + os.path.sep #et path name of the working directory
  destination_directory = None
  
  if len(list_of_files)>=1 and path!=None:
    upload(list_of_files,path)
  
  

if __name__ == '__main__':
  
  main()
  
