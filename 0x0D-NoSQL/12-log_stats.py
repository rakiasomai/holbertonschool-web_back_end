#!/usr/bin/env python3
''' MongoDB '''
from pymongo import MongoClient


def log_stats():
    ''' def log stats '''
    client = MongoClient("mongodb://127.0.0.1:27017")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    data = client.logs.nginx
    print("{} logs".format(data.count_documents({})))
    print('Methods:')

    for method in methods:
        print("\tmethod {}: {}".format(
                method, data.count_documents({'method': method})))

    print("{} status check".format(
        data.count_documents({'method': 'GET', 'path': '/status'})))

if __name__ == "__main__":
    log_stats()
