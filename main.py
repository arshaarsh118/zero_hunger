from flask import*
from public import public
from farmer import farmer
from shelter import shelter
from distributor import distributor
from admin import admin

app=Flask(__name__)

app.secret_key="bhlaaaablaa"
app.register_blueprint(public)
app.register_blueprint(farmer)
app.register_blueprint(shelter)
app.register_blueprint(distributor)
app.register_blueprint(admin)

app.run(debug=True)