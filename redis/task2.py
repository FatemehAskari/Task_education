import redis

# Create Redis client
r = redis.StrictRedis(host='127.0.0.1',port='6379',db=0)

def update_database(data):
    # Lock key for this operation
    lock_key = 'database_update_lock'

    # Try to acquire the lock
    locked = r.setnx(lock_key, '1')
    if not locked:
        # If lock is already held, return without updating
        print('Database update already in progress, skipping...')
        return

    # Set lock expiration to 60 seconds
    r.expire(lock_key, 60)

    try:
        # Perform database update
        print('Updating database with:', data)
        # Your database update logic goes here
        # Example database update:
        for key, value in data.items():
            r.set(key, value)
    except Exception as e:
        print('Error updating database:', e)
    finally:
        # Release the lock
        r.delete(lock_key)

# Example usage with sample data
data = {
    'user:1': 'John Doe',
    'user:2': 'Jane Smith',
    'product:123': 'Widget',
    'product:456': 'Gadget'
}
update_database(data)