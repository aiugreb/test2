#!/usr/bin/python3
"""Review module"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Create a new review based on baseModel"""

    place_id = ""
    user_id = ""
    text = ""
