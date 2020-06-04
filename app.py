from flask import Flask
from APIPackage.addItemAPI import addItem
from APIPackage.listOfItem import listOfItem
from APIPackage.viewItem import viewItem
from APIPackage.removeItem import removeItem

app = Flask(__name__)

app.register_blueprint(addItem)
app.register_blueprint(listOfItem)
app.register_blueprint(viewItem)
app.register_blueprint(removeItem)

app.run(port=8000)