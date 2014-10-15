#! /usr/bin/env python
'''
    fitbit-steps.py
    
    Reads credentials from secret module then queries FitBit for total step 
    count. That's it!
'''
import argparse as ap
import pytz
from datetime import date, datetime, timedelta

import fitbit

from secret import *

if __name__ == '__main__':
    parser = ap.ArgumentParser(prog='fitbit-steps.py', 
                               conflict_handler='resolve', 
                               description="Get total steps for a given date")

    parser.add_argument('-d', '--date', default=date.today(),
                        metavar="STR", type=str,
                        help='A date formated like YYYY-MM-DD (Default: Today)')
    parser.add_argument('-n','--name', metavar="STR", type=str, required=True,
                        default='robert', help='Person to pull steps for.')
    parser.add_argument('-h', '--help', action='help', 
                        help='Show this help message and exit')
    
    args = parser.parse_args()

    auth_client = fitbit.Fitbit(
        CONSUMER_KEY, 
        CONSUMER_SECRET_KEY,
        resource_owner_key=USER_KEY[args.name],
        resource_owner_secret=USER_SECRET_KEY[args.name]
    )
    
    if args.date != date.today():
        if args.date == 'yesterday':
            args.date = datetime.now(pytz.timezone('US/Eastern')) - timedelta(1)
        else:
            args.date = datetime.strptime(args.date, "%Y-%m-%d")

    stats = auth_client.activities(date=args.date)

    print stats['summary']['steps']