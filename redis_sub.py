from redis import Redis

# redis 连接
cil = Redis()

# 创建一个订阅连接 （创建一个管道）
sub = cil.pubsub()

# 订阅 teachers
sub.subscribe("teachers")


# 监听 teachers的信息
for i in sub.listen():
    print(i)

