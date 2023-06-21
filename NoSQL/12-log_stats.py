#!/usr/bin/env python3
"""
Script that provides some stats about Nginx logs stored
in MongoDB.
"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://localhost:2717/')
    logs_collection = client.logs.nginx

    # Get number of docs in the collection
    num_logs = logs_collection.count_documents({})
    print(f"{num_logs} logs")

    # Get number of docs for each method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = logs_collection.count_documents({'method': method})
        print(f"\tmethod {method}: {count}")

    # Get num docs with method=GET and path=/status
    count = logs_collection.count_documents(
        {'method': 'GET', 'path': '/status'})
    print(f"{count} status check")
