#! /usr/bin/python
# -*- coding:utf-8 -*-


import pymongo
import config

mdb = pymongo.MongoClient(**config.MONGO_CONFIG)[config.MDB_NAME]
