from entity import *
from repository import *
from service import *

class Admin:
    def __init__(self):
        self.repo = PatiRepo()
        self.service = PatiService()

