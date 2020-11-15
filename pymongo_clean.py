import pymongo
myclient = pymongo.MongoClient("mongodb://35.174.211.255:27017/")
mydb = myclient["kindle_metadata"]
mycol = mydb["kindle_metadata_origin"]
mycol_origin = mydb["meta_Kindle_Store"]

def update(x):
  myquery = { "asin": x['asin'] }
  newvalues = { "$set": { "title": x['title']} }
  mycol.update_one(myquery, newvalues, upsert=True)

for documents in mycol_origin.find():
  # print(documents['title'])
   update(documents)
   print('finish one')
