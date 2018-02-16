from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from flask_cors import CORS, cross_origin
import config.MySQL as db

app = Flask(__name__)
api = Api(app)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('price')

PRODUCT=db.MySQL('products')

# shows a single product item and lets you delete a product item
class Product(Resource):
    def get(self, id):
        data=PRODUCT.get(id)
        if(not data):
           abort(404, msj="Element {} doesn't exist".format(id))
        return data
    def delete(self,id):
        PRODUCT.delete(id)
        return '', 205
    def put(self, id):
        args = parser.parse_args()
        query = """Update products set name='{}',price={} where id={};""".format(args['name'],args['price'],id)
        PRODUCT.put(query)
        return '', 201
# shows a list of all products, and lets you POST to add new products
class ProductList(Resource):
    def get(self):
        return PRODUCT.all()
    def post(self):
        args = parser.parse_args()
        query = """Insert into products (name,price) Values ('{}',{});""".format(args['name'],args['price'])
        PRODUCT.post(query)
        return {'message':'El producto ha sido actualizado'}, 201

##
## Actually setup the Api resource routing here
##
api.add_resource(ProductList, '/products')
api.add_resource(Product, '/products/<id>')
if __name__ == '__main__':
    app.run(debug=True,threaded=True)