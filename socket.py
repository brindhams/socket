
import socket			


s = socket.socket()		
print ("Socket successfully created")


port = 12345				



s.bind(('', port))		
print ("socket binded to %s" %(port))


s.listen(5)	
print ("socket is listening")			


while True:
    conn, addr = s.accept()	
    print ('Got connection from', addr )
    conn.send('Thank you for connecting')
    conn.close()


