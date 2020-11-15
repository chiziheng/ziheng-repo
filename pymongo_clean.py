import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["kindle_metadata"]
mycol = mydb["kindle_metadata_origin"]
mycol_origin = mydb["meta_Kindle_Store"]

def update(x):
  myquery = { "asin": x['asin'] }
  # print(x['asin'])
  title = mycol_origin.find({'asin':x['asin']})[0]['title']
  newvalues = { "$set": { "title": x['title']} }
  mycol.update_one(myquery, newvalues, upsert=True)

i=0
ls_failed=[]
for documents in mycol.find({"title":{"$exists":False}}):
  try:
    update(documents)
    print(documents['asin'], 'inserted')
  except:
    print('cannot find record', documents['asin'])
    ls_failed.append(documents['asin'])

  i+=1
  print('finish record', i)
