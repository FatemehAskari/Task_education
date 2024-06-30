import redis
r=redis.Redis(host='127.0.0.1',port='6379',db=0)
data={
    "Ali": 1000,
    "Alex": 2000,
    "Hamid": 1356,
    "Hirad": 10180
}
for key,value in data.items():
    r.set(key,value,ex=86400)    
for key in data.keys():
    value=r.get(key)
    
    if value:
        print(f"{key}:{(int(value))}")
    else:
        print(f"{key}:not found")
                
