
from pprint import pprint
import os
from flask import Flask, render_template,request,redirect,url_for,jsonify,json # For flask implementation
from flask_pymongo import PyMongo
# from flask import Flask,render_template,jsonify,json,request

app = Flask(__name__)

#resource_path = os.path.join(app.root_path, 'flaskmongoCRUD')
app.config['MONGO_DBNAME'] = 'ServerInventoryDB'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/ServerInventoryDB'

mongo = PyMongo(app)


@app.route("/ServerInventoryTool/index")
def page_loading():
	return render_template('listSites.html')


@app.route("/ServerInventoryTool/bulkAddition")
def bulk_site_insertion():

	servers = mongo.db.server_details

	with open('Config.json') as json_data_file:
   		data = json.load(json_data_file)
   	
		for sites in data["Sites"]:
			
			serverData = json.load(open('/Users/sreekanth/Documents/Sreekanth-Projects/ServerInventoryTool/ServerData/'+sites+'-details.json'))
			
			#for j in serverData:
			for x in range(0,4):
				for y in range(0,4):

					servers.insert({
						"sitename":serverData['siteName'],
						"sitetype":serverData['siteType'],
						"location":serverData['location'],
						"status":serverData['active'],
						"type":serverData['servers'][y]['type'],
						"name":serverData['servers'][y]['names'][x]
					})
	return jsonify(status='OK',message='inserted successfully')

# @app.route("/ServerInventoryTool/getAllSites")
# def display_all_sites():

									

				

if __name__ == '__main__':
    app.run(debug=True)

	