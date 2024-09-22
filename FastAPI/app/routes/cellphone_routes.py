"""Cellphone routes for the FastAPI application."""

from fastapi import APIRouter, Body, HTTPException
from models.cellphone_schema import CellphoneModel as CellphoneSchema
from database import CellphoneModel, CameraCellphone

cellphone_route = APIRouter()

@cellphone_route.post("/")
def create_cellphone(cellphone: CellphoneSchema = Body(...)):
    """Create a new cellphone."""
    CellphoneModel.create(
        imei=cellphone.imei,
        color=cellphone.color,
        brand=cellphone.brand,
        model=cellphone.model,
        portType=cellphone.portType,
        systemStorage=cellphone.systemStorage,
        ram=cellphone.ram,
        price=cellphone.price
    )
    for camera in cellphone.camera:
        CameraCellphone.create(
            camera=camera,
            cellphone=cellphone.imei
        )
    return {"message": "Cellphone created successfully"}

@cellphone_route.get("/")
def get_cellphones():
    """Retrieve all cellphones."""
    cellphones = CellphoneModel.select().where(CellphoneModel.imei > 0).dicts()
    return list(cellphones)

# pylint: disable=no-member
@cellphone_route.get("/{cellphone_imei}")
def get_cellphone(cellphone_imei: int):
    """Retrieve a specific cellphone by IMEI."""
    try:
        cellphone = CellphoneModel.get(CellphoneModel.imei == cellphone_imei)
        return cellphone
    except CellphoneModel.DoesNotExist as exc:
        raise HTTPException(status_code=404, detail="Cellphone doesn't exist") from exc

@cellphone_route.put("/{cellphone_imei}")
def update_cellphone(cellphone_imei: int, cellphone: CellphoneSchema = Body(...)):
    """Update an existing cellphone."""
    try:
        cellphone_update = CellphoneModel.get(CellphoneModel.imei == cellphone_imei)
        cellphone_update.color = cellphone.color
        cellphone_update.camera = cellphone.camera
        cellphone_update.brand = cellphone.brand
        cellphone_update.model = cellphone.model
        cellphone_update.portType = cellphone.portType
        cellphone_update.systemStorage = cellphone.systemStorage
        cellphone_update.ram = cellphone.ram
        cellphone_update.price = cellphone.price
        cellphone_update.save()
        return {"message": f"Cellphone with IMEI {cellphone_imei} updated"}
    except CellphoneModel.DoesNotExist as exc:
        raise HTTPException(status_code=404, detail="Failed to update") from exc

@cellphone_route.delete("/{cellphone_imei}")
def delete_cellphone(cellphone_imei: int):
    """Delete a cellphone by IMEI."""
    try:
        cellphone_camera = CameraCellphone.get(CameraCellphone.cellphone == cellphone_imei)
        cellphone_camera.delete_instance()
        cellphone = CellphoneModel.get(CellphoneModel.imei == cellphone_imei)
        cellphone.delete_instance()

        return {"message": f"Cellphone with IMEI {cellphone_imei} deleted"}
    except CellphoneModel.DoesNotExist as exc:
        raise HTTPException(status_code=404, detail="Cellphone not found") from exc
