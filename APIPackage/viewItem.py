from flask import Blueprint,jsonify
from APIPackage.dbFunctionModule import selectqueryfunc


viewItem = Blueprint('viewItem', __name__)

@viewItem.route('/view/item/<string:name>')
def viewItemInventory(name):
    name = name.lower()
    select_query_item = """SELECT name, description, price, filename from items where name = ?"""
    item_tuple = (name,)
    result_item = selectqueryfunc(select_query_item,item_tuple)

    if len(result_item) > 0:
        fileurl = ""
        item = result_item[0]
        if item[3] != "" and item[3] != None:
            fileurl = "http://127.0.0.1:8000/file/" + item[3]
        return jsonify({'name': item[0], 'description': item[1],
                        'price': item[2], 'thumbnailurl': fileurl})
    else:
        return jsonify({'message': 'No item present in store inventory with this name'})