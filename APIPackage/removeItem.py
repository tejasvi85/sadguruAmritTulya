from flask import Blueprint, jsonify
from APIPackage.dbFunctionModule import deletequeryfunc, selectqueryfunc

removeItem = Blueprint('removeItem', __name__)


@removeItem.route('/remove/item/<string:name>')
def removeItemInventory(name):
    name = name.lower()
    select_query_item = """SELECT name from items where name = ?"""
    item_tuple = (name,)
    result_item = selectqueryfunc(select_query_item, item_tuple)

    if len(result_item) > 0:
        delete_query_item = """Delete from items where name = ?"""
        item_tuple = (name,)
        deletequeryfunc(delete_query_item, item_tuple)
        return jsonify({'message': 'Item removed successfully from inventory'})

    else:
        return jsonify({'message': 'No such item present in inventory to remove'})
