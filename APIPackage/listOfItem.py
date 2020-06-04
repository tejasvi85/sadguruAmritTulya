from flask import Blueprint,jsonify,send_file
from APIPackage.dbFunctionModule import selectqueryfunc
from io import BytesIO

listOfItem = Blueprint('listOfItem', __name__)

@listOfItem.route('/list/item')
def listOfItemInventory():
    select_query_item = """SELECT name , price, filename from items"""
    result_item = selectqueryfunc(select_query_item)

    item_list = []

    if len(result_item) > 0:
        for i in result_item:
            fileurl=""
            if i[2] != "" and i[2] != None:
                fileurl="http://127.0.0.1:8000/file/"+i[2]
            item_list.append({'name': i[0], 'price': i[1], 'thumbnailurl': fileurl})
        return jsonify({'list of items': item_list})
    else:
        return jsonify({'message': 'No item present in store inventory'})

@listOfItem.route('/file/<string:filename>')
def getFileFromUrl(filename):
    select_query = "select photo from items where filename = ?"
    filenametuple=(filename,)
    result_image = selectqueryfunc(select_query,filenametuple)
    result_image_1 = result_image[0][0]

    if result_image_1 == None:
        resp = jsonify({'message': 'No photo uploaded for this item'})
        resp.status_code = 404
        return resp
    else:
        return send_file(BytesIO(result_image_1), attachment_filename=filename)