import os

def read_data(filename):
    with open(filename, 'rb') as f:
        data = f.read().decode('utf-8').split('\n')

    transactions = []
    for line in data:
        items = line.split(' ')
        transactions.append(items)
    
    return transactions

def transform_to_data(transactions):
    database = []
    for transaction in transactions:
        itemset = {}
        for item in transaction:
            if item != '\r':
                itemset[f'{item}'] = 1
        database.append(itemset)
    return database
