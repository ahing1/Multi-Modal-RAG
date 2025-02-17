import json
import redis
from config import REDIS_HOST, REDIS_PORT, CACHE_TTL

# Initialize Redis
redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

def cache_request(data):
    """ Check if result is cached in Redis """
    cache_key = json.dumps(data)
    cached_response = redis_client.get(cache_key)
    if cached_response:
        return json.loads(cached_response)
    return None

def store_cache(data, response):
    """ Store response in Redis cache """
    cache_key = json.dumps(data)
    redis_client.set(cache_key, json.dumps(response), ex=CACHE_TTL)
