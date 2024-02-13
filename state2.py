#!/usr/bin/python3
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

storage = FileStorage()
b_m = BaseModel()
all_objs = storage.all()
print("**********before", all_objs)
storage.new(b_m)
storage.save()
print("######## after", all_objs)
storage.reload()
print("---------------", all_objs)
_class = globals()[val['__class__']]
