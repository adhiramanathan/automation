__author__ = 'vignesh'


from oauth2client.client import AccessTokenCredentials
import httplib2
from apiclient import discovery, http
from apiclient.http import MediaFileUpload
from oauth2client import file
from oauth2client import client
from oauth2client import tools
import logging;
import os
_API_VERSION = 'v1beta4'

class disable_enable_backups():
    def __init__(self):
      from authentication.generate_access_token import generate_access_token
      generate_access_token=generate_access_token()
      credentials=generate_access_token.get_access_token()
      httpreq = credentials.authorize(httplib2.Http())
      self.service = discovery.build('sqladmin',_API_VERSION, http=httpreq)

    def getInstanceDetails(self,instance_id,project_id):
        try:
         req=self.service.instances().get(
            project=project_id,
            instance=instance_id)
         resp=req.execute()
         return resp
        except Exception as e:
             print("exception raised")
             raise e

    def disable_enable_backup(self,instance_id,project_id,enable):
         instance_details=self.getInstanceDetails(instance_id,project_id)
         settings=instance_details.get("settings")
         tier=settings.get("tier")
         backupConfiguration=settings.get("backupConfiguration")
         enabled=backupConfiguration.get("enabled")
         settingVersion=instance_details.get("settingsVersion")
         if enabled:
           req=self.service.instances().update(
             project=project_id,
             instance=instance_id,
             body={
              "project":project_id,
              "kind":"sql#instance",
               "settings":{
                    "kind": "sql#settings",
                    "backupConfiguration":{
                        "kind":"sql#backupConfiguration",
                        "enabled":enable,
                        "binaryLogEnabled":enable
                    },
                "settingsVersion": settingVersion,
                "tier": tier}})

           resp = req.execute()
           return resp








