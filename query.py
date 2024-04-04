import db
from db import Devices

def insert(mac,ip,files):
    
   

    device =  db.session.query(Devices).filter(Devices.MAC_address == mac).first()
    if(device == None):
        print("1 1 1 1 1 1 1 1 1 1 1 1 1 1 ")
        db.session.add(db.Devices(MAC_address=mac, IP_address=ip, Files=files))
    else:
        print("2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 ")
        user = db.session.merge(db.Devices(MAC_address=mac, IP_address=ip, Files=device.Files+files))
    db.session.commit()


print("here")
devices = db.session.query(db.Devices).all() 
for U in devices:
     print("here")
     print(U.MAC_address,U.Files,U.IP_address)

print("here ----  1")



#db.session.commit()


