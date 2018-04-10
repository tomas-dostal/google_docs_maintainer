#!/usr/bin/python3
# -*- coding: utf-8 -*-

from threading import Thread
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os, socket
REMOTE_SERVER = "www.google.com"

def connection_test():
  try:
    # see if we can resolve the host name -- tells us if there is
    # a DNS listening
    host = socket.gethostbyname(REMOTE_SERVER)
    # connect to the host -- tells us if the host is actually
    # reachable
    s = socket.create_connection((host, 80), 2)
    print("Connection available. \n")
    return True
  except:
     pass
  print("Connection not available. ")
  return False
def download (drive, id):
    file = drive.CreateFile({'id': id})
    mimetypes = {
        # Drive Document files as PDF
        'application/vnd.google-apps.document': 'application/pdf',

        # Drive Sheets files as PDF
        'application/vnd.google-apps.spreadsheet': 'application/pdf'# 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        # other mimetypes on https://developers.google.com/drive/v3/web/mime-types
    }

    download_mimetype = None

    # if the file's mimetype is in  mimetypes = {}, like google document, google sheet...
    if file['mimeType'] in mimetypes:
        download_mimetype = mimetypes[file['mimeType']]
        #print("↻ Converting " + file['title'] + ' to ' +  mimetypes[file['mimeType']])
        file.GetContentFile(file['title'] + ".pdf", mimetype=download_mimetype)
        #change version stored int title_version file.
        version_file = open(file['title'] + "_version","w+")
        version_file.write(file['version'])

    #    {'foo': 'bar',
    # if it's a normal file
    else:
        file.GetContentFile(file['title'])

    print("☑ " + file['title'] + " Downloaded! ("+ file['title'] + ")")
def check(drive, id):
    try:
        file = drive.CreateFile({'id': id})
        file.FetchMetadata()

        #print('Getting info for file: name: %s, mimeType: %s; version:  %s' % (file['title'], file['mimeType'], file['version']))

        # check if I own latest version of file
        if(os.path.isfile(file['title'] + "_version")):
            f = open(file['title'] + "_version", "r")
            local_version = int(f.readline())
        else:
            f = open(file['title'] + "_version", "w+")
            f.writelines("0")

        #print(file['title'] + " version " + file['version'] + " (online) == " + str(local_version) + " (local)")

        if(local_version == int(file['version'])):
            #print(file['title'] + " is up to date "+ file['version'])
            print("☑ " + file['title'] + ": version (local) "+ str(local_version) + "   ==  " + file['version'] + " (online) ")

            f.close()
            return
        else:
            print("↻ " + file['title'] + " version " + str(local_version) + " (local) -> " + file['version'] + " (online)" )
            f.close()
            # Local version is not updated. Make an update!
            if(file['copyable']):
                t = Thread(target=download, args=(drive, id))
                t.start()
            else:
                print("!!! " + file['title'] + " is not copyable. You do not have a permission to download it.")

        f.close()
    except:
        print("! " + file['title'] + ": an error occurred. :/ ")


# ================= here main function starts =================

# change working directory to script's location....
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

# Authorisation is needed to download files.
# You need to have an acces to files you're gonna download.
# If you don't have so, the program will not work.

if connection_test():
    gauth = GoogleAuth()
    # Creates local webserver and auto handles authentication.
    gauth.LocalWebserverAuth()
    # Create GoogleDrive instance with authenticated GoogleAuth instance.
    drive = GoogleDrive(gauth)


    # following documents will be downloaded.
    # to download file you need to get an ID, like 1yuJhon5FyvUVtqtzaoLHnm_M4EWba8WJbhgKiPvI5Wg, which you can extract from page URL
    """
       #1J_YafGKPBItGqJjxPBgJ-1sWDF2tmwIT0v2wClt2IB8 # dějepis moje 
       #1yuJhon5FyvUVtqtzaoLHnm_M4EWba8WJbhgKiPvI5Wg # společenské vědy moje 
       #19xSSOf0rfgOGxwe3V4RFevVNHkbdWRwm9S5DA-pCoIA # chemie moje 
       #1pNPQ9B_bTfSq1BJczC6cnBXRnv8OZ9W2Okul5i4vvUs # literatura moje
       #1-2-LtKTXkOYh_2J1pTCNIjHBIcSV1MDokNNBqfEx_hg # geografie moje 

       #1k-lmLsNoT-SpcIDx5YT0kRno7XjZN_d7YkbITw2Q5EA # dějspis od Marcela
       #1ZbqKG6nA5pTHdqG5Py0BnGuyemeLruLdXJ68MCJgmAY # chemie od Marcela
       #1BycZMbz8WCVArgHij1m02FmVt2iGv2KdJPtwglpyIXQ # literatura od Marcela
    """
    ids = { "1J_YafGKPBItGqJjxPBgJ-1sWDF2tmwIT0v2wClt2IB8",
            "1yuJhon5FyvUVtqtzaoLHnm_M4EWba8WJbhgKiPvI5Wg",
            "19xSSOf0rfgOGxwe3V4RFevVNHkbdWRwm9S5DA-pCoIA",
            "1pNPQ9B_bTfSq1BJczC6cnBXRnv8OZ9W2Okul5i4vvUs",
            "1-2-LtKTXkOYh_2J1pTCNIjHBIcSV1MDokNNBqfEx_hg",
           }
    print("Getting " + str(len(ids)) + " files... \n_____________________\n")

    # this is more cool solution: https://stackoverflow.com/questions/2846653/how-to-use-threading-in-python
    for id in ids:
        check(drive, id)

 # ================= here main function ends =================
