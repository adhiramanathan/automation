__author__ = 'vignesh'

from  disable_enable_backups.disable_enable_backups import disable_enable_backups
import MySQLdb,sys, os,datetime,logging
backup=disable_enable_backups()
#backup.upload_files()
#backup.getInstanceDetails('kf0001741','kissflow.com:kissflow')
#backup.disable_enable_backup('kf0001741','kissflow.com:kissflow',False)

dbname='os_flow'
dbuser='root'
dbpassword='orange123'
dbhost='flow-db-prd.cf3rzylmtqxs.us-east-1.rds.amazonaws.com'
port=3306

class main:
    def mysqlConnection(self):
        try:
         dbsql=MySQLdb.connect(host=dbhost,port=port,user=dbuser,passwd=dbpassword,db=dbname)
         return dbsql
        except Exception as e:
             raise e
             print "db connection is not possible"

    def execute_query(self,sql):
        dbconn=self.mysqlConnection()
        cursor=dbconn.cursor()
        cursor.execute(sql)
        results=cursor.fetchall()
        rowVal=[]
        for row in results:
           rowVal.append(row[5])
        return rowVal

main=main()
sql="SELECT cs.id, sys.SheetName, cs.id,syscs.CreatedAt,app.id,tbl.SQLInstance,app.Company,cs.UserType, app.Application_Name,company.CreatedAt, company.FinalSubscription, company.IsTrial, company.CreatedBy FROM tblappspot AS tbl, sysappspot AS sys,tblapplication AS app,tblcompanysubscription cs,syscompanysubscription syscs,tblcompany company where company.ISTrial < 0"
rowVal=main.execute_query(sql)
if len(rowVal) > 0:
  for row in rowVal:
       backup.disable_enable_backup(row,'kissflow.com:kissflow',False)



