import hashlib

import datetime 




def calc_hash(data):
      sha = hashlib.sha256()

      hash_str = data.encode('utf-8')

      sha.update(hash_str)

      return sha.hexdigest()




class Block:
    
    def __init__(self, data, previous_hash, timestamp):
      self.timestamp = timestamp 
      self.data = data
      self.previous_hash = previous_hash
      self.hash = calc_hash(data)
      self.previews_block = None


    def __str__(self): 
        timestamp = f'Timestamp: {self.timestamp}'
        data = f'Data: {self.data}'
        hash = f'Hash: {self.hash}'
        previous_hash = f'previous_hash: {self.previous_hash}'

        return  f'{data} {hash} {previous_hash} {timestamp}'


class BlockChain:

      def __init__(self):
            self.head = None



      def append(self,data,previews_hash, timestamp):

      
            if self.head == None:
                  
                  self.head = Block(data, 0, timestamp)
                  return

            new_block = Block(data,self.head.hash, timestamp)

            new_block.previews_block = self.head
            self.head = new_block 

           
      



      def size(self):

          size = 0
          current_block = self.head
          while current_block:

                size += 1
                current_block = current_block.previews_block
          return size

      def to_list(self):
          
          block_list = []

          current_block = self.head

          while current_block:

                block_list.append(current_block)
                current_block = current_block.previews_block
      
    
          return block_list


 


"""
Test Cases
"""
timestamp = datetime.datetime.utcnow()
A = BlockChain()
print("size",A.size())
print(A.head)



B = BlockChain()
B.append("Genesis",0,timestamp)
print("size",B.size())
for item in B.to_list():
    print(item)



print("Test Case 3 Two item BlockChain")
C = BlockChain()
C.append("Genesis",0,timestamp)
C.append("Exodus",calc_hash("Genesis"),timestamp)
print("size",C.size())
for item in C.to_list():
    print(item)

"""
Test Case with empy block
"""
print("Test Case with empty Block")
C = BlockChain()



print("size",C.size())
for item in C.to_list():
    print(item)


"""
Test Case with the sampe time stamp
"""
print("Test Case with empty Block")
C = BlockChain()
same_time = 0
C.append("Genesis",0,same_time)
C.append("Exodus",calc_hash("Genesis"),same_time)
C.append("Mathew",calc_hash("Exodus"),same_time)

print("size",C.size())
for item in C.to_list():
    print(item)