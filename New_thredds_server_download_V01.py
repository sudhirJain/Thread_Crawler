#!/usr/bin/python

#--------------------------------------------------------------------------
# Author:       Sudhir Jain
# Date  :       20/10/2016
# Description:  Utility for downloading data from NCI thredd server
#               WOFS
#
#--------------------------------------------------------------------------

import argparse
import sys
import os
import urllib
import time
from functools import wraps
from thredds_crawler.crawl import Crawl

#--------------------------------------------------------------------------
#--------------------------------------------------------------------------

path  = ''
row   = ''
output_path  = ''

ts_url_1      = 'http://dapds00.nci.org.au/thredds/catalog/fk4/wofs/current/pyramids/WaterSummaryFiltered/0/'
ts_url_2      = 'catalog.xml'

#--------------------------------------------------------------------------
#--------------------------------------------------------------------------

def get_args():

   parser = argparse.ArgumentParser(
   description='Script downloads files from thread server ! ')

#--------------------------------------------------------------------------
#  Adding arguments
#--------------------------------------------------------------------------

   parser.add_argument(
   '-p','--path', type=str,help='Path Type(***) 025 ', required=True)
   parser.add_argument(
   '-r','--row', type=str, help='Data Type(***) 112', required=True)
   parser.add_argument(
   '-o','--opath', type=str,help='Output Path', required=True)

   args = parser.parse_args()

   return args.path, args.row, args.opath


#--------------------------------------------------------------------------
#--------------------------------------------------------------------------

class ThreadS_Download:

    def __init__(self):
        pass

#   Decorator for checking elapsed time

    def _with_Elapsedtime(func):
        wraps(func)
        def wrapper(*args, **kwargs):
            t1 = time.time()
            func(*args, **kwargs)
            t2 = time.time() - t1
            print ({'Data Downloading function {} ran in: {} secs '.format(func.__name__,t2)})
        return wrapper

    @_with_Elapsedtime
    def download_data_1(self):

        global output_path, row, path

        ts_path=ts_url_1+'/'+ts_url_2
        ts_path=ts_path.strip()
        sels = [".*_"+path+"_-"+row]

        c=Crawl(ts_path,select=sels)
        f_str=path+"_-"+row
        filtered_files = []
        for item in range(len(c.datasets)):
            if f_str in c.datasets[item].services[0]['url']:
                filtered_files.append(c.datasets[item].services[0]['url']+','+ c.datasets[item].name)

        print ' Download Started ..........'
        for item in filtered_files:
            ll=[]
            ll=item.split(',')
            o_path=output_path+'/'+ll[1]
            urllib.urlretrieve(ll[0],o_path)
            print 'Download Item : ',ll[1]
        print ' Download Finished ..........'

    def __del__(self):
        pass

#--------------------------------------------------------------------------
#--------------------------------------------------------------------------

if __name__ == "__main__":

   path, row, output_path = get_args()
   tobj = ThreadS_Download(); tobj.download_data_1()
