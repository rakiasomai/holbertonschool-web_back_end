#!/usr/bin/env python3
''' MongoDB, '''


def schools_by_topic(mongo_collection, topic):
    ''' def schools by topics '''
    return mongo_collection.find({"topics": topic})
