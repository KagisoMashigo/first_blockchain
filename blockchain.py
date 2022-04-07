# Module 1 - Create a Blockchain

# Importing the libraries
import datetime
# used to hash the blocks
import hashlib
import json
from flask import Flask, jsonify

# Part 1 - Building the blockchain
# Building a blockchain is always best done with a class

class Blockchain:
    
    def __init__(self):
        self.chain = []
        self.create_block(proof = 1, previous_hash = '0')

    def create_block(self, proof, previous_hash):
        block = {'index': len(self.chain) + 1,
                 'timestamp': str(datetime.datetime.now()),
                 'proof': proof,
                 'previous_hash': previous_hash}
        self.chain.append(block)
        return block
    
    def get_previous_block(self):
        # -1 will give the last index of a list in Python
        return self.chain[-1]