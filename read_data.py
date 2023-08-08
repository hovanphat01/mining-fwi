import os

def read_data(filename):
    with open(filename, 'rb') as f:
        data = f.read().decode('utf-8').split('\n')

    transactions = []
    for line in data:
        items = line.split(' ')
        transactions.append(items)
    
    return transactions

