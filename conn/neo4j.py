"""Redis module
"""
from decorator import singleton


@singleton
class NeoClient:
    """ Neo4J DB Client
    """
    def __init__(self):
        pass
