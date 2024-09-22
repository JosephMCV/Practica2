"""Camera routes for the FastAPI application."""

from fastapi import APIRouter, Body, HTTPException
from models.cellphone_schema import Camera as CameraSchema
from database import Camera,CameraCellphone

camera_route = APIRouter()

@camera_route.post("/")
def create_camera(camera: CameraSchema = Body(...)):
    """Create a new camera."""
    Camera.create(
        id=camera.id,
        cameraModel=camera.cameraModel,
        resolution=camera.resolution,
        pixels=camera.pixels,
        zoom=camera.zoom,
        cameraMode=camera.cameraMode
    )
    return {"message": "Camera created successfully"}

@camera_route.get("/")
def get_cameras():
    """Retrieve all cameras."""
    cameras = Camera.select().where(Camera.id > 0).dicts()
    return list(cameras)

# pylint: disable=no-member
@camera_route.get("/{camera_id}")
def get_camera(camera_id: int):
    """Retrieve a specific camera by ID."""
    try:
        camera = Camera.get(Camera.id == camera_id)
        return camera
    except Camera.DoesNotExist as exc:
        raise HTTPException(status_code=404, detail="Camera does not exist") from exc

@camera_route.put("/{camera_id}")
def update_camera(camera_id: int, camera: CameraSchema = Body(...)):
    """Update an existing camera."""
    try:
        camera_update = Camera.get(Camera.id == camera_id)
        camera_update.cameraModel = camera.cameraModel
        camera_update.resolution = camera.resolution
        camera_update.pixels = camera.pixels
        camera_update.zoom = camera.zoom
        camera_update.cameraMode = camera.cameraMode

        camera_update.save()
        return {"message": f"Camera with ID {camera_id} updated"}
    except Camera.DoesNotExist as exc:
        raise HTTPException(status_code=404, detail="Failed to update") from exc

@camera_route.delete("/{camera_id}")
def delete_camera(camera_id: int):
    """Delete a camera by ID."""
    try:
        cellphone_camera = CameraCellphone.get(CameraCellphone.camera == camera_id)
        cellphone_camera.delete_instance()
        camera = Camera.get(Camera.id == camera_id)
        camera.delete_instance()
        return {"message": f"Camera with ID {camera_id} deleted"}
    except Camera.DoesNotExist as exc:
        raise HTTPException(status_code=404, detail="Camera not found") from exc
    