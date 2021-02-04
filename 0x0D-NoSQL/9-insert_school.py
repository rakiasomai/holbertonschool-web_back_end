#!/usr/bin/env python3
''' MongoDB '''


def insert_school(mongo_collection, **kwargs):
    ''' def insert school '''
    add = mongo_collection.insert_one(kwargs)
    return add.inserted_id
