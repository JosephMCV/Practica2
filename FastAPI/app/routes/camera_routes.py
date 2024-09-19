from fastapi import APIRouter, Body, HTTPException
from models.cellphone_schema import Camera  as CameraSchema
from database import Camera

camera_route = APIRouter()

@camera_route.post("/")
def create_camera(camera: CameraSchema = Body(...)):
    Camera.create(id = camera.id, cameraModel = camera.cameraModel, resolution = camera.resolution
                        ,pixels = camera.pixels, zoom = camera.zoom, cameraMode = camera.camera_mode)
    return {"message": "Camera created successfully"}

@camera_route.get("/")
def get_camera():
    camera = Camera.select().where(Camera.id > 0).dicts()
    return list(camera)

@camera_route.get("/{camera_id}")
def get_camera(camera_id: int):
    try:
        camera = Camera.get(Camera.id == camera_id)
        return camera
    except Camera.DoesNotExist:
        raise HTTPException(status_code=404, detail="Camera does not exist")

@camera_route.put("/{id}")
def update_camera(id: int, camera: CameraSchema= Body(...)):
    try:
        camera_update = Camera.get(Camera.id == id)
        camera_update.cameraModel = camera.cameraModel
        camera_update.resolution = camera.resolution
        camera_update.pixels = camera.pixels
        camera_update.zoom = camera.zoom
        camera_update.zoom = camera.camera_mode

        camera_update.save()
        return {"message": f"{id} updated"}
    except Camera.DoesNotExist:
        raise HTTPException(status_code=404, detail="Failed to update")

@camera_route.delete("/{id}")
def delete_camera(id: int):
    try:
        camera = Camera.get(Camera.id == id)
        camera.delete_instance()
        return {"message": f"{id} deleted"}
    except Camera.DoesNotExist:
        raise HTTPException(status_code=404, detail="Book not found")
