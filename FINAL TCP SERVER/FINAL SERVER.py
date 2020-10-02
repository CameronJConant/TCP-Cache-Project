import SimpleHTTPServer
import SocketServer
from threading import Thread

##THIS SERVER SERVES UP FILES OUR CACHE DOESN'T HAVE

## CREATE OUR THREADED SERVER CLASS, WHICH IS JUST MAKING A NEW COPY OF THE CLASS THATS
## ALMOST THE SAME BUT WE CALL THE THREADINGMIXIN, WHICH IS BUILT IN BUT DISABLED BY DEFAULT
class ThreadedServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass

##CREATE A STANDARD HANDLER
Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

## MAKE OUR THREADED SERVER
http = ThreadedServer(("127.0.0.1", 888), Handler)

## INFORM USER AND MAKE SASSY COMMENT
print("Serving at port 888, not because you told me but because I want to.")

http.serve_forever()

## GET SERVED
