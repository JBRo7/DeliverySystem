
# used for the package data.
class HashTable:

    # Constructor with optional initial capacity parameter. All buckets are assigned nothing at first
    #O(n)
    def __init__(self, initial_capacity=40):
        # the list starts out as empty but will be filled later.
        self.address = None
        self.myList = []
        for i in range(initial_capacity):
            self.myList.append([])

    # This adds something new to the list and place it in a bucket.
    def insert(self, ID, item):
        bucket = hash(ID) % len(self.myList)
        my_bucket_list = self.myList[bucket]
        my_bucket_list.append([ID, item])

    # Searches for an item in a bucket with matching key in the hash table.
    #O(n)
    def search(self, key):
        bucket = hash(key) % len(self.myList)
        my_bucket_list = self.myList[bucket]

        for pair in my_bucket_list:
            if pair[0] == key:
                return pair[1]

    # This will delete something out of the list.
    def remove(self, key):
        bucket = hash(key) % len(self.myList)
        my_bucket_list = self.myList[bucket]

        # if item is found then it will be removed from the bucket.
        if key in my_bucket_list:
            my_bucket_list.remove(key)

    #update the address of Package 9
    def updatePkg9(self, key):
        pkg9 = self.search(9)
        pkg9.address = '410 S State St'
        pkg9.city = 'Salt Lake City'
        pkg9.zip = '84111'
        self.insert(pkg9, key)
        

