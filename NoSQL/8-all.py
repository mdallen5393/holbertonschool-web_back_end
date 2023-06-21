#!/usr/bin/env python3
"""
Defines a python function that lists all documents
in a collection.
"""
import pymongo


def list_all(mongo_collection):
    """lists all documents in a collection"""

    return list(mongo_collection.find())