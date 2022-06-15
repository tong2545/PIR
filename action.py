from tn import Con
c = Con

class Action:
    def gettn():
        data = c.gettn()
        return data
    
    def update_tn(id,status):
        data= c.update_tn(id,status)
        return data
    
    def delete_tn(name):
        x = c.delete_tn(name)
        if(x == True):
            data = {"error":False}
        else:
            data = {"error":True}
            
        return data
    
    def select_tn(id):
        data= c.select_tn(id)
        return data
    
    def update_tn(id,status):
        t = c.update_tn(id,status)
        if(t == True):
           data = c.getbyid(id)
        else:
            data={"error": True} 
        return data
    
    def insert_tn(name,hardware):
        id = c.insert_tn(name,hardware)
        if(id):
            data=c.getbyid(id)
        else:
            data={"error": True} 
        return data
    
    