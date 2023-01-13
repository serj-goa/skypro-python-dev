import redis


with redis.Redis(host='redis', port=6379) as client:
    while True:
        user_expression = client.brpop('expressions')[1].decode('utf-8')
        print(eval(user_expression))
