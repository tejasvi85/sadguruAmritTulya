from flask import Blueprint,request,jsonify
from APIPackage.dbFunctionModule import selectqueryfunc, insertqueryfunc, allowed_file


addItem = Blueprint('additem', __name__)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

@addItem.route('/additem', methods = ['POST'])
def addItemInventory():
    name = request.form['name'].lower()
    description = request.form['description'].lower()
    price = request.form['price']
    itemexist_select_query = """SELECT name from items where name = ?"""
    itemexist_tuple = (name,)
    itemexist_result = selectqueryfunc(itemexist_select_query,itemexist_tuple)

    if len(itemexist_result) > 0:
        return jsonify({'message': 'Item already present in store inventory'})

    else:
        if 'photo' in request.files:
            photo = request.files['photo']
            filename = photo.filename
            if len(filename) != 0 :
                filename = name
                if filename.find(' ') != -1:
                    filename = filename.replace(' ','')
                extension = '.' in photo.filename and photo.filename.rsplit('.', 1)[1].lower()
                filename = filename + '.' + extension

            if photo and allowed_file(photo.filename,ALLOWED_EXTENSIONS):
                readFile = photo.read()
            else:
                return jsonify({'message': 'Allowed file types are pdf, png, jpg, jpeg, gif'})

            additem_query = """ Insert INTO items (name, description, price, filename,  photo) 
                                        values (?,?,?,?,?)"""
            itemtuple = (name,description,price,filename,readFile)

        else:
            additem_query = """ Insert INTO items (name, description, price) 
                                                    values (?,?,?)"""
            itemtuple = (name, description, price)

        insertqueryfunc(additem_query,itemtuple)

        return jsonify({'message': 'Item added successfully'})