#!/usr/bin/python3
"""City module"""
from models.base_model import BaseModel


class City(BaseModel):
    """Create a new city based on baseModel"""
    state_id = ""
    name = ""
