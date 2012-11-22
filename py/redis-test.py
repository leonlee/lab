import redis

#r = redis.StrictRedis(host="localhost", port=6379, db=0)
#r.set('foo', 'bar')
#print r.get('foo')

class RedisQueue(object):
    """Simple Queue with Redis Backend"""
    def __init__(self, name, namespace='queue', **redis_kwargs):
        self.__db = redis.Redis(**redis_kwargs)
        self.__pubsub = self.__db.pubsub()
        self.key = '%s:%s' %(namespace, name)
        
    def qsize(self):
        return self.__db.llen(self.key)

    def empty(self):
        return self.qsize() == 0

    def put(self, item):
        self.__db.rpush(self.key, item)

    def get(self, block=True, timeout=None):
        if block:
            item = self.__db.blpop(self.key, timeout=timeout)
        else:
            item = self.__db.lpop(self.key)

        if item:
            item = item[1]
        return item
    
    def pub(self, channel, message):
        self.__db.publish(channel, message)

    def sub(self, channel):
        self.__pubsub.subscribe(channel)

    def _listen(self):
        for message in self.__pubsub.listen():
            print 'got msg: %s' %(message)
    
    def get_nowait(self):
        return self.get(False)

def main():
    print 'test'
    q = RedisQueue('test')
    q.put('hello world')
    
    print 'got %s' %(q.get())
    
    q.pub('top', 'test')
    q.sub('top')
    q.pub('top', 'top one lumian 920')

if __name__ == '__main__':
    main()

