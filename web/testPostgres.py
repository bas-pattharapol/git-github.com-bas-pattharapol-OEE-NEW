from flask import Flask, render_template, request, redirect, url_for, jsonify,make_response,session
from flask.sessions import NullSession
from flask_socketio import SocketIO
from flask_login.utils import logout_user
import pandas as pd
import psycopg2
import pdfkit
import json
from datetime import datetime, timedelta

host = "127.0.0.1"
port = 5432
database = "oeeV99"
user = "postgres"
passwd = "P@ssw0rd"

app = Flask(__name__)

count = 3
@app.route('/')
@app.route('/index')
def index():
    global count
    count+=1
    print(count)
    return render_template('index.html')

@app.route("/uploadFile", methods=['GET', 'POST'])
def uploadFile():
    if request.method == 'POST':
        print(request.files['file'])
        #print(request.files['file2'])
       
        f = request.files['file']
        col = ['Plant','MachineID','Machine','Loading','Sat','Sun','Mon','Tue','Wed','The','Fri','Sat1','Sun1']
        data_xls = pd.read_excel(f,usecols ='A:M',skiprows=2,header=None,names=col)
        data_xls1 = pd.read_excel(f,usecols ='A:M',skiprows=3,header=None,names=col)
        dimensions = data_xls.shape
        print(dimensions[0])
        dataPlant = []
        dataMachineID = []
        dataMachine =[]
        dataLoading=[]
        dataPlannedCode=[]
        dataDate=[]
        dataStart=[]
        dataEnd=[]
            
        dataGet = ['Sat','Sun','Mon','Tue','Wed','The','Fri','Sat1','Sun1']
        now = datetime.now()
      
        conn = psycopg2.connect(host=host, port = port, database=database, user=user, password=passwd)
        cur = conn.cursor()
        cur.execute(""" SELECT s."ShiftcodeID" ,s."StartTime" ,s."EndTime" FROM  "Data"."ShiftCode" s """)
        Plant_s = []
        PlannedCode_Chk = []
        StartTime = []
        EndTime = []
        PlantID_Chk = []
        PlantName_Chk = []
        dataPlantName= []
        len_Plant_s = 0
        for i in cur:
            len_Plant_s+=1
            Plant_s.append(i)
                    
        for i in range(0,len_Plant_s):
           PlannedCode_Chk.append(Plant_s[i][0])
               
        for i in range(0,len_Plant_s):
           StartTime.append(Plant_s[i][1].strftime("%H:%M:%S"))
               
        for i in range(0,len_Plant_s):
           EndTime.append(Plant_s[i][2].strftime("%H:%M:%S"))
               
        conn = psycopg2.connect(host=host, port = port, database=database, user=user, password=passwd)
        cur = conn.cursor()
        cur.execute("""SELECT s."PlantID" ,s."PlantName" FROM  "Data"."Plant" s """)
            
        len_Plant_data = 0
        Plant_data = []
        for i in cur:
            len_Plant_data+=1
            Plant_data.append(i)
            
        for i in range(0,len_Plant_data):
           PlantID_Chk.append(Plant_data[i][0])
               
        for i in range(0,len_Plant_data):
           PlantName_Chk.append(Plant_data[i][1])
        
            
        print(PlannedCode_Chk)
        print(PlantName_Chk)
        print(StartTime)
        print(EndTime)
        for i in range(0,int(dimensions[0])-1):
            for j in range(0,9):
                
                if data_xls[dataGet[j]][0] >= now :
                
                    dataPlant.append(data_xls1['Plant'][i])
                    dataMachineID.append(data_xls1['MachineID'][i])
                    dataMachine.append(data_xls1['Machine'][i])
                    dataLoading.append(data_xls1['Loading'][i])
                    dataPlannedCode.append(data_xls1[dataGet[j]][i])
                        
                    for o in range(0,len_Plant_s):
                        if data_xls1[dataGet[j]][i] == PlannedCode_Chk[o] :
                            dataStart.append(StartTime[o])
                            dataEnd.append(EndTime[o])
                                
                    for o in range(0,len_Plant_data):
                        if PlantName_Chk[o] == data_xls1['Plant'][i] :
                            dataPlantName.append(PlantID_Chk[o])
                           
                        
                    dataDate.append(data_xls[dataGet[j]][0].date())
       
        ok_data  = pd.DataFrame({'PlantName':dataPlant,
                                 'PlantID':dataPlantName,
                                    'MachineID':dataMachineID,
                                    'Machine':dataMachine,
                                    'Loading':dataLoading,
                                    'Date':dataDate,
                                    'PlannedCode':dataPlannedCode,
                                    'StartTime':dataStart,
                                    'EndTime':dataEnd})
        print(ok_data)
        conn = psycopg2.connect(host=host, port = port, database=database, user=user, password=passwd)
        cur = conn.cursor()
        for row in ok_data.itertuples():
            postgres_insert_query = """ INSERT INTO "Data"."PlannedProductionTime" ("PlantID","PlantName", "MachineID", "MachineName","LoadingDate","Date","PlannedCode","StartTime","EndTime") VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
            record_to_insert = (row.PlantID,row.PlantName, row.MachineID, row.Machine,row.Loading,row.Date,row.PlannedCode,row.StartTime,row.EndTime)
            cur.execute(postgres_insert_query, record_to_insert)

        conn.commit()
            
        return redirect(url_for('uploadFile'))
      
    return render_template('uploadFile.html')

@app.route('/ReportOEE')
def ReportOEE():
    return render_template('Report_OEE.html')

@app.route('/ReportYield')
def ReportYield():
    return render_template('Report_Yield.html')

    
@app.route('/ReportOverallYield')
def ReportOverallYield():
    return render_template('Report_Overall_Yield.html')

@app.route('/ReportOEEMontly')
def ReportOEEMontly():
    return render_template('Report_OEE_Montly.html')

@app.route('/ReportYieldMontly')
def ReportYieldMontly():
    return render_template('Report_Yield_Montly.html')

@app.route('/Edit_StorageTanks/<string:mode>/<string:id>',methods=['GET', 'POST'])
def Edit_StorageTanks(mode,id):
    if request.method == 'POST':
        if mode == 'update':
            StorageID = request.form['StorageID']
            StorageName = request.form['StorageName']
            PlantName = request.form['PlantName']
            MaxSize = request.form['MaxSize']
            NormalSize = request.form['NormalSize']
             
            cnxn = psycopg2.connect(host=host, port = port, database=database, user=user, password=passwd)
            StorageTanks = cnxn.cursor()
            StorageTanks.execute("""UPDATE "Data"."StorageTanks" SET "StorageID" = %s , "StorageName" = %s,"PlantName" = %s,"MaxSize" = %s,"NormalSize" = %s,"DeleteFlag" = %s WHERE "RecordID" = %s """, ( StorageID  , StorageName , PlantName , MaxSize , NormalSize , "1",id ))
            cnxn.commit()
            
        elif mode == "add":
            StorageID = request.form['StorageID']
            StorageName = request.form['StorageName']
            PlantName = request.form['PlantName']
            MaxSize = request.form['MaxSize']
            NormalSize = request.form['NormalSize']
            
            cnxn = psycopg2.connect(host=host, port = port, database=database, user=user, password=passwd)
            StorageTanks = cnxn.cursor()
            StorageTanks.execute("""INSERT INTO "Data"."StorageTanks"("StorageID","StorageName","PlantName","MaxSize","NormalSize","DeleteFlag") VALUES(%s,%s,%s,%s,%s,%s)""" ,( StorageID  , StorageName , PlantName , MaxSize , NormalSize , "1" ))
            cnxn.commit()
            
    if mode == "del":
        cnxn = psycopg2.connect(host=host, port = port, database=database, user=user, password=passwd)
        StorageTanks = cnxn.cursor()
        StorageTanks.execute(""" UPDATE "Data"."StorageTanks" SET "DeleteFlag" = -1 WHERE "RecordID" = %s """,id )
        cnxn.commit()   
    
    
    cnxn = psycopg2.connect(host=host, port = port, database=database, user=user, password=passwd)
    StorageTanks = cnxn.cursor()
    StorageTanks.execute(""" SELECT * FROM "Data"."StorageTanks" WHERE "DeleteFlag" = 1 ORDER BY "DateTime" DESC""")
    
    cnxn = psycopg2.connect(host=host, port = port, database=database, user=user, password=passwd)
    Plant = cnxn.cursor()
    Plant.execute("""SELECT "PlantName" FROM "Data"."Plant" WHERE "DeleteFlag" = 1""")
    lenPlant = 0
    Plant_s = []
    for i in Plant:
        lenPlant+=1
        Plant_s.append(i)
        
    print(Plant_s)
        
    return render_template('Edit_StorageTanks.html',StorageTanks = StorageTanks,Plant=Plant_s,len=lenPlant)

@app.route('/Edit_Machines/<string:mode>/<string:id>',methods=['GET', 'POST'])
def Edit_Machines(mode,id):
    if request.method == 'POST':
        if mode == 'update':
            MachineID = request.form['MachineID']
            MachineName = request.form['MachineName']
            MachineDesc = request.form['MachineDesc']
            PlantName = request.form['PlantName']
            MainProduct = request.form['MainProduct']
            SubProduct = request.form['SubProduct']
            ValidatedSpeed = request.form['ValidatedSpeed']
            MaxSpeed = request.form['MaxSpeed']
             
            cnxn = psycopg2.connect(host=host, port = port, database=database, user=user, password=passwd)
            StorageTanks = cnxn.cursor()
            StorageTanks.execute(""" UPDATE "Data"."Machines" SET "MachineID" = %s , "MachineName" = %s,"MachineDesc" = %s,"PlantName" = %s,"MainProduct" = %s,"SubProduct" = %s,"ValidatedSpeed" = %s,"MaxSpeed" = %s,"DeleteFlag" = %s WHERE "RecordID" = %s """, ( MachineID  , MachineName , MachineDesc , PlantName , MainProduct ,SubProduct,ValidatedSpeed,MaxSpeed ,"1",id ))
            cnxn.commit()
            
        elif mode == "add":
            MachineID = request.form['MachineID']
            MachineName = request.form['MachineName']
            MachineDesc = request.form['MachineDesc']
            PlantName = request.form['PlantName']
            MainProduct = request.form['MainProduct']
            SubProduct = request.form['SubProduct']
            ValidatedSpeed = request.form['ValidatedSpeed']
            MaxSpeed = request.form['MaxSpeed']
            
            cnxn = psycopg2.connect(host=host, port = port, database=database, user=user, password=passwd)
            StorageTanks = cnxn.cursor()
            StorageTanks.execute(""" INSERT INTO "Data"."Machines"("MachineID"  , "MachineName" , "MachineDesc" , "PlantName" , "MainProduct" ,"SubProduct","ValidatedSpeed","MaxSpeed" ,"DeleteFlag") VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)""" , ( MachineID  , MachineName , MachineDesc , PlantName , MainProduct ,SubProduct,ValidatedSpeed,MaxSpeed ,"1" ))
            cnxn.commit()
            
    if mode == "del":
        cnxn = psycopg2.connect(host=host, port = port, database=database, user=user, password=passwd)
        Machines = cnxn.cursor()
        Machines.execute("""UPDATE "Data"."Machines" SET "DeleteFlag" = -1 WHERE "RecordID" = %s """,id )
        cnxn.commit()   
    
    
    cnxn = psycopg2.connect(host=host, port = port, database=database, user=user, password=passwd)
    Machines = cnxn.cursor()
    Machines.execute("""SELECT * FROM "Data"."Machines" WHERE "DeleteFlag" = 1 ORDER BY "DateTime" DESC""")
    
    cnxn = psycopg2.connect(host=host, port = port, database=database, user=user, password=passwd)
    Plant = cnxn.cursor()
    Plant.execute("""SELECT "PlantName" FROM "Data"."Plant" WHERE "DeleteFlag" = 1 """)
    lenPlant = 0
    Plant_s = []
    for i in Plant:
        lenPlant+=1
        Plant_s.append(i)
        
    print(Plant_s)
        
    return render_template('Edit_Machines.html',Machines = Machines,Plant=Plant_s,len = lenPlant)

@app.route('/Edit_Plant/<string:mode>/<string:id>',methods=['GET', 'POST'])
def Edit_Plant(mode,id):
    if request.method == 'POST':
        if mode == 'update':
            PlantID = request.form['PlantID']
            PlantName = request.form['PlantName']
            
            cnxn = psycopg2.connect(host=host, port = port, database=database, user=user, password=passwd)
            Plant = cnxn.cursor()
            Plant.execute(""" UPDATE "Data"."Plant" SET "PlantID" = %s , "PlantName" = %s,"DeleteFlag" = %s WHERE "RecordID" = %s""", (  PlantID  , PlantName , "1",id ))
            cnxn.commit()
            
        elif mode == "add":
            PlantID = request.form['PlantID']
            PlantName = request.form['PlantName']
            
            cnxn = psycopg2.connect(host=host, port = port, database=database, user=user, password=passwd)
            Plant = cnxn.cursor()
            Plant.execute(""" INSERT INTO "Data"."Plant"("PlantID","PlantName","DeleteFlag") VALUES(%s,%s,%s)""" ,( PlantID  , PlantName , "1" ))
            cnxn.commit()
            
    if mode == "del":
        cnxn = psycopg2.connect(host=host, port = port, database=database, user=user, password=passwd)
        Plant = cnxn.cursor()
        Plant.execute("""UPDATE "Data"."Plant" SET "DeleteFlag" = -1 WHERE "RecordID" =%s """,id )
        cnxn.commit()
    
    cnxn = psycopg2.connect(host=host, port = port, database=database, user=user, password=passwd)
    Plant = cnxn.cursor()
    Plant.execute("""SELECT * FROM "Data"."Plant" WHERE "DeleteFlag" = 1 ORDER BY "DateTime" DESC""")
    
    
        
    return render_template('Edit_Plant.html',Plant = Plant)

@app.route('/Edit_DownTimeCode/<string:mode>/<string:id>',methods=['GET', 'POST'])
def Edit_DownTimeCode(mode,id):
    if request.method == 'POST':
        if mode == 'update':
            CodeID = request.form['CodeID']
            Code = request.form['Code']
            Description = request.form['Description']
            Type = request.form['Type']
            Response = request.form['Response']
            
            cnxn = psycopg2.connect(host=host, port = port, database=database, user=user, password=passwd)
            DownTimeCode = cnxn.cursor()
            DownTimeCode.execute("""UPDATE "Data"."DownTimeCode" SET "CodeID" = %s , "Code" = %s,"Description" = %s,"Type" = %s,"Response" = %s,"DeleteFlag" = %s WHERE "RecordID" =%s """, (CodeID  , Code,Description ,Type,Response, "1",id ))
            cnxn.commit()
            
        elif mode == "add":
            CodeID = request.form['CodeID']
            Code = request.form['Code']
            Description = request.form['Description']
            Type = request.form['Type']
            Response = request.form['Response']
            
            cnxn = psycopg2.connect(host=host, port = port, database=database, user=user, password=passwd)
            DownTimeCode = cnxn.cursor()
            DownTimeCode.execute(""" INSERT INTO "Data"."DownTimeCode"("CodeID"  , "Code","Description" ,"Type","Response","DeleteFlag") VALUES(%s,%s,%s,%s,%s,%s)""" , (CodeID  , Code,Description ,Type,Response, "1" ))
            cnxn.commit()
            
    if mode == "del":
        cnxn = psycopg2.connect(host=host, port = port, database=database, user=user, password=passwd)
        DownTimeCode = cnxn.cursor()
        DownTimeCode.execute(""" UPDATE "Data"."DownTimeCode" SET "DeleteFlag" = -1 WHERE  "RecordID" = %s """,id )
        cnxn.commit()
    
    cnxn = psycopg2.connect(host=host, port = port, database=database, user=user, password=passwd)
    DownTimeCode = cnxn.cursor()
    DownTimeCode.execute("""SELECT * FROM "Data"."DownTimeCode" WHERE "DeleteFlag" = 1 ORDER BY "DateTime" DESC""")
    
    
        
    return render_template('Edit_DownTimeCode.html',DownTimeCode = DownTimeCode)

@app.route('/Edit_Shift/<string:mode>/<string:id>',methods=['GET', 'POST'])
def Edit_Shift(mode,id):
    if request.method == 'POST':
        if mode == 'update':
            ShiftCodeID = request.form['ShiftCodeID']
            ShiftCodeName = request.form['ShiftCodeName']
            StartTime = request.form['StartTime']
            EndTime = request.form['EndTime']
            Break1 = request.form['Break1']
            Break2 = request.form['Break2']
            Break3 = request.form['Break3']
            PlanProductionTime = request.form['PlanProductionTime']
            
            cnxn = psycopg2.connect(host=host, port = port, database=database, user=user, password=passwd)
            Edit_Shift = cnxn.cursor()
            Edit_Shift.execute("""UPDATE "Data"."ShiftCode" SET "ShiftCodeID" = %s , "ShiftCodeName" = %s,"StartTime" = %s,"EndTime" = %s,"Break1" = %s,"Break2" = %s,"Break3" = %s,"PlanProductionTime" = %s,"DeleteFlag" = %s WHERE "RecordID" = %s """,( ShiftCodeID  , ShiftCodeName,StartTime ,EndTime,Break1,Break2,Break3,PlanProductionTime ,"1",id ))
            cnxn.commit()
            
        elif mode == "add":
            ShiftCodeID = request.form['ShiftCodeID']
            ShiftCodeName = request.form['ShiftCodeName']
            StartTime = request.form['StartTime']
            EndTime = request.form['EndTime']
            Break1 = request.form['Break1']
            Break2 = request.form['Break2']
            Break3 = request.form['Break3']
            PlanProductionTime = request.form['PlanProductionTime']
            
            
            cnxn = psycopg2.connect(host=host, port = port, database=database, user=user, password=passwd)
            Edit_Shift = cnxn.cursor()
            Edit_Shift.execute("""INSERT INTO "Data"."ShiftCode"("ShiftCodeID"  , "ShiftCodeName","StartTime" ,"EndTime","Break1","Break2","Break3","PlanProductionTime","DeleteFlag") VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)""" ,(  ShiftCodeID  , ShiftCodeName,StartTime ,EndTime,Break1,Break2,Break3,PlanProductionTime, "1") )
            cnxn.commit()
            
    if mode == "del":
        cnxn = psycopg2.connect(host=host, port = port, database=database, user=user, password=passwd)
        Edit_Shift = cnxn.cursor()
        Edit_Shift.execute("""UPDATE "Data"."ShiftCode" SET "DeleteFlag" = %s WHERE "RecordID" = %s """,(-1,id) )
        cnxn.commit()
    
    cnxn = psycopg2.connect(host=host, port = port, database=database, user=user, password=passwd)
    Edit_Shift = cnxn.cursor()
    Edit_Shift.execute("""SELECT * FROM "Data"."ShiftCode" WHERE "DeleteFlag" = 1 ORDER BY "DateTime" DESC""")
    
    
        
    return render_template('Edit_Shift.html',Edit_Shift = Edit_Shift)

@app.route('/Edit_Standardcolor/<string:mode>/<string:id>',methods=['GET', 'POST'])
def Edit_Standardcolor(mode,id):
    if request.method == 'POST':
        if mode == 'update':
            Red = request.form['Red']
            Yellow = request.form['Yellow']
            Green = request.form['Green']
            Revision = request.form['Revision']
            
            cnxn = psycopg2.connect(host=host, port = port, database=database, user=user, password=passwd)
            DownTimeCode = cnxn.cursor()
            DownTimeCode.execute("""UPDATE "Data"."StandardColor" SET "Red" = %s , "Yellow" = %s,"Green" = %s,"Revision" = %s,"DeleteFlag" = %s WHERE "RecordID" = %s """, (Red  , Yellow ,Green ,Revision, "1",id ))
            cnxn.commit()
            
        elif mode == "add":
            Red = request.form['Red']
            Yellow = request.form['Yellow']
            Green = request.form['Green']
            Revision = request.form['Revision']
            
            cnxn = psycopg2.connect(host=host, port = port, database=database, user=user, password=passwd)
            DownTimeCode = cnxn.cursor()
            DownTimeCode.execute("""INSERT INTO "Data"."StandardColor"("Red"  , "Yellow" ,"Green" ,"Revision","DeleteFlag") VALUES(%s,%s,%s,%s,%s)""",( Red  , Yellow ,Green ,Revision, "1" ))
            cnxn.commit()
            
   
    
    cnxn = psycopg2.connect(host=host, port = port, database=database, user=user, password=passwd)
    Edit_Standardcolor = cnxn.cursor()
    Edit_Standardcolor.execute("""SELECT * FROM "Data"."StandardColor" WHERE "DeleteFlag" = 1 ORDER BY "DateTime" DESC""")
    Standardcolor = []
    
    for i in Edit_Standardcolor:
        #len_color+=1
        Standardcolor.append(i)
    
        
    return render_template('Edit_Standardcolor.html',Edit_Standardcolor = Standardcolor)



@app.route('/Report_OEE_API' ,methods=["GET", "POST"])
def Report_OEE_API():
    global count
    q = request.args.get('q')
    print(q)

    if request.method == "POST":
        count+=1
        return redirect(url_for('ReportOEE'))
    else:
        return {
                "data": [{
                    "Plant": "T1" + str(count),
                    "work_time": "กะสั้นเช้า",
                    "Posting_Date": "10/10/2501",
                    "PD_order": "78852145",
                    "Material_number": "12541250",
                    "Material_Description": "text text",
                    "Machine": "Robotic",
                    "Machine_Text": "Robotic",
                    "Validate_Speed": "100",
                    "Plan_DT": "10",
                    "Unlan_DT": "12",
                    "ka_time": "11",
                    "getwork_time_1": "2",
                    "getwork_time_2": "3",
                    "number_of_product": "1000",
                    "number_should_of_product_1": "1040",
                    "number_should_of_product_2": "1020",
                    "product_Qty": "900",
                    "Return_Qty": "800",
                    "product_Qty_F": "900",
                    "Availability_A1": "70",
                    "Availability_A2": "75",
                    "Performance_P1": "80",
                    "Performance_P2": "85",
                    "Quality": "90",
                    "Quality_Final": "90",
                    "OEE1": "90",
                    "OEE2": "95",
                    "OEE1_F": "90",
                    "OEE2_F": "95"
                }, {
                    "Plant": "TLT",
                    "work_time": "กะสั้นเช้า",
                    "Posting_Date": "10/10/2501",
                    "PD_order": "78852145",
                    "Material_number": "12541250",
                    "Material_Description": "text text",
                    "Machine": "Robotic",
                    "Machine_Text": "Robotic",
                    "Validate_Speed": "100",
                    "Plan_DT": "10",
                    "Unlan_DT": "12",
                    "ka_time": "11",
                    "getwork_time_1": "2",
                    "getwork_time_2": "3",
                    "number_of_product": "1000",
                    "number_should_of_product_1": "1040",
                    "number_should_of_product_2": "1020",
                    "product_Qty": "900",
                    "Return_Qty": "800",
                    "product_Qty_F": "900",
                    "Availability_A1": "70",
                    "Availability_A2": "75",
                    "Performance_P1": "80",
                    "Performance_P2": "85",
                    "Quality": "90",
                    "Quality_Final": "90",
                    "OEE1": "90",
                    "OEE2": "95",
                    "OEE1_F": "90",
                    "OEE2_F": "95"
                }, {
                    "Plant": "TLT",
                    "work_time": "กะสั้นเช้า",
                    "Posting_Date": "10/10/2501",
                    "PD_order": "78852145",
                    "Material_number": "12541250",
                    "Material_Description": "text text",
                    "Machine": "Robotic",
                    "Machine_Text": "Robotic",
                    "Validate_Speed": "100",
                    "Plan_DT": "10",
                    "Unlan_DT": "12",
                    "ka_time": "11",
                    "getwork_time_1": "2",
                    "getwork_time_2": "3",
                    "number_of_product": "1000",
                    "number_should_of_product_1": "1040",
                    "number_should_of_product_2": "1020",
                    "product_Qty": "900",
                    "Return_Qty": "800",
                    "product_Qty_F": "900",
                    "Availability_A1": "70",
                    "Availability_A2": "75",
                    "Performance_P1": "80",
                    "Performance_P2": "85",
                    "Quality": "90",
                    "Quality_Final": "90",
                    "OEE1": "90",
                    "OEE2": "95",
                    "OEE1_F": "90",
                    "OEE2_F": "95"
                }, {
                    "Plant": "TLT",
                    "work_time": "กะสั้นเช้า",
                    "Posting_Date": "10/10/2501",
                    "PD_order": "78852145",
                    "Material_number": "12541250",
                    "Material_Description": "text text",
                    "Machine": "Robotic",
                    "Machine_Text": "Robotic",
                    "Validate_Speed": "100",
                    "Plan_DT": "10",
                    "Unlan_DT": "12",
                    "ka_time": "11",
                    "getwork_time_1": "2",
                    "getwork_time_2": "3",
                    "number_of_product": "1000",
                    "number_should_of_product_1": "1040",
                    "number_should_of_product_2": "1020",
                    "product_Qty": "900",
                    "Return_Qty": "800",
                    "product_Qty_F": "900",
                    "Availability_A1": "70",
                    "Availability_A2": "75",
                    "Performance_P1": "80",
                    "Performance_P2": "85",
                    "Quality": "90",
                    "Quality_Final": "90",
                    "OEE1": "90",
                    "OEE2": "95",
                    "OEE1_F": "90",
                    "OEE2_F": "95"
                }]
            }, 201          
        
@app.route('/Report_OEE_Montly_API' ,methods=["GET", "POST"])
def Report_OEE_Montly_API():
    global count
    q = request.args.get('q')
    print(q)

    if request.method == "POST":
        count+=1
        return redirect(url_for('ReportOEEMontly'))
    else:
        return {
                "data": [{
                    "Month": "Jan",
                    "Plant": "T1" + str(count),
                    "Machine": "Robotic",
                    "Machine_Text": "Robotic",
                    "WorkTime": "2",
                    "Plan_DT": "10",
                    "Unlan_DT": "12",
                    "getwork_time_1": "2",
                    "getwork_time_2": "3",
                    "Plan_DT_Per": "10",
                    "Unlan_DT_Per": "12",
                    "DT_Per": "12",
                    "number_of_product": "1000",
                    "number_should_of_product_1": "1040",
                    "number_should_of_product_2": "1020",
                    "product_Qty": "900",
                    "Return_Qty": "800",
                    "product_Qty_F": "900",
                    "Availability_A1": "70",
                    "Availability_A2": "75",
                    "Performance_P1": "80",
                    "Performance_P2": "85",
                    "Quality": "90",
                    "Quality_Final": "90",
                    "OEE1": "90",
                    "OEE2": "95",
                    "OEE1_F": "90",
                    "OEE2_F": "95"
                }, {
                    "Month": "Jan",
                    "Plant": "T1" + str(count),
                    "Machine": "Robotic",
                    "Machine_Text": "Robotic",
                    "WorkTime": "2",
                    "Plan_DT": "10",
                    "Unlan_DT": "12",
                    "getwork_time_1": "2",
                    "getwork_time_2": "3",
                    "Plan_DT_Per": "10",
                    "Unlan_DT_Per": "12",
                    "DT_Per": "12",
                    "number_of_product": "1000",
                    "number_should_of_product_1": "1040",
                    "number_should_of_product_2": "1020",
                    "product_Qty": "900",
                    "Return_Qty": "800",
                    "product_Qty_F": "900",
                    "Availability_A1": "70",
                    "Availability_A2": "75",
                    "Performance_P1": "80",
                    "Performance_P2": "85",
                    "Quality": "90",
                    "Quality_Final": "90",
                    "OEE1": "90",
                    "OEE2": "95",
                    "OEE1_F": "90",
                    "OEE2_F": "95"
                }, {
                    "Month": "Jan",
                    "Plant": "T1" + str(count),
                    "Machine": "Robotic",
                    "Machine_Text": "Robotic",
                    "WorkTime": "2",
                    "Plan_DT": "10",
                    "Unlan_DT": "12",
                    "getwork_time_1": "2",
                    "getwork_time_2": "3",
                    "Plan_DT_Per": "10",
                    "Unlan_DT_Per": "12",
                    "DT_Per": "12",
                    "number_of_product": "1000",
                    "number_should_of_product_1": "1040",
                    "number_should_of_product_2": "1020",
                    "product_Qty": "900",
                    "Return_Qty": "800",
                    "product_Qty_F": "900",
                    "Availability_A1": "70",
                    "Availability_A2": "75",
                    "Performance_P1": "80",
                    "Performance_P2": "85",
                    "Quality": "90",
                    "Quality_Final": "90",
                    "OEE1": "90",
                    "OEE2": "95",
                    "OEE1_F": "90",
                    "OEE2_F": "95"
                }, {
                    "Month": "Jan",
                    "Plant": "T1" + str(count),
                    "Machine": "Robotic",
                    "Machine_Text": "Robotic",
                    "WorkTime": "2",
                    "Plan_DT": "10",
                    "Unlan_DT": "12",
                    "getwork_time_1": "2",
                    "getwork_time_2": "3",
                    "Plan_DT_Per": "10",
                    "Unlan_DT_Per": "12",
                    "DT_Per": "12",
                    "number_of_product": "1000",
                    "number_should_of_product_1": "1040",
                    "number_should_of_product_2": "1020",
                    "product_Qty": "900",
                    "Return_Qty": "800",
                    "product_Qty_F": "900",
                    "Availability_A1": "70",
                    "Availability_A2": "75",
                    "Performance_P1": "80",
                    "Performance_P2": "85",
                    "Quality": "90",
                    "Quality_Final": "90",
                    "OEE1": "90",
                    "OEE2": "95",
                    "OEE1_F": "90",
                    "OEE2_F": "95"
                }]
            }, 201          

@app.route('/Report_Yield_API' ,methods=["GET", "POST"])
def Report_Yield_API():
    global count
    q = request.args.get('q')
    print(q)

    if request.method == "POST":
        count+=1
        return redirect(url_for('ReportYield'))
    else:
        return {
                "data": [{
                    "Plant": "T1" + str(count),
                    "Posting_Date": "10/10/2501",
                    "PD_order": "90058064",
                    "Material_number": "232-0149",
                    "Material_Description": "TMF 750 PH PI R2",
                    "WorkCenter": "EFFYTEC9",
                    "Input_Qty": "22080",
                    "Output_Qty": "21904",
                    "Return_Qty": "150",
                    "First_Quality": "P",
                    "Yield": "99.2%",
                    "Final_Yield": "95.5%"

                }, {
                    "Plant": "HHD" ,
                    "Posting_Date": "10/10/2501",
                    "PD_order": "80095485",
                    "Material_number": "232.01",
                    "Material_Description": "TMF - PI",
                    "WorkCenter": "Storage 8T Bay 6 MC-1",
                    "Input_Qty": "8500",
                    "Output_Qty": "8415",
                    "Return_Qty": "",
                    "First_Quality": "P",
                    "Yield": "99.0%",
                    "Final_Yield": "99.0%"
                }, {
                    "Plant": "HHD",
                    "Posting_Date": "10/10/2501",
                    "PD_order": "80095486",
                    "Material_number": "232.01",
                    "Material_Description": "TMF - PI",
                    "WorkCenter": "Storage 8T Bay 6 MC-1",
                    "Input_Qty": "8500",
                    "Output_Qty": "8300",
                    "Return_Qty": "",
                    "First_Quality": "P",
                    "Yield": "97.6%",
                    "Final_Yield": "97.0%"
                }, {
                    "Plant": "TLT",
                    "Posting_Date": "10/10/2501",
                    "PD_order": "90056287",
                    "Material_number": "22C-0306",
                    "Material_Description": "DNK HB 200 GN  R3",
                    "WorkCenter": "Robotic No.5",
                    "Input_Qty": "18048",
                    "Output_Qty": "17720",
                    "Return_Qty": "5000",
                    "First_Quality": "P",
                    "Yield": "98.2%",
                    "Final_Yield": "70.5%"
                }, {
                    "Plant": "TLT",
                    "Posting_Date": "10/10/2501",
                    "PD_order": "90056287",
                    "Material_number": "22C-0306",
                    "Material_Description": "DNK HB 200 GN  R3",
                    "WorkCenter": "Sticker Rotary",
                    "Input_Qty": "18400",
                    "Output_Qty": "18114",
                    "Return_Qty": "",
                    "First_Quality": "P",
                    "Yield": "98.4%",
                    "Final_Yield": "98.4%"
                }, {
                    "Plant": "TLT",
                    "Posting_Date": "10/10/2501",
                    "PD_order": "80090415",
                    "Material_number": "22C.740",
                    "Material_Description": "DNK - HB - GN",
                    "WorkCenter": "Storage Benice 4 tons",
                    "Input_Qty": "4000",
                    "Output_Qty": "3960",
                    "Return_Qty": "",
                    "First_Quality": "P",
                    "Yield": "99.0%",
                    "Final_Yield": "99.0%"
                }]
            }, 201          
            

@app.route('/Report_Yield_Montly_API' ,methods=["GET", "POST"])
def Report_Yield_Montly_API():
    global count
    q = request.args.get('q')
    print(q)

    if request.method == "POST":
        count+=1
        return redirect(url_for('ReportYieldMontly'))
    else:
        return {
                "data": [{
                    "Month": "Sep",
                    "Plant": "T1" + str(count),
                    "Machine": "232-0149",
                    "Machine_text": "TMF 750 PH PI R2",
                    "Input_Qty": "22080",
                    "Output_Qty": "21904",
                    "Return_Qty": "150",
                    "Yield": "99.2%",
                    "Final_Yield": "95.5%"

                }, {
                   "Month": "Sep",
                    "Plant": "T1" + str(count),
                    "Machine": "232-0149",
                    "Machine_text": "TMF 750 PH PI R2",
                    "Input_Qty": "22080",
                    "Output_Qty": "21904",
                    "Return_Qty": "150",
                    "Yield": "99.2%",
                    "Final_Yield": "95.5%"
                }, {
                   "Month": "Sep",
                    "Plant": "T1" + str(count),
                    "Machine": "232-0149",
                    "Machine_text": "TMF 750 PH PI R2",
                    "Input_Qty": "22080",
                    "Output_Qty": "21904",
                    "Return_Qty": "150",
                    "Yield": "99.2%",
                    "Final_Yield": "95.5%"
                }, {
                    "Month": "Sep",
                    "Plant": "T1" + str(count),
                    "Machine": "232-0149",
                    "Machine_text": "TMF 750 PH PI R2",
                    "Input_Qty": "22080",
                    "Output_Qty": "21904",
                    "Return_Qty": "150",
                    "Yield": "99.2%",
                    "Final_Yield": "95.5%"
                }, {
                   "Month": "Sep",
                    "Plant": "T1" + str(count),
                    "Machine": "232-0149",
                    "Machine_text": "TMF 750 PH PI R2",
                    "Input_Qty": "22080",
                    "Output_Qty": "21904",
                    "Return_Qty": "150",
                    "Yield": "99.2%",
                    "Final_Yield": "95.5%"
                }, {
                  "Month": "Sep",
                    "Plant": "T1" + str(count),
                    "Machine": "232-0149",
                    "Machine_text": "TMF 750 PH PI R2",
                    "Input_Qty": "22080",
                    "Output_Qty": "21904",
                    "Return_Qty": "150",
                    "Yield": "99.2%",
                    "Final_Yield": "95.5%"
                }]
            }, 201          
            
            
@app.route('/Report_Overall_Yield_API' ,methods=["GET", "POST"])
def Report_Overall_Yield_API():
    global count
    q = request.args.get('q')
    print(q)

    if request.method == "POST":
        count+=1
        return redirect(url_for('ReportOverallYield'))
    else:
        return {
                "data": [{
                    "Plant": "T1" + str(count),
                    "Posting_Date": "10/10/2501",
                    "FG_PD_order": "90058064",
                    "FG_Material_number": "232-0149",
                    "FG_Material_Description": "TMF 750 PH PI R2",
                    "Bulk_PD_order": "90058064",
                    "Bulk_Material_number": "232-0149",
                    "Bulk_Material_Description": "TMF 750 PH PI R2",
                    "Finishing_yield": "98.5%",
                    "Bulk_yield": "99.0%",
                    "Preprocess_yield": "",
                    "Overall_yield": "69.9%"
                   
                }, {
                   "Plant": "T1" + str(count),
                    "Posting_Date": "10/10/2501",
                    "FG_PD_order": "90058064",
                    "FG_Material_number": "232-0149",
                    "FG_Material_Description": "TMF 750 PH PI R2",
                    "Bulk_PD_order": "90058064",
                    "Bulk_Material_number": "232-0149",
                    "Bulk_Material_Description": "TMF 750 PH PI R2",
                    "Finishing_yield": "98.5%",
                    "Bulk_yield": "99.0%",
                    "Preprocess_yield": "",
                    "Overall_yield": "69.9%"
                }, {
                    "Plant": "T1" + str(count),
                    "Posting_Date": "10/10/2501",
                    "FG_PD_order": "90058064",
                    "FG_Material_number": "232-0149",
                    "FG_Material_Description": "TMF 750 PH PI R2",
                    "Bulk_PD_order": "90058064",
                    "Bulk_Material_number": "232-0149",
                    "Bulk_Material_Description": "TMF 750 PH PI R2",
                    "Finishing_yield": "98.5%",
                    "Bulk_yield": "99.0%",
                    "Preprocess_yield": "",
                    "Overall_yield": "69.9%"
                }, {
                    "Plant": "T1" + str(count),
                    "Posting_Date": "10/10/2501",
                    "FG_PD_order": "90058064",
                    "FG_Material_number": "232-0149",
                    "FG_Material_Description": "TMF 750 PH PI R2",
                    "Bulk_PD_order": "90058064",
                    "Bulk_Material_number": "232-0149",
                    "Bulk_Material_Description": "TMF 750 PH PI R2",
                    "Finishing_yield": "98.5%",
                    "Bulk_yield": "99.0%",
                    "Preprocess_yield": "10.0%",
                    "Overall_yield": "69.9%"
                }]
            }, 201          
            
#-------------------- main --------------------------------------

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True ,port=5001)
