from BasicWebCrawler import item41
from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps

app = Flask(__name__)
api = Api(app)

class Item42(Resource) :
    def get(self) :
        logoList = []
        companyList = item41()
        for company in companyList :
            data = {}
            data['logo'] = 'https://theinternship.io/' + company[1]
            logoList.append(data)
        logoJSON = {}
        logoJSON['companies'] = logoList
        return dumps(logoJSON, indent=1)

api.add_resource(Item42, '/companies')
app.run()