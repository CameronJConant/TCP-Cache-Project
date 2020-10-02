import urllib
import time
import logging

## THIS FILE GRABS THE SWEET PICTURE OF CAMERON IN A WIZARD HAT.
## ITS A GOOD PICTURE THAT SOMEONE MADE FOR ME AND I LOOK STYLISH.
## I WROTE THIS IN ALL CAPS IN ORDER TO BE READ EASIER, BUT I FEEL
## LIKE I'M YELLING.


##SETUP LOG TO BASIC CONFIG AND NAME IT 'wood.log' BECAUSE I'M A MAN OF
##REFINED TASTE IN PUNS
logging.basicConfig(filename='wood.log',level = logging.INFO)

##THIS FUNCTION IS CALLED AT THE END TO CREATE THE LOG AND FILL
##IT WITH THE NECESSARY DETAILS LIKE TIME TO PROCESS AND THE HEADER.
def createlog(T1, T2, T3, T4, header):
    Request = T2 - T1
    Process = T3 - T2
    Transfer = T4 - T3
    Total = T4 - T1

    logging.info('This is the header:\n %s', header[1])
    logging.info('Request time = %s \n', Request)
    logging.info('Process time = %s \n', Process)
    logging.info('Transfer time = %s \n', Transfer)
    logging.info('TOTAL TIME = %s \n\n', Total)
    size = os.path.getsize('picture.png')
    size = size/(1024**2)
    size = size/ total
    logging.info('MB over time = %s \n', size)

## CREATE A FILE TO OPEN UP THE URL
testfile = urllib.URLopener()

## GET THAT FILE AND SAVE IT FOREVER. ALSO RECORD THE T1 AND T4 EPOCH TIMES.

T1 = time.time()

header = urllib.urlretrieve("http://localhost:777/picture.png", "picture.png")

T4 = time.time()

## GRAB THE TEXT FILE FROM THE SERVER SO WE CAN GET T3 AND T4.

testfile.retrieve("http://localhost:777/times.txt", "times.txt")


## OPEN THE TIMES FILE UP AND PULL OUT THOSE VALUES
gettimes = open("times.txt")

readin = gettimes.readlines()
T2, T3 = readin[0].split(',')
T2.strip('\n')
T3.strip()
T2 = float(T2)
T3 = float(T3)

gettimes.close()

## CREATE THE LOG BY CALLING THE FUNCTION AND PLUGGING IN THAT GOOD STUFF
createlog(T1, T2, T3, T4, header)
print '\nDone'

