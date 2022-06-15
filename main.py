from fastapi import FastAPI
import uvicorn
from action import Action
app = FastAPI()


@app.get("/")
def read_root():
    return {"kuy": ""}

@app.get("/gethw")
def gethw():
    data = Action.gettn()
    return data

@app.get("/geth")
def geth(id,status):
    data = Action.update_tn(id,status)
    return data

@app.get("/gethh")
def gethh(id):
    data = Action.delete_tn(id)
    return data

@app.get("/getkk")
def getkk(id):
    data = Action.select_tn(id)
    return data

@app.get("/input_name")
def input_name(name):
    data = name
    return data

@app.get("/input_name_2")
def input_name2(name,last_name):
    data = "{} {}".format(name,last_name)
    return data

@app.get("/R")
def R(R1,R2,R3):
    R = ((1/float(R1))+(1/float(R2))+(1/float(R3)))**-1
    data = " R = {:.2f}".format(R)
    return data

@app.get("/update_hw_id")
def update_hw_id(id,status) :
    data = Action.update_tn(id,status)
    return data

@app.get("/getbyid")
def getbyid(name,hardware):
    data = Action.insert_tn(name,hardware)
    return data

@app.get("/inserthw")
def inserthw(name,hardware):
    data = Action.insert_tn(name,hardware)
    return data

@app.get("/deletehw")
def deletehw(name):
    data = Action.delete_tn(name)
    return data

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
