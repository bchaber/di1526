from redis import Redis
db = Redis("redis")
db.flushall()
db.set("user:bach", "haslo")
db.set("user:john", "snow")
db.set("user:bob",  "bob")
for i in range(1,30):
    db.set(f"user:user{i}", "pass")
self.db.lpush("posts:bach" , "To jest sekret!")
