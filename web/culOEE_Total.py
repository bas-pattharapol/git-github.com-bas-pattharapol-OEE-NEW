import pyodbc
import json
from datetime import datetime, timedelta

server = "172.30.2.2"
#port = 5432
database = "OEE_DB"
username = "sa"
password = "p@ssw0rd"


def startOEE():
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    pd = cnxn.cursor()
    pd.execute('select PDOrder from OEEReport  order by RecordID DESC')
    for i in pd:
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        PDOrder = cnxn.cursor()
        PDOrder.execute("""
                        select PDOrder , UnplanDownTime , RunTime1 , RunTime2 ,
                        TotalCount , IdealCount1 , IdealCount2 , GoodCount , PostReturn
                        from OEEReport_Total where PDOrder = ? 
                        """,(i[0],))
        
        for j in PDOrder:
            UnplanDownTime = j[1]
            RunTime1 = j[2]
            RunTime2 = j[3]
            TotalCount = j[4]
            IdealCount1 = j[5]
            IdealCount2 = j[6]
            GoodCount = j[7]
            PostReturn = j[8]
            FinalGoodCount = GoodCount - PostReturn
            
            OEE_A1 = (RunTime1 - UnplanDownTime)/RunTime1
            OEE_A2 = (RunTime2 - UnplanDownTime)/RunTime2
            OEE_P1 = TotalCount / IdealCount1
            OEE_P2 = TotalCount / IdealCount2
            OEE_Q1 = GoodCount / TotalCount
            OEE_Q1_Final = FinalGoodCount / TotalCount
            OEE_Q2 = GoodCount / TotalCount
            OEE_Q2_Final = FinalGoodCount / TotalCount
            OEE1Calculation = OEE_A1 * OEE_P1 * OEE_Q1 
            OEE2Calculation = OEE_A2 * OEE_P2 * OEE_Q2 
            OEE1FinalCalculation = OEE_A1 * OEE_P1 * OEE_Q1_Final 
            OEE2FinalCalculation = OEE_A2 * OEE_P2 * OEE_Q2_Final 
            
            cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
            UPDATE = cnxn.cursor()
            UPDATE.execute("""UPDATE OEE_DB.dbo.[OEEReport_Total] 
                            SET 
                            FinalGoodCount = ?,
                            OEE_A1 = ?,
                            OEE_A2 = ?,
                            OEE_P1 = ?,
                            OEE_P2 = ?,
                            OEE_Q1 = ?,
                            OEE_Q1_Final = ?,
                            OEE_Q2 = ?,
                            OEE_Q2_Final = ?,
                            OEE1Calculation = ?,
                            OEE2Calculation = ?,
                            OEE1FinalCalculation = ?,
                            OEE2FinalCalculation = ?
                            WHERE PDOrder = ? """,(
                                FinalGoodCount ,
                                OEE_A1 ,
                                OEE_A2 ,
                                OEE_P1 ,
                                OEE_P2 ,
                                OEE_Q1 ,
                                OEE_Q1_Final,
                                OEE_Q2 ,
                                OEE_Q2_Final ,
                                OEE1Calculation ,
                                OEE2Calculation ,
                                OEE1FinalCalculation,
                                OEE2FinalCalculation,
                                i[0]))
            cnxn.commit()
        
