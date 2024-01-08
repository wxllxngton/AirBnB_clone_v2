#!/usr/bin/python3
""" Amenity Module for BnB v2 clone project """
import os
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String

from models.base_model import BaseModel, Base


class Amenity(BaseModel, Base):
    """Represents the amenity data set."""

    __tablename__ = "amenities"
    __table_args__ = {"extend_existing": True}
    name = (
        Column(String(128), nullable=False)
        if os.getenv("HBNB_TYPE_STORAGE") == "db"
        else ""
    )
