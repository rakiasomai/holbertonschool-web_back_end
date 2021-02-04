#!/usr/bin/env python3
''' MongoDB '''
import pymongo


def top_students(mongo_collection):
    ''' def top students '''
    agr = mongo_collection.aggregate([
        {"$project": {"name": "$name", "averageScore": {"$avg": "$topics.score"}}},
        {"$sort": {"averageScore": -1}}])
    return agr
