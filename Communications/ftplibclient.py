
from ftplib import FTP
from threading import Thread


class FTPLibClient(Thread):
    
    def __init__(self, host, port, user, passwd, timeout):
        Thread.__init__()
        self._host = host
        self._port = port
        self._timeout = timeout
        self._user = user
        self._passwd = passwd
    
    
    def login(self):
        
        try:
           
            self.__connector = FTP()
            self.__connector.connect(host = self._host, port = self._port, timeout=self._timeout)
            self.__connector.login(user=self._user, passwd = self._passwd)
            return True
        except Exception as err: 
            #call error Handling
            print('Error on FTP Login: %s'%(err)) 
            return False
              
   
    def change_dir(self,dirname):    
        
        try:    
            self.__connector.cwd(dirname)
            return True
        except Exception as err:
            print('Error on FTP change dir: %s'%(err))
            return False       
        
   
    def store_file(self,dest_filename, filedata):
        
        try:
            self.__connector.storbinary("STOR "+dest_filename, filedata)
            return True
        except Exception as err:
            print('FTP transfer error: %s'%(err))
            return False
        

if(__name__ == '__main__'):
    from time import sleep
    connection_params = {'host':'',
                         'port':'number',
                         'user':'',
                         'password':'',
                         'dir':'',
                         'timeout': 10,
                         'retry':3,
                         'forcezip':True}

    print(connection_params)
    
    ftpclient = FTPLibClient(connection_params['host'], connection_params['port'], connection_params['user'], connection_params['password'],connection_params['timeout'])
    print(ftpclient.login())
    print(ftpclient.change_dir(connection_params['dir']))
    sleep(5)
    with open('file',"rb") as file:
        print(ftpclient.store_file('dfsd.txt', file))
        file.close()
        