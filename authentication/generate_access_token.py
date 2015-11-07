__author__ = 'vignesh'
import urllib2
import urllib
import json
import argparse
import os
from urllib2 import Request
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
from apiclient.discovery import build
from oauth2client import tools
from oauth2client import file
from oauth2client.client import SignedJwtAssertionCredentials
from oauth2client.file import Storage
import httplib2

resourcePath = os.path.join(os.path.dirname(__file__),"resources")

SERVICE_ACCOUNT_EMAIL ='283378574268-v1hbp93pkt1jh2rcumfjlkhu6livosti@developer.gserviceaccount.com'
PRIVATE_KEY_PATH =  os.path.join(resourcePath,'Credentials.json')
CREDENTIALS_STORAGE = os.path.join(os.path.dirname(PRIVATE_KEY_PATH),
                                   '{}-credentials.json'.format('sqladmin'))
class generate_access_token():

  def get_access_token(self):
       storage = Storage(CREDENTIALS_STORAGE)
       credentials = storage.get()
       http = httplib2.Http()

       if credentials is None or credentials.invalid:
         with open(PRIVATE_KEY_PATH, 'rb') as f:
            private_key = json.loads(f.read()).get("private_key")
         credentials = SignedJwtAssertionCredentials(SERVICE_ACCOUNT_EMAIL,
                                                    private_key,
                                                    scope='https://www.googleapis.com/auth/sqlservice.admin')
         storage.put(credentials)
       else:
         credentials.refresh(http)

       return credentials






