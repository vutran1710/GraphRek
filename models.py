""" Pydantic Models for data modelling & verifcation
"""
from typing import List
from pydantic import BaseModel


class GetKeysPayload(BaseModel):
    """ Demo api
    """
    data: List[str]


class TokenPayload(BaseModel):
    """ Nope
    """
    user_id: int = None


class TokenModel(BaseModel):
    """ Nope
    """
    access_token: str
    token_type: str


class PostMeta(BaseModel):
    """ PostMeta model
    """
    id: str
    score: int
