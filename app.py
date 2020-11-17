from flask import Flask, jsonify, request

app = Flask(__name__)

from products import products

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({"message": "Pong"})

@app.route('/products', methods=['GET'])
def getProducts():
    return jsonify({"products": products, "message": "Product List"})

@app.route('/products/<string:product_name>', methods=['GET'])
def getProduct(product_name):
    productsFound = [product for product in products if product['name'] == product_name]
    if (len(productsFound)> 0):
        return jsonify({'product': productsFound[0]})
    return jsonify({"message": "Product not found"})

@app.route('/products', methods=['POST'])
def addProducts():
    new_products = {
        "name": request.json['name'],
        "price": request.json['price'],
        "quantity": request.json['quantity']
    }
    products.append(new_products)
    return jsonify({"message": "Product add succesfull", "products": products})


@app.route('/products/<string:product_name>', methods=['PUT'])
def editProducts(product_name):
    productFound= [product for product in products if product["name"] == product_name]
    if (len(productFound) > 0):
        productFound[0]['name'] = request.json['name']
        productFound[0]['price'] = request.json['price']
        productFound[0]['quantity'] = request.json['quantity']
        
        return jsonify({
            "message": "Product Updated",
            "product": productFound
        })
        
    return jsonify({"message": "Product not found"})
    
    
@app.route('/products/<string:product_name>', methods=['DELETE'])
def deleteProducts(product_name):
    productFound= [product for product in products if product["name"] == product_name]
    if (len(productFound) > 0):
        products.remove(productFound[0])
        return jsonify({
            "Message": "Product Deleted",
            "products": products
        })
    return jsonify({"mesasge": "Product not found"})
    


if __name__ == "__main__":
    app.run(debug=True, port=4000)