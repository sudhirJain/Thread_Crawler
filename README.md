# Thread_Crawler
Utility for download data from thredd server.
Following Command is used;
python thredds_server_download.py  -d SLC  -s sentinel-1 -t 2015-10-10 -o /g/data/v10/sentinel_hub_download/test/Test_Programs/

New Vesrion of Thredds_server_download.py has been amended it is used to down WOFS data from Thredd Server;
Following are the commands to download a single and multiple files;

Single FileDownload;
python New_thredds_server_download_V01.py -p 113 -r 024 -o .

Multiple Downlods;
for var in {020..026}; do python New_thredds_server_download_V01.py -p 113 -r ${var} -o .; done
