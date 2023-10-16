import time
import hashlib
import json
import random

#Delegate list for DPoS
delegates = ["delegate1", "delegate2", "delegate3", "delegate4", "delegate5", "delegate6", "delegate7", "delegate8", "delegate9", "delegate10"]

#Blockchain as a list
blockchain = []

class Block:
    #Constructor
    def __init__(self, transactions, previous_hash, chosen_delegate):
        self.timestamp = time.time()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.delegate = chosen_delegate  # The delegate who produced the block
        self.merkle_root = self.compute_merkle_root()
        self.nonce = random.randint(1, 100) 
        self.hash = self.calculate_hash()
    
    #Merkle Tree Computation
    def compute_merkle_root(self):
        # Create a list of transaction hashes
        transaction_hashes = [get_transaction_hash(transaction) for transaction in self.transactions]

        # Continue until there is only one hash left (the Merkle root)
        while len(transaction_hashes) > 1:
            next_level = []
            for i in range(0, len(transaction_hashes), 2):
                # Combine two hashes and hash them together
                combined_hash = transaction_hashes[i]
                if i + 1 < len(transaction_hashes):
                    combined_hash += transaction_hashes[i + 1]
                next_level.append(hashlib.sha256(combined_hash.encode()).hexdigest())
            transaction_hashes = next_level

        return transaction_hashes[0] 
    
    #Block Hash Calculation
    def calculate_hash(self):
        block_data = {
            "transactions": self.transactions,
            "previous_hash": self.previous_hash,
            "delegate": self.delegate,
            "timestamp": self.timestamp,
            "merkle_root": self.merkle_root,
            "nonce": self.nonce
        }
        block_data_str = json.dumps(block_data, sort_keys=True).encode()
        return hashlib.sha256(block_data_str).hexdigest()

    # Mining of block after every 3 transactions using DPoS consensus algorithm
    def mine_block(transactions, previous_hash):
        delegate_sums = {delegate: 0 for delegate in delegates}
        # Choose a random delegate 10 times and associate a random number from 1 to 100
        print("Voting for choosing the delegate")
        for _ in range(10):
            chosen_delegate = random.choice(delegates)
            print(f"Voted Delegate: {chosen_delegate}")
            random_number = random.randint(1, 100)
            print(f"Stake Percentage: {random_number}")
            delegate_sums[chosen_delegate] += random_number
        
        # Choose the delegate with the maximum sum as the final delegate
        chosen_delegate = max(delegate_sums, key=delegate_sums.get)

        #Creating object of Block Class
        block = Block(transactions, previous_hash, chosen_delegate)
        blockchain.append(block)
        print(f"Block #{len(blockchain)} verified by {chosen_delegate} has been added to the blockchain!")

    #View the blockchain with all possible information
    def view_blockchain(username):
        if username:
            for index, block in enumerate(blockchain):
                print("\n")
                print(f"Block #{index + 1}: ")
                print("\tTimestamp:", time.ctime(block.timestamp))
                print("\tDelegate:", block.delegate)
                print("\tPrevious Hash:", block.previous_hash)
                print("\tMerkle Root:", block.merkle_root)
                print("\tNonce:", block.nonce)
                print("\tHash:", block.hash)
                print("\tTransactions:")
                for transaction in block.transactions:
                    print(json.dumps(transaction, indent=4))
                print("\n")
        else:
            print("You must be logged in to view the blockchain.")       

#Transaction Hash Calculation
def get_transaction_hash(transaction):
        transaction_data_str = json.dumps(transaction, sort_keys=True)  # Convert to a JSON string
        transaction_hash = hashlib.sha256(transaction_data_str.encode()).hexdigest()
        return transaction_hash
                