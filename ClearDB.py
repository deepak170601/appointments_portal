import pymongo
client=pymongo.MongoClient("mongodb+srv://deepakreddy1431:Deepak961800@cluster0.cjcfynu.mongodb.net/?retryWrites=true&w=majority")
db=client["database"]
coll=db["faculty_schedule"]
coll.delete_many({})
coll=db["student_schedule"]
coll.delete_many({})
coll=db["slots_list"]
coll.delete_many({})
