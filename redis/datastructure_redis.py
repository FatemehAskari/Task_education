import redis


# list
r = redis.StrictRedis(host='127.0.0.1',port='6379',db=0)

res1 = r.lpush("bikes:repairs", "bike:1")
print(res1)  # >>> 1

res2 = r.lpush("bikes:repairs", "bike:2")
print(res2)  # >>> 2

res3 = r.rpop("bikes:repairs")
print(res3)  # >>> b'bike:2'

res4 = r.rpop("bikes:repairs")
print(res4)  # >>> b'bike:1'


# set

res1 = r.sadd("bikes:racing:france", "bike:1")
print(res1)  # >>> 1

res2 = r.sadd("bikes:racing:france", "bike:1")
print(res2)  # >>> 0

res3 = r.sadd("bikes:racing:france", "bike:2", "bike:3")
print(res3)  # >>> 2

res4 = r.sadd("bikes:racing:usa", "bike:1", "bike:4")
print(res4)  # >>> 2


res1 = r.hset(
    "bike:1",
    mapping={
        "model": "Deimos",
        "brand": "Ergonom",
        "type": "Enduro bikes",
        "price": 4972,
    },
)
print(res1)
# >>> 4

res2 = r.hget("bike:1", "model")
print(res2)
# >>> 'Deimos'

res3 = r.hget("bike:1", "price")
print(res3)
# >>> '4972'

res4 = r.hgetall("bike:1")
print(res4)
# >>> {'model': 'Deimos', 'brand': 'Ergonom', 'type': 'Enduro bikes', 'price': '4972'}

# sortset
res1 = r.zadd("racer_scores", {"Norem": 10})
print(res1)  # >>> 1

res2 = r.zadd("racer_scores", {"Castilla": 12})
print(res2)  # >>> 1

res3 = r.zadd(
    "racer_scores",
    {"Sam-Bodden": 8, "Royce": 10, "Ford": 6, "Prickett": 14, "Castilla": 12},
)
print(res3)  # >>> 4

# geospatial
res1 = r.geoadd("bikes:rentable4", [-122.27652, 37.805186, "station:1"])
print(res1)  # >>> 1

res2 = r.geoadd("bikes:rentable4", [-122.2674626, 37.8062344, "station:2"])
print(res2)  # >>> 1

res3 = r.geoadd("bikes:rentable4", [-122.2469854, 37.8104049, "station:3"])
print(res3)  # >>> 1

res4 = r.geosearch(
    "bikes:rentable4",
    longitude=-122.27652,
    latitude=37.805186,
    radius=0.1,
    unit="km",
)
print(res4) 


