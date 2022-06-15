
from fastapi import FastAPI
import uvicorn
app = FastAPI()

from action import Action
a = Action

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/my_name")
def name():
    data = 'Peerawat Jaitaeng'
    return data

@app.get("/input_name")
def input_name(name):
    data = name
    return data

@app.get("/input_name_2")
def input_name(name,last_name):
    data = "{} {}".format(name,last_name)
    return data
    
@app.get("/speed")
def speed(s,t):
    v = float(s)/float(t)
    data = 'v = {:.0f}'.format(v)
    return data

@app.get("/rt")
def rt(r1,r2,r3):
    r_rt=float(r1)+float(r2)+float(r3)
    s_rt=(1/float(r1)+1/float(r2)+1/float(r3))**-1
    data = "อนุกรม = {} ขนาน = {:.2f}".format(r_rt,s_rt)
    return data

@app.get("/gethw")
def get_hw():
    data = a.gethw()
    return data


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)


