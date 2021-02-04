#!/usr/bin/env python3
''' MongoDB '''


def update_topics(mongo_collection, name, topics):
    ''' def update topics '''
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
