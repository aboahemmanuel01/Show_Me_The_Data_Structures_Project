import datetime
import hashlib

class Block:

    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash(data)
      self.next = None

    def calc_hash(self, data):
      sha = hashlib.sha256()

      hash_str = data.encode('utf-8')

      sha.update(hash_str)

      return sha.hexdigest()

    #def __repr__(self):
        
        
        #return output

class Linkedlist:

    def __init__(self):
        self.current_block = None
        self.last_block = None
        self.size = 0

    def add_block(self, timestamp, data):
        #timestamp = time.gmtime()
        #data = value
        if data is None:
          return

        self.size += 1
        if not self.current_block:
          self.current_block = Block(timestamp, data, 0)
          self.last_block = self.current_block

        else:
          value = self.last_block
          self.last_block = Block(timestamp, data, value)
          self.last_block.previous_hash = value

def _timestamp():

  return datetime.datetime.utcnow().strftime("%Y/%m/%d %H:%M:%S")

        #previous_hash = self.current_block.hash if self.current_block else 0
        #self.current_block = Block(timestamp, data, previous_hash)
#Case 1
block_A = Block(_timestamp(), "Emmanuel", 0)
print("TimeStamp: ", block_A.timestamp)
print("Data: ", block_A.data)
print("Hash: ", block_A.hash)
print("Previous Hash: ", None)

#Case 2
#block_lists = Linkedlist()
block_B = Block(_timestamp(), "is", block_A)
print("\n")
print("TimeStamp: ", block_B.timestamp)
print("Data: ", block_B.data)
print("Hash: ", block_B.hash)
print("Previous Hash: ", block_A.hash)

#case 3
block_C = Block(_timestamp(), "Good", block_B)
print("\n")
print("TimeStamp: ", block_C.timestamp)
print("Data: ", block_C.data)
print("Hash: ", block_C.hash)
print("Previous Hash: ", block_B.hash)



block_lists = Linkedlist()
block_lists.add_block(_timestamp(), "Done!" )

