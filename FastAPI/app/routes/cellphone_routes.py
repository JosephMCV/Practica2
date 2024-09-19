from fastapi import APIRouter, Body
from models.cellphone_schema import Cellphone_model  as CellphoneSchema
from database import Cellphone_model,Camera_Cellphone

cellphone_route = APIRouter()

@cellphone_route.post("/")
def create_cellphone(cellphone: CellphoneSchema = Body(...)):
   
    Cellphone_model.create(imei=cellphone.imei,
                                color=cellphone.color,
                                brand = cellphone.brand,
                                model = cellphone.model,
                                port_type = cellphone.port_type,
                                system_storage = cellphone.system_storage,
                                ram = cellphone.ram,
                                price = cellphone.price
                                )
    for i in cellphone.camera:
        Camera_Cellphone.create(
            camera = i,
            cellphone = cellphone.imei
        )
    return {"message": "cellphone created successfully"}
    
@cellphone_route.get("/")
def get_cellphone():
    cellphone = Cellphone_model.select().where(Cellphone_model.imei > 0).dicts()
    return list(cellphone)

@cellphone_route.get("/{cellphone_imei}")
def get_cellphone(cellphone_imei: int):
    try:
        cellphone = Cellphone_model.get(Cellphone_model.imei == cellphone_imei)
        return cellphone
    except Cellphone_model.DoesNotExist:
        return {"error": "Cellphone doesn´t exist"}
    
@cellphone_route.put("/{imei}")
def update_cellphone(imei: int, cellphone: CellphoneSchema = Body(...)):
    try:
        cellphone_update = Cellphone_model.get(Cellphone_model.id == id)
        cellphone_update.color = cellphone.color
        cellphone_update.camera = cellphone.camera
        cellphone_update.brand= cellphone.brand
        cellphone_update.model = cellphone.model
        cellphone_update.port_type = cellphone.port_type
        cellphone_update.system_storage = cellphone.system_storage
        cellphone_update.ram = cellphone.ram
        cellphone_update.price = cellphone.price
        cellphone_update.save() 
        return {"message": "{imei} updated"}
    except Cellphone_model.DoesNotExist:
        return {"error": "Failed to update"}

@cellphone_route.delete("/{imei}")
def delete_cellphone(imei: int):
    try:
        cellphone = Cellphone_model.get(Cellphone_model.imei == imei)
        cellphone.delete_instance()
        return {"message": f"{imei} eliminated"}
    except Cellphone_model.DoesNotExist:
        return {"error": "Cellphone not found"}
