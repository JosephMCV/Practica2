from typing import List
from pydantic import BaseModel,Field,validator

class Camera(BaseModel):
    id: int
    cameraModel:str
    resolution:str
    pixels:int
    zoom:float
    camera_mode:str

class Cellphone_model(BaseModel):
    
    imei:int 
    color:str
    camera:List[int]
    brand:str
    model:str
    port_type:str
    system_storage:float
    ram:int
    price:int

    @validator("price")
    def minimun_of_ram(cls,v):
        if v <= 0:
            raise ValueError("The price cant be 0 or below")
        return v
    
    @validator("ram")
    def minimun_of_ram(cls,v):
        if v <= 3:
            raise ValueError("Ram must be 3 or superior in order for start the software")
        return v