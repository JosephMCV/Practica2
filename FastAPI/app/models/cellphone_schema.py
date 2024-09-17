from pydantic import BaseModel,Field,validator

class Camera(BaseModel):
    cameraModel:str
    resolution:str
    pixels:int
    zoom:float
    camera_mode:str

class Cellphone_model(BaseModel):
    
    imei:int 
    color:str
    camera:Camera
    brand:str
    model:str
    port_type:str
    system_storage:float
    ram:int
    price:int

    @validator("model")
    def model_must_be_above_8(cls,v):
        if v < "8":
            raise ValueError("Cellphone version must be above 8")
        return v
    
    @validator("ram")
    def minimun_of_ram(cls,v):
        if v >= 3:
            raise ValueError("Ram must be 3 or superior in order for start the software")
        return v