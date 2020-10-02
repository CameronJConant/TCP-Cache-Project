import SimpleHTTPServer
import SocketServer
import time
import os
import urllib
from threading import Thread

## THIS IS A CACHE. IT WORKS BY REWRITING THE DO_GET FUNCTION WITHIN
## SIMPLEHTTPSERVER SO WE CAN DO WITH IT WHAT WE WANT.
## WHAT WE WANT TO DO IS CHECK THE LOCAL FILEPATH TO SEE IF WE HAVE
## A FILE WITH THE REQUESTED NAME. IF WE DO, SEND IT. IF NOT, WE GO GET IT.

## THIS IS OUR NEW HTTP REQUEST HANDLER CLASS.
class CacheHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    ## WHEN A DO_GET IS CALLED, OUR NEW FUNCTION IS CALLED INSTEAD OF THE ORIGINAL
    ## WE WILL KEEP TIMES AND SAVE THEM TO THEIR OWN FILE TO BE ACCESSED AT A LATER TIME.
    def do_GET(self):
        T2 = time.time()
        ## CLEAN UP THE PATH FOR OUR OWN USE
        filename = self.path
        filename = filename.strip('/')
        ## IF WE ALREADY HAVE THAT FILE JUST GO STRAIGHT TO SENDING IT.
        ## OTHERWISE, GO GET IT FROM THE CORE SERVER AT PORT 888
        if os.path.exists(filename):
            print("We got that file, yo")
        else:
            print("I gotta grab that file yo")
            data = urllib.URLopener()
            header = data.retrieve("http://localhost:888/" + filename , filename)
            print(header[1])
        ## SEND THE FILE
        T3 = time.time()
        thefile = self.send_head()
        self.copyfile(thefile, self.wfile)
        if thefile:
            thefile.close()
        ## WRITE THE TIMES TO A TXT FILE
        f = open('times.txt', 'w')
        f.write(str(T2)+ ',' + str(T3))
        print(str(T2) + '\n' + str(T3))
        f.close()

## IN ORDER TO THREAD WITH SOCKETSERVER, WE CAN MAKE A NEW CLASS FROM SOCKETSERVER/TCPSERVER
## BUT WE ADD IN THE LINE "THREADINGMIXIN". THIS IS A PART OF SOCKET SERVER AND WE
## JUST HAVE TO MANUALLY INITIATE IT.
class ThreadedServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass

## MAKE OUR HANDLE BASED OFF OF OUR CACHEHANDLER
## CREATE OUR THREADED SERVER CLASS AND MAKE IT SERVE.
handle = CacheHandler
http = ThreadedServer(("127.0.0.1", 777), handle)
print("Serving at port 777, your majesty!")
http.serve_forever()

## THATS HOW YOU GOT SERVED
