import hashlib

import datetime 




def calc_hash(data):
      sha = hashlib.sha256()

      hash_str = data.encode('utf-8')

      sha.update(hash_str)

      return sha.hexdigest()




class Block:
    
    def __init__(self, data, previous_hash):
      self.timestamp = datetime.datetime.utcnow()
      self.data = data
      self.previous_hash = previous_hash
      self.hash = calc_hash(data)
      self.previews_block = None




class BlockChain:

      def __init__(self):
            self.head = None



      def append(self,data,previews_hash):

      
            if self.head == None:
                  
                  self.head = Block(data, 0)
                  return

            new_block = Block(data,self.head.hash)

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

A = BlockChain()
print("size",A.size())
print(A.head)



B = BlockChain()
B.append("Genesis",0)
print("size",B.size())
for item in B.to_list():
    print(item)



print("Test Case 3 Two item BlockChain")
C = BlockChain()
C.append("Genesis",0)
C.append("Exodus",calc_hash("Genesis"))
