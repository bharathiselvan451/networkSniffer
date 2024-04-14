import db
from db import Devices

def insert(d_name,vendour,mac,ip,name):
    
   

    device =  db.session.query(Devices).filter(Devices.MAC_address == mac).first()
    if(device == None):
       
        db.session.add(db.Devices(MAC_address=mac, IP_address=ip, Device_name=d_name, vendour = vendour,File_name= name ))
    else:
        
        user = db.session.merge(db.Devices(MAC_address=mac, IP_address=ip, Device_name=d_name, vendour = vendour,File_name= device.File_name+" "+name))
    db.session.commit()

def search(mac):
    device =  db.session.query(Devices).filter(Devices.MAC_address == mac).first()
    if(device == None):
        
        return True
    else:
        
        return False
    
def search_device(mac):
    device =  db.session.query(Devices).filter(Devices.MAC_address == mac).first()
    return device

def all():
    devices = db.session.query(db.Devices).all()
    return devices


devices = db.session.query(db.Devices).all() 






#db.session.commit()


