#! /usr/bin/env python
'''

'''
from datetime import date, timedelta
import fitbit
from secret import *

auth_client = fitbit.Fitbit(
    CONSUMER_KEY, 
    CONSUMER_SECRET_KEY,
    resource_owner_key=USER_KEY,
    resource_owner_secret=USER_SECRET_KEY
)
yesterday = date.today() - timedelta(1)

stats = auth_client.activities(date=yesterday)

print stats['summary']['steps']