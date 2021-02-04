#!/usr/bin/env python3
''' MongoDB '''


def list_all(mongo_collection):
    ''' def list all '''
    docs = mongo_collection.find()
    return docs
