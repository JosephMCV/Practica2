"""
Schema models for cellphones and cameras using Pydantic.
"""

from typing import List
from pydantic import BaseModel, validator

class Camera(BaseModel):
    """
    Represents a camera with attributes such as model, resolution, pixels, zoom, and mode.
    """
    id: int
    cameraModel:str
    resolution:str
    pixels:int
    zoom:float
    cameraMode:str

class CellphoneModel(BaseModel):
    """
    Represents a cellphone with various attributes such as IMEI, color, camera, brand, etc.
    """
    imei:int
    color:str
    camera:List[int]
    brand:str
    model:str
    portType:str
    systemStorage:float
    ram:int
    price:int

    @validator("price")
    def minimun_of_price(cls,v):  # pylint: disable=no-self-argument
        """
        Validates that the price is greater than zero.
        
        Args:
        v (int): The price of the cellphone.

        Returns:
            int: The validated price.
        
        Raises:
            ValueError: If the price is zero or below.
        """
        if v <= 0:
            raise ValueError("The price can't be 0 or below")
        return v

    @validator("ram")
    def minimun_of_ram(cls,v):  # pylint: disable=no-self-argument
        """
        Validates that the RAM is at least 3GB.
        
        Args:
        v (int): The amount of RAM in GB.

        Returns:
            int: The validated RAM.
        
        Raises:
            ValueError: If the RAM is less than 3GB.
        """
        if v <= 3:
            raise ValueError("RAM must be 3GB or more to start the software")
        return v
    