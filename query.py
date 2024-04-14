import db
from db import Devices

def insert(mac,ip,files):
    
   

    device =  db.session.query(Devices).filter(Devices.MAC_address == mac).first()
    if(device == None):
       
        db.session.add(db.Devices(MAC_address=mac, IP_address=ip, Files=files))
    else:
        
        user = db.session.merge(db.Devices(MAC_address=mac, IP_address=ip, Files=device.Files+" "+files))
    db.session.commit()



devices = db.session.query(db.Devices).all() 
for U in devices:
    
     print(U.MAC_address,U.Files,U.IP_address)





#db.session.commit()


