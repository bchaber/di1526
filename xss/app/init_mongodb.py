import pymongo
db = pymongo.MongoClient("mongodb://root:root@mongodb").db
db.counters.remove({})
db.counters.insert({"name":"posts","value":0})
db.user.remove({})
db.user.insert({'username':'bach', 'password':'haslo'})
db.user.insert({'username':'john', 'password':'snow'})
db.user.insert({'username':'bob',  'password':'bob'})
for i in range(1,30):
  db.user.insert({'username':f'user{i}',  'password':'pass'})
db.session.remove({})
db.session.insert({'sid':'deadbeef', 'username':'bach'})
db.posts.remove({})
db.posts.insert({'username':'bob', 'post':'To jest sekret!', 'id':1})

for u in db.user.find():
  print(u)
