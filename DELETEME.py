from models.base_model import BaseModel
n = {'Name': 'test'}
new = BaseModel(**n)
print(new.Name)