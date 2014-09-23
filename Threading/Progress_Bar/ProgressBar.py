'''
Created on Sep 23, 2014

@author: thomasknell
'''

import urllib.request
from urllib.error import  URLError



def main():
    url = "http://downloads.sourceforge.net/project/openofficeorg.mirror/4.1.1/binaries/en-US/Apache_OpenOffice_4.1.1_MacOS_x86-64_install_en-US.dmg?r=&ts=1411481687&use_mirror=switch"
    try:
        response = urllib.request.urlopen(url)
    except URLError as e:
        if hasattr(e, 'reason'):
            print('We failed to reach a server.')
            print('Reason: ', e.reason)
        elif hasattr(e, 'code'):
            print('The server couldn\'t fulfill the request.')
            print('Error code: ', e.code)
    else:
        print("downloading ")
        print (response.getheader('Content-Length'))
        # Open our local file for writing
        local_file = open('/Users/thomasknell/Downloads/tmp', "w" + 'b')
        #Write to our local file
        local_file.write(response.read(85705635))
        local_file.write(response.read(85705636))
        local_file.close()
        

if __name__ == '__main__':
    main()