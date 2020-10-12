from fastapi import FastAPI
from src.beans.ProductData import ProductData
from src.mongo_db_client.mongo_db_client import MongoDBClient

MDClient = MongoDBClient()

app = FastAPI()


@app.get('/')
def index():
    return {'key': 'value'}


@app.post('/{ProductData.name}')
def new_product(prod: ProductData):
    MDClient.Collection.insert_one(prod.dict())
    return prod.dict()


@app.get('/{product.name}')
def get_product():
    product = MDClient.Collection.find({},{'_id':0,'name':1,'image':1,'price':1,'description':1})
    result = [i for i in product]
    return result

