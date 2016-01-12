#!/usr/bin/python

#--------------------------------------------------------------------------
# Author:       Sudhir Jain
# Date  :       18/12/2015
# Description:  Utility for downloading data from NCI thredd server
#
#--------------------------------------------------------------------------

import argparse
import sys
import os
import urllib
from thredds_crawler.crawl import Crawl

#--------------------------------------------------------------------------
#--------------------------------------------------------------------------

datatype      = ''
download_date = ''
esasat        = ''
outpath_path  = ''

ts_url_1      = 'http://dapds00.nci.org.au/thredds/catalog/fj7/SAR/'
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
   '-s','--sat', type=str,help='Satellie(Sentinel_1) ', required=True)
   parser.add_argument(
   '-d','--dt', type=str, help='Data Type(RAW/SLC/GRD)', required=True,nargs='+')
   parser.add_argument(
   '-t','--dndt', type=str,help='Down Load Date(eg yyyy-mm-dd)', required=True, nargs='+')
   parser.add_argument(
   '-o','--opath', type=str,help='Output Path', required=True, nargs='+')

   args = parser.parse_args()

   return args.dt, args.dndt, (args.sat).capitalize(), args.opath


#--------------------------------------------------------------------------
#--------------------------------------------------------------------------

class ThreadS_Download:

    def __init__(self):
        pass

    def download_data(self):

        dd = ((download_date[0]).strip()).split("-")
        ts_path=ts_url_1+esasat+'/'+datatype[0]+'/'+dd[0]+'-'+dd[1]+'/'+ts_url_2
        ts_path=ts_path.strip()
        sels = [".*_"+dd[0].strip()+dd[1].strip()+dd[2].strip()]
        c=Crawl(ts_path,select=sels)
        f_str=dd[0]+dd[1]+dd[2]
        filtered_files = []

        for item in range(0,len(c.datasets)-1):
            if f_str in c.datasets[item].services[0]['url']:
                filtered_files.append(c.datasets[item].services[0]['url']+ ','+ c.datasets[item].name)

        print ' Download Started ..........'
        for item in filtered_files:
            l1 = ''
            l1=(item.strip()).split(',')
            print 'Downloading ', l1[1]
            o_path = output_path[0] + l1[1]
            urllib.urlretrieve(l1[0],o_path)
        print ' Download Finished ..........'

    def __del__(self):
        pass

#--------------------------------------------------------------------------
#--------------------------------------------------------------------------

if __name__ == "__main__":
   datatype,download_date,esasat,output_path = get_args()
   tobj = ThreadS_Download(); tobj.download_data()
