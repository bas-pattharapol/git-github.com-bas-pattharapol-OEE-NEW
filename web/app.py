import email
from re import I
from flask import Flask, render_template, request, redirect, url_for, jsonify,make_response,session,send_file
from flask.sessions import NullSession
import flask_login 
from flask_login.utils import logout_user
from numpy import add_newdoc
import pandas as pd
import pyodbc
import json
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash, check_password_hash
import decimal
from openpyxl.styles import Alignment , Font , PatternFill
import openpyxl
import time 
import babel
import sys

UserLogin = ''
UserLevelLogin = ''
#test


#ddd

class Encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal): return float(obj)
        
class create_dict(dict): 
  
    # __init__ function 
    def __init__(self): 
        self = dict() 
          
    # Function to add key:value 
    def add(self, key, value): 
        self[key] = value

server = "172.30.2.2"
port = 5432
database = "OEE_DB"
username = "sa"
password = "p@ssw0rd"

ansOEE_Plant = 'ALL'
ansOEE_Machines = 'ALL'
ansOEE_Shifts   = 'ALL'
ansOEE_StartDate = ''
ansOEE_StopDate = ''
ansOEE_UserGroup = 'ALL'

ansOEE_Total_Plant = 'ALL'
ansOEE_Total_Machines = 'ALL'
ansOEE_Total_Shifts   = 'ALL'
ansOEE_Total_StartDate = ''
ansOEE_Total_StopDate = ''
ansOEE_Total_UserGroup = 'ALL'

ansOEE_Plant_M = 'ALL'
ansOEE_Machines_M = 'ALL'
ansOEE_Shifts_M   = 'ALL'
ansOEE_StartDate_M = ''
ansOEE_StopDate_M = ''
ansOEE_UserGroup_M = 'ALL'
ansOEE_Month_M = 'ALL'

ansYield_Plant = 'ALL'
ansYield_Machines = 'ALL'
ansYield_Shifts   = 'ALL'
ansYield_StartDate = ''
ansYield_StopDate = ''
ansYield_UserGroup = 'ALL'


where = ''

excelOEE_Plant_M = 'ALL'
excelOEE_Machines_M = 'ALL'
excelOEE_Shifts_M   = 'ALL'
excelOEE_StartDate_M = ''
excelOEE_StopDate_M = ''
excelOEE_UserGroup_M = 'ALL'
excelOEE_Month_M = ''


excelOEE_Total_Plant = 'ALL'
excelOEE_Total_Machines = 'ALL'
excelOEE_Total_Shifts   = 'ALL'
excelOEE_Total_StartDate = ''
excelOEE_Total_StopDate = ''
excelOEE_Total_UserGroup = 'ALL'

excelOEE_Plant = 'ALL'
excelOEE_Machines = 'ALL'
excelOEE_Shifts   = 'ALL'
excelOEE_StartDate = ''
excelOEE_StopDate = ''
excelOEE_UserGroup = 'ALL'

ansOEE_Month_M_Report = ''

excelYield_Plant = 'ALL'
excelYield_Machines = 'ALL'
excelYield_Shifts   = 'ALL'
excelYield_StartDate = ''
excelYield_StopDate = ''
excelYield_UserGroup = 'ALL'
    

app = Flask(__name__)
app.secret_key = '0'
login_manager = flask_login.LoginManager()

login_manager.init_app(app)
users = {}
nameUser = None

count = 3

class User(flask_login.UserMixin):
    pass



            
@login_manager.user_loader
def user_loader(email):
    if email not in users:
        return

    user = User()
    user.id = email
    return user

@login_manager.request_loader
def request_loader(request):
    email = request.form.get('Username')
    if email not in users:
        return

    user = User()
    user.id = email
    return user
    
@app.errorhandler(401)
def custom_401(error):
    return redirect(url_for('login_user'))

@app.before_request
def before_request():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=30)


@app.template_filter()
def format_datetime(value, format='medium'):
    if format == 'full':
        format="EEEE, d. MMMM y 'at' HH:mm"
    elif format == 'medium':
        format="EE dd.MM.y HH:mm"
    return babel.dates.format_datetime(value, format)

@app.route("/API_INF_OEE01", methods=['POST'])
def API_INF_OEE01():
    print(request.get_json())
    data = request.get_json()

    for i in range(0,len(data['Result'])):
        
        print('Plant --> ' ,data['Result'][i]['Plant'] )
        print('PDOrder --> ' ,data['Result'][i]['PDOrder'][4:12] )
        print('MachineID --> ' ,data['Result'][i]['MachineID'] )
        print('Material --> ' ,data['Result'][i]['Material'] )
        print('Description --> ' ,data['Result'][i]['Description'] )
        print('PlanQuantity --> ' ,data['Result'][i]['PlanQuantity'] )
        print('Bacth --> ' ,data['Result'][i]['Bacth'] )
        print('Bulk - Code --> ' ,data['Result'][i]['Code'] )
        print('Bulk - PD_order1 --> ' ,data['Result'][i]['PD_order1'][4:12] )
        print('Bulk - PD_order2 --> ' ,data['Result'][i]['PD_order2'][4:12] )
        print('Bulk - PD_order3 --> ' ,data['Result'][i]['PD_order3'][4:12] )
        print('Bulk - PD_order4 --> ' ,data['Result'][i]['PD_order4'][4:12] )
        print('Bulk - PD_order5 --> ' ,data['Result'][i]['PD_order5'][4:12] )
        print('Bulk - PD_order6 --> ' ,data['Result'][i]['PD_order6'][4:12] )
        print('Bulk - PD_order7 --> ' ,data['Result'][i]['PD_order7'][4:12] )
        print('Bulk - PD_order8 --> ' ,data['Result'][i]['PD_order8'][4:12] )
        print('Bulk - PD_order9 --> ' ,data['Result'][i]['PD_order9'][4:12] )
        print('Bulk - PD_order10 --> ' ,data['Result'][i]['PD_order10'][4:12] )
        
        print("------------------------------------")
        
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        update = cnxn.cursor()
        update.execute('INSERT INTO OEE_DB.dbo.INF_OEE1_V2 (Plant, PDOrder, MachineID, Material, Description, PlanQuantity, Bacth, Code, PD_order1, PD_order2, PD_order3, PD_order4, PD_order5, PD_order6, PD_order7, PD_order8) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)' ,(data['Result'][i]['Plant'],data['Result'][i]['PDOrder'][4:12],data['Result'][i]['MachineID'],data['Result'][i]['Material'],data['Result'][i]['Description'],data['Result'][i]['PlanQuantity'],data['Result'][i]['Bacth'],data['Result'][i]['Code'],data['Result'][i]['PD_order1'][4:12],data['Result'][i]['PD_order2'][4:12],data['Result'][i]['PD_order3'][4:12],data['Result'][i]['PD_order4'][4:12],data['Result'][i]['PD_order5'][4:12],data['Result'][i]['PD_order6'][4:12],data['Result'][i]['PD_order7'][4:12],data['Result'][i]['PD_order8'][4:12]))
        cnxn.commit()
        
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 

@app.route("/API_INF_OEE03", methods=['POST'])
def API_INF_OEE03():
    print(request.get_json())
    data = request.get_json()
    for p in range(0,len(data['Result'])):
        for i in range(0,len(data['Result'][p]['Machine'])):
        
            for j in range(0,len(data['Result'][p]['Machine'][i]['GR_QTY'])):
                print('PDOrder --> ' ,data['Result'][p]['PDOrder'][4:12] )
                print('Machine - ID --> ' ,data['Result'][p]['Machine'][i]['ID'] )
                print('GR_QTY - ID --> ' ,data['Result'][p]['Machine'][i]['GR_QTY'][j]['QTY'] )
                print('GR_QTY - Date --> ' ,data['Result'][p]['Machine'][i]['GR_QTY'][j]['Date'] )
                print('GR_QTY - Time --> ' ,data['Result'][p]['Machine'][i]['GR_QTY'][j]['Time'] )
                
                DateTime =  str(datetime.strptime(data['Result'][p]['Machine'][i]['GR_QTY'][j]['Date'] , '%Y-%m-%d').date())+' ' + data['Result'][p]['Machine'][i]['GR_QTY'][j]['Time']

                cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
                update = cnxn.cursor()
                update.execute('INSERT INTO OEE_DB.dbo.INF_OEE3_V2 (PDOrder,MachineID, QTY, [Date], [Time]) VALUES(?,?,?,?,?)' ,(data['Result'][p]['PDOrder'][4:12],data['Result'][p]['Machine'][i]['ID'],data['Result'][p]['Machine'][i]['GR_QTY'][j]['QTY'],data['Result'][p]['Machine'][i]['GR_QTY'][j]['Date'],DateTime))
                cnxn.commit()
            print("------------------------------------")
        
    
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 

@app.route("/API_INF_OEE04", methods=['POST'])
def API_INF_OEE04(): 
    print(request.get_json())
    data = request.get_json()
    for p in range(0,len(data['Result'])):
        for i in range(0,len(data['Result'][p]['Machine'])):
            print('PDOrder --> ' ,data['Result'][p]['PDOrder'][4:12] )
            print('Machine - ID --> ' ,data['Result'][p]['Machine'][i]['ID'] )
            for j in range(0,len(data['Result'][p]['Machine'][i]['GI'])):
                print('GI - ID --> ' ,data['Result'][p]['Machine'][i]['GI'][j]['QTY'] )
                print('GI - Dep --> ' ,data['Result'][p]['Machine'][i]['GI'][j]['Dep'] )
                print('GI - Date --> ' ,data['Result'][p]['Machine'][i]['GI'][j]['Date'] )
                print('GI - Time --> ' ,data['Result'][p]['Machine'][i]['GI'][j]['Time'] )
                DateTime =  str(datetime.strptime(data['Result'][p]['Machine'][i]['GI'][j]['Date'] ,'%Y-%m-%d').date()) +' ' + data['Result'][p]['Machine'][i]['GI'][j]['Time']

                cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
                update = cnxn.cursor()
                update.execute('INSERT INTO OEE_DB.dbo.INF_OEE4_V2 (PDOrder,MachineID, QTY,Dep ,[Date], [Time]) VALUES(?,?,?,?,?,?)' ,(data['Result'][p]['PDOrder'][4:12],data['Result'][p]['Machine'][i]['ID'],data['Result'][p]['Machine'][i]['GI'][j]['QTY'],data['Result'][p]['Machine'][i]['GI'][j]['Dep'],data['Result'][p]['Machine'][i]['GI'][j]['Date'],DateTime))
                cnxn.commit()
            print("------------------------------------")
        
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 

@app.route("/API_INF_OEE05", methods=['POST'])
def API_INF_OEE05():
    print(request.get_json())
    data = request.get_json()
    for p in range(0,len(data['Result'])):
        for i in range(0,len(data['Result'][p]['Machine'])):
            print('PDOrder --> ' ,data['Result'][p]['PDOrder'][4:12] )
            print('Machine - ID --> ' ,data['Result'][p]['Machine'][i]['ID'] )
            for j in range(0,len(data['Result'][p]['Machine'][i]['Return'])):
                print('Return - ID --> ' ,data['Result'][p]['Machine'][i]['Return'][j]['QTY'] )
                print('Return - Text --> ' ,data['Result'][p]['Machine'][i]['Return'][j]['Text'] )
                print('Return - Date --> ' ,data['Result'][p]['Machine'][i]['Return'][j]['Date'] )
                print('Return - Time --> ' ,data['Result'][p]['Machine'][i]['Return'][j]['Time'] )
                cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
                update = cnxn.cursor()
                update.execute('INSERT INTO OEE_DB.dbo.INF_OEE5_V2 (PDOrder,MachineID, QTY,Text ,[Date], [Time]) VALUES(?,?,?,?,?,?)' ,(data['Result'][p]['PDOrder'][4:12],data['Result'][p]['Machine'][i]['ID'],data['Result'][p]['Machine'][i]['Return'][j]['QTY'],data['Result'][p]['Machine'][i]['Return'][j]['Text'],data['Result'][p]['Machine'][i]['Return'][j]['Date'],data['Result'][p]['Machine'][i]['Return'][j]['Time']))
                cnxn.commit()
            print("------------------------------------")
        
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 

@app.route("/API_RunTime_DownTime", methods=['POST'])
def API_RunTime_DownTime():
    print(request.get_json())
    data = request.get_json()
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cur = conn.cursor()
    cur.execute("DELETE from OEE_DB.dbo.INF_OEE2_V2  WHERE PDOrder = ? AND Operation = ?",(data['Order'],data['Operation']))
    conn.commit()     
    
    for i in range(0,len(data['RunTime'])):
        print("-->> RunTime [",i,"]")
        print('PDOrder --> ' ,data['Order'][4:12] )
        print('Operation --> ' ,data['Operation'])
        print('RunTime - Post_Date --> ' ,data['RunTime'][i]['Post_Date'] )
        print('RunTime - Start_Runtime --> ' ,data['RunTime'][i]['Start_Runtime'] )
        print('RunTime - End_Runtime --> ' ,data['RunTime'][i]['End_Runtime'] )
        print('RunTime - Total_Runtime --> ' ,data['RunTime'][i]['Total_Runtime'] )
        print("------------------------------------")
        DateDate  = str(datetime.strptime(data['RunTime'][i]['Post_Date'] , '%d-%m-%Y').date())
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        update = cnxn.cursor()
        update.execute('INSERT INTO OEE_DB.dbo.INF_OEE2_V2 (PDOrder, TypeTime, Operation, PostDate, StartTime, EndTime, [Min]) VALUES(?,?,?,?,?,?,?)' ,(data['Order'][4:12],"RunTime",data['Operation'],DateDate,data['RunTime'][i]['Start_Runtime'],data['RunTime'][i]['End_Runtime'],data['RunTime'][i]['Total_Runtime']))
        cnxn.commit()
       
        
    for i in range(0,len(data['DonwTime'])):
        print("-->> DonwTime [",i,"]")
        print('PDOrder --> ' ,data['Order'][4:12] )
        print('Operation --> ' ,data['Operation'])
        print('DonwTime - Post_Date --> ' ,data['DonwTime'][i]['Post_Date'] )
        print('DonwTime - Start_Downtime --> ' ,data['DonwTime'][i]['Start_Downtime'] )
        print('DonwTime - End_Downtime --> ' ,data['DonwTime'][i]['End_Downtime'] )
        print('DonwTime - Total_Downtime --> ' ,data['DonwTime'][i]['Total_Downtime'] )
        print('DonwTime - Reason_Var --> ' ,data['DonwTime'][i]['Reason_Var'] )
                    
        print("------------------------------------")
        
        conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        cur1 = conn.cursor() 
        cur1.execute("""SELECT TOP(1) iov.MachineID , ppt.PlannedCode from OEE_DB.dbo.INF_OEE1_V2 iov 
                        INNER JOIN OEE_DB.dbo.PlannedProductionTime ppt
                        ON iov.MachineID = ppt.MachineID AND iov.PDOrder = ? AND ppt.[Date] = ? 
                        order by ppt.[DateTime] DESC 
                    """,(data['Order'][4:12] ,str(datetime.strptime(data['DonwTime'][i]['Post_Date'] , '%d-%m-%Y').date())))
        
        for o in cur1:
            print(o[1])
            conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
            cur = conn.cursor()
            cur.execute("SELECT StartTime , EndTime FROM OEE_DB.dbo.[ShiftCode] WHERE DeleteFlag = 1 AND  ShiftCodeID = ? ",(o[1],))
            print('cur1')
            for m in cur:
                print('cur2')
                oldStartTime = m[0]
        
        
            """
            newdate = datetime.strptime(data['DonwTime'][i]['PostDate'] , '%d-%m-%Y').date() + timedelta(days=-1)                      
            
            print('row.Date',data['DonwTime'][i]['PostDate']) 
            print('newdate',newdate)   
            startDate =  str(newdate) +' ' + str(data['DonwTime'][i]['EndTime']) 
            endDate =  str(datetime.strptime(data['DonwTime'][i]['PostDate'] , '%d-%m-%Y').date()) +' ' + str(data['DonwTime'][i]['StartTime'])
            print(startDate)
            print(endDate)
            """
        
        
        if datetime.strptime(str(data['DonwTime'][i]['Start_Downtime']),'%H:%M:%S') >= datetime.strptime(str(data['DonwTime'][i]['End_Downtime']),'%H:%M:%S'):
            newdate = datetime.strptime(data['DonwTime'][i]['Post_Date'] , '%d-%m-%Y').date() + timedelta(days=1)                      
            
            print('row.Date',data['DonwTime'][i]['Post_Date']) 
            print('newdate',newdate)    
            startDate =  str(datetime.strptime(data['DonwTime'][i]['Post_Date'] , '%d-%m-%Y').date()) +' ' + str(data['DonwTime'][i]['Start_Downtime'])
            endDate =  str(newdate) +' ' + str(data['DonwTime'][i]['End_Downtime'])
        else:
            startDate =  str(datetime.strptime(data['DonwTime'][i]['Post_Date'] , '%d-%m-%Y').date()) +' ' + str(data['DonwTime'][i]['Start_Downtime'])
            endDate =  str(datetime.strptime(data['DonwTime'][i]['Post_Date'] , '%d-%m-%Y').date()) +' ' + str(data['DonwTime'][i]['End_Downtime'])
        print(startDate)
        print(endDate)
        DateDate  = str(datetime.strptime(data['DonwTime'][i]['Post_Date'] , '%d-%m-%Y').date())
 
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        update = cnxn.cursor()
        update.execute('INSERT INTO OEE_DB.dbo.INF_OEE2_V2 (PDOrder, TypeTime, Operation, PostDate, StartTime, EndTime, [Min],DownTimeCode) VALUES(?,?,?,?,?,?,?,?)' ,(data['Order'][4:12],"DonwTime",data['Operation'],DateDate,startDate,endDate,data['DonwTime'][i]['Total_Downtime'],data['DonwTime'][i]['Reason_Var']))
        cnxn.commit()
       
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 
#55
@app.route("/", methods=['GET', 'POST'])
@app.route("/login_user", methods=['GET', 'POST'])
def login_user():        
    
    return render_template('login.html')

@app.route("/sidebar", methods=['GET', 'POST'])
def sidebar():        
    return render_template('sidebar.html')

@app.route("/login_CkPass", methods=['GET', 'POST'])
def login_CkPass():
    if request.method == 'POST':
        
        conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        cur = conn.cursor()
        cur.execute("SELECT * FROM OEE_DB.dbo.[User] WHERE DeleteFlag = 1")

        dataUser = request.form['username']
        print(users)
        for data in cur: 
            print(data)
            if dataUser == data[3]:
                if data[4] == None or  data[4] == '':
                    return render_template('login_NoPass.html',username = data[3])        
                else:
                    return render_template('login_Password.html',username = data[3])   
           
            
        return redirect(url_for('login_user'))

@app.route("/login_addPass/<string:username1>", methods=['GET', 'POST'])
def login_addPass(username1):
    if request.method == 'POST':
        dataPassword = request.form['New_Password']
        NewPassword = generate_password_hash(dataPassword,"sha256")
        print(NewPassword)
        conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID=sa ;PWD=p@ssw0rd')
        cur = conn.cursor()
        cur.execute("UPDATE OEE_DB.dbo.[User] SET Pass = ? WHERE UserName = ?", (NewPassword,username1))
        conn.commit() 
       

    return redirect(url_for('login_user'))

@app.route("/login_Password/<string:username1>", methods=['GET', 'POST'])
def login_Password(username1):
    global UserLogin
    global UserLevelLogin
    if request.method == 'POST':
        dataPassword = request.form['Password']

        conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        cur = conn.cursor()
        cur.execute("SELECT * FROM OEE_DB.dbo.[User] WHERE UserName = ?  AND DeleteFlag = 1", (username1,))

        conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        cur1 = conn.cursor()
        cur1.execute("SELECT * FROM OEE_DB.dbo.[User]  WHERE DeleteFlag = 1")

        email = username1

        for i in cur1:
            users[i[3]] = {'Password' : i[4]}

        print(users)
        
        
        for data in cur: 
            print(data[3])
            Level = data[11]
            Fname_LName = data[5] + ' ' + data[6]
            UserLevelLogin = data[11]
            UserLogin = data[5] + ' ' + data[6]
            print(check_password_hash(data[4], dataPassword))
           
            if check_password_hash(data[4], dataPassword):
                user = User()
                user.id = email
                flask_login.login_user(user)
                    
                global nameUser 
                nameUser = email
                return render_template('login_succeed.html',username = username1,Level=Level,Fname_LName = Fname_LName)   
            else :
                return redirect(url_for('login_user'))

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login_user'))

@app.errorhandler(401)
def custom_401(error):
    return redirect(url_for('login_user'))

@app.errorhandler(404)
def custom_404(error):
    return redirect(url_for('login_user'))


@app.errorhandler(500)
def custom_500(error):
    return redirect(url_for('login_user'))


@app.route('/userManagement/<string:mode>/<string:id>/<string:Level>/<string:Fname_Lname>',methods=['GET', 'POST'])
@flask_login.login_required
def userManagement(mode,id,Level,Fname_Lname):
    if request.method == 'POST':
        if mode == 'update':
           

            UserName = request.form['UserName']
            Fname = request.form['Fname']
            Lname = request.form['Lname']
            UserGroup = request.form['UserGroup']
            UserLevel = request.form['UserLevel']

            Department = request.form['Department']
            
            
            cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
            userManagement = cnxn.cursor()
            userManagement.execute('UPDATE OEE_DB.dbo.[User] SET UserName = ? ,Fname = ? , Lname = ?, UserGroup = ? , UserLevel = ? , UserLevelID = ?, Department = ? ,DeleteFlag = ? , DateTime = GETDATE() WHERE RecordID = ? ',(UserName,Fname,Lname,UserGroup,UserLevel,UserLevel,Department,'1',id ))
            cnxn.commit()
            
        elif mode == "add":

            UserName = request.form['UserName']
            Fname = request.form['Fname']
            Lname = request.form['Lname']
            UserGroup = request.form['UserGroup']
            UserLevel = request.form['UserLevel']

            Department = request.form['Department']
            
            cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
            userManagement = cnxn.cursor()
            userManagement.execute('INSERT INTO OEE_DB.dbo.[User] ( UserName ,Fname , Lname , UserGroup  , UserLevel , UserLevelID, Department,DeleteFlag  ) VALUES(?,?,?,?,?,?,?,?)' ,(UserName,Fname,Lname,UserGroup,UserLevel,UserLevel,Department,'1') )
            cnxn.commit()

        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        update = cnxn.cursor()
        update.execute('INSERT INTO OEE_DB.dbo.EditRecord (EditID,ChangeTopic,NameValue,[User],UserLevel) VALUES(?,?,?,?,?)' ,(8,mode,id,Fname_Lname,Level))
        cnxn.commit()
            
    if mode == "del":
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        userManagement = cnxn.cursor()
        userManagement.execute('UPDATE OEE_DB.dbo.[User] SET DeleteFlag = ?  , DateTime = GETDATE() WHERE RecordID = ? ',(-1,id) )
        cnxn.commit()

        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        update = cnxn.cursor()
        update.execute('INSERT INTO OEE_DB.dbo.EditRecord (EditID,ChangeTopic,NameValue,[User],UserLevel) VALUES(?,?,?,?,?)' ,(8,mode,id,Fname_Lname,Level))
        cnxn.commit()
    
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    userManagement = cnxn.cursor()
    userManagement.execute("""
                           SELECT u.* , ul.Name 
                            FROM OEE_DB.dbo.[User] u 
                            INNER JOIN OEE_DB.dbo.UserLevel ul 
                            ON u.UserLevel = ul.ID AND  u.DeleteFlag = 1 ORDER BY DateTime DESC
                           """)
    
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    Department = cnxn.cursor()
    Department.execute('SELECT DepartmentID FROM OEE_DB.dbo.Department WHERE DeleteFlag = 1 ORDER BY DateTime DESC')
    lenDepartment = 0
    Department_s = []
    for i in Department:
        lenDepartment+=1
        Department_s.append(i)

    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    UserLevel = cnxn.cursor()
    UserLevel.execute('SELECT * FROM OEE_DB.dbo.UserLevel ')
    lenUserLevel = 0
    UserLevel_s = []
    for i in UserLevel:
        lenUserLevel+=1
        UserLevel_s.append(i)
    
        
    return render_template('userManagement.html',userManagement = userManagement,Department=Department_s,lenDepartment=lenDepartment,UserLevel=UserLevel_s,lenUserLevel=lenUserLevel,Level=Level,Fname_Lname=Fname_Lname)

@app.route('/userManagementQC/<string:mode>/<string:id>',methods=['GET', 'POST'])
def userManagementQC(mode,id):
    if request.method == 'POST':
        if mode == 'update':

            UserName = request.form['UserName']
            
            cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
            userManagement = cnxn.cursor()
            userManagement.execute('UPDATE SCADA_DB.dbo.UserQC SET UserName = ? ,DeleteFlag = ? , DateTime = GETDATE() WHERE RecordID = ? ',(UserName,'1',id ))
            cnxn.commit()
            
        elif mode == "add":

            UserName = request.form['UserName']
           
            cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
            userManagement = cnxn.cursor()
            userManagement.execute('INSERT INTO SCADA_DB.dbo.UserQC ( UserName ,DeleteFlag  ) VALUES(?,?)' ,(UserName,'1') )
            cnxn.commit()

    if mode == "del":
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        userManagement = cnxn.cursor()
        userManagement.execute('UPDATE SCADA_DB.dbo.UserQC SET DeleteFlag = ?  , DateTime = GETDATE() WHERE RecordID = ? ',(-1,id) )
        cnxn.commit()


    
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    userManagement = cnxn.cursor()
    userManagement.execute('SELECT * FROM SCADA_DB.dbo.UserQC WHERE DeleteFlag = 1 ORDER BY DateTime DESC')
    
    
        
    return render_template('userManagementQC.html',userManagement = userManagement)



@app.route('/index/<string:username1>/<string:Level>/<string:Fname_Lname>')
@flask_login.login_required
def index(username1,Level,Fname_Lname):
    global count
    count+=1
    print(count)
    return render_template('index.html', username =username1, Level = Level,Fname_Lname = Fname_Lname)

@app.route("/uploadFile/<string:Level>/<string:Fname_Lname>", methods=['GET', 'POST'])
@flask_login.login_required
def uploadFile(Level,Fname_Lname):
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
        #now = datetime.now()
        now = datetime(2021, 5, 17)
      
        conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        cur = conn.cursor()
        cur.execute(' SELECT ShiftCodeID ,StartTime ,EndTime FROM OEE_DB.dbo.ShiftCode ')
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
               
        conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        cur = conn.cursor()
        cur.execute('SELECT PlantID ,PlantName FROM OEE_DB.dbo.Plant WHERE DeleteFlag = 1')
            
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
        
            
        conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        cur = conn.cursor()
        for row in ok_data.itertuples():      
              
            
            if datetime.strptime(str(row.StartTime),'%H:%M:%S') == datetime.strptime('00:00:00','%H:%M:%S') and datetime.strptime(str(row.EndTime),'%H:%M:%S') == datetime.strptime('00:00:00','%H:%M:%S') :
                startDate = str(row.Date) + ' 00:00:00'
                endDate = str(row.Date) + ' 00:00:00'
            elif datetime.strptime(str(row.StartTime),'%H:%M:%S') >= datetime.strptime(str(row.EndTime),'%H:%M:%S'):
                newdate = row.Date + timedelta(days=1)                      
                print('row.Date',row.Date) 
                print('newdate',newdate)    
                startDate =  str(row.Date) +' ' + str(row.StartTime)
                endDate =  str(newdate) +' ' + str(row.EndTime)
            else:
                startDate =  str(row.Date) +' ' + str(row.StartTime)
                endDate =  str(row.Date) +' ' + str(row.EndTime)       
                                                                                   
            postgres_insert_query = ' INSERT INTO OEE_DB.dbo.PlannedProductionTime (PlantID,PlantName,MachineID,MachineName,LoadingDate,Date,PlannedCode,StartTime,EndTime,DeleteFlag) VALUES (?,?,?,?,?,?,?,?,?,?)'
            record_to_insert = (row.PlantID,row.PlantName, row.MachineID, row.Machine,row.Loading,row.Date,row.PlannedCode,startDate,endDate,'1')
            cur.execute(postgres_insert_query, record_to_insert)

        conn.commit()
            
        return redirect(url_for('uploadFile',Level=Level,Fname_Lname=Fname_Lname))
      
    return render_template('uploadFile.html',Level=Level,Fname_Lname=Fname_Lname)

@app.route("/testDataExcel_INF_OEE/<string:io>", methods=['GET', 'POST'])
def testDataExcel_INF_OEE(io):
    if request.method == 'POST':
        if io == '01':
            print(request.files['file'])
            #print(request.files['file2'])
            
            f = request.files['file']
            col = ['Plant','WC_Text','Machine_Text','Machine_ID','Material','Description','PD_Order','UOM_Qty','Plan_quantity','Batch','Bulk_Code','Bulk_PD_order1','Bulk_PD_order2','Bulk_PD_order3','Bulk_PD_order4','Bulk_PD_order5','Bulk_PD_order6','Bulk_PD_order7','Bulk_PD_order8','Bulk_PD_order9','Bulk_PD_order10']
            data_xls = pd.read_excel(f,names=col)
            dimensions = data_xls.shape
            print(data_xls)
            
            
            for i in range(0,dimensions[0]):
                #Plant.append(data_xls['Plant'][i])
                INF_OEE01_Plant = str(data_xls['Plant'][i])
                INF_OEE01_WC_Text = str(data_xls['WC_Text'][i])
                INF_OEE01_Machine_text = str(data_xls['Machine_Text'][i])
                INF_OEE01_Machine_ID = str(data_xls['Machine_ID'][i])
                INF_OEE01_Material = str(data_xls['Material'][i])
                INF_OEE01_Description = str(data_xls['Description'][i])
                INF_OEE01_PD_Order = str(data_xls['PD_Order'][i])
                INF_OEE01_UOM_Qty = str(data_xls['UOM_Qty'][i])
                INF_OEE01_Plan_quantity = str(data_xls['Plan_quantity'][i])
                INF_OEE01_Batch = str(data_xls['Batch'][i])
                INF_OEE01_Bulk_Code = str(data_xls['Bulk_Code'][i])
                INF_OEE01_Bulk_PD_order1 = str(data_xls['Bulk_PD_order1'][i])
                INF_OEE01_Bulk_PD_order2 = str(data_xls['Bulk_PD_order2'][i])
                INF_OEE01_Bulk_PD_order3 = str(data_xls['Bulk_PD_order3'][i])
                INF_OEE01_Bulk_PD_order4 = str(data_xls['Bulk_PD_order4'][i])
                INF_OEE01_Bulk_PD_order5 = str(data_xls['Bulk_PD_order5'][i])
                INF_OEE01_Bulk_PD_order6 = str(data_xls['Bulk_PD_order6'][i])
                INF_OEE01_Bulk_PD_order7 = str(data_xls['Bulk_PD_order7'][i])
                INF_OEE01_Bulk_PD_order8 = str(data_xls['Bulk_PD_order8'][i])
                INF_OEE01_Bulk_PD_order9 = str(data_xls['Bulk_PD_order9'][i])
                INF_OEE01_Bulk_PD_order10 = str(data_xls['Bulk_PD_order10'][i])
                print("INF_OEE01_Plant --> " ,INF_OEE01_Plant )
                print("INF_OEE01_WC_Text --> " ,INF_OEE01_WC_Text )
                print("INF_OEE01_Machine_text --> " ,INF_OEE01_Machine_text )
                print("INF_OEE01_Machine_ID --> " ,INF_OEE01_Machine_ID )
                print("INF_OEE01_Material --> " ,INF_OEE01_Material )
                print("INF_OEE01_Description --> " ,INF_OEE01_Description )
                print("INF_OEE01_PD_Order --> " ,INF_OEE01_PD_Order )
                print("INF_OEE01_UOM_Qty --> " ,INF_OEE01_UOM_Qty )
                print("INF_OEE01_Plan_quantity --> " ,INF_OEE01_Plan_quantity )
                print("INF_OEE01_Batch --> " ,INF_OEE01_Batch )
                print("INF_OEE01_Bulk_Code --> " ,INF_OEE01_Bulk_Code )
                print("INF_OEE01_Bulk_PD_order1 --> " ,INF_OEE01_Bulk_PD_order1 )
                print("INF_OEE01_Bulk_PD_order2 --> " ,INF_OEE01_Bulk_PD_order2 )
                print("INF_OEE01_Bulk_PD_order3 --> " ,INF_OEE01_Bulk_PD_order3 )
                print("INF_OEE01_Bulk_PD_order4 --> " ,INF_OEE01_Bulk_PD_order4 )
                print("INF_OEE01_Bulk_PD_order5 --> " ,INF_OEE01_Bulk_PD_order5 )
                print("INF_OEE01_Bulk_PD_order6 --> " ,INF_OEE01_Bulk_PD_order6 )
                print("INF_OEE01_Bulk_PD_order7 --> " ,INF_OEE01_Bulk_PD_order7 )
                print("INF_OEE01_Bulk_PD_order8 --> " ,INF_OEE01_Bulk_PD_order8 )
                print("INF_OEE01_Bulk_PD_order9 --> " ,INF_OEE01_Bulk_PD_order9 )
                print("INF_OEE01_Bulk_PD_order10 --> " ,INF_OEE01_Bulk_PD_order10 )
            
                cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
                INSERT_INF_OEE01 = cnxn.cursor()
                INSERT_INF_OEE01.execute('INSERT INTO OEE_DB.dbo.INF_OEE01 (Plant,W_CText,Machine_Text,MachineID,Material,Description,PDOrder,UOMQty,PlanQuantity,Batch,BulkCode,BulkPDOrder1,BulkPDOrder2,BulkPDOrder3,BulkPDOrder4,BulkPDOrder5,BulkPDOrder6,BulkPDOrder7,BulkPDOrder8,BulkPDOrder9,BulkPDOrder10) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)' ,( INF_OEE01_Plant  , INF_OEE01_WC_Text , INF_OEE01_Machine_text  , INF_OEE01_Machine_ID  , INF_OEE01_Material  , INF_OEE01_Description,INF_OEE01_PD_Order,INF_OEE01_UOM_Qty,INF_OEE01_Plan_quantity,INF_OEE01_Batch,INF_OEE01_Bulk_Code,INF_OEE01_Bulk_PD_order1,INF_OEE01_Bulk_PD_order2,INF_OEE01_Bulk_PD_order3,INF_OEE01_Bulk_PD_order4,INF_OEE01_Bulk_PD_order5,INF_OEE01_Bulk_PD_order6,INF_OEE01_Bulk_PD_order7,INF_OEE01_Bulk_PD_order8,INF_OEE01_Bulk_PD_order9,INF_OEE01_Bulk_PD_order10 ))
                cnxn.commit()
            

        elif io == '02':
            print(request.files['file'])
            #print(request.files['file2'])
            
            f = request.files['file']
            col = ['Plant','WC_Text','Machine_Text','Machine_ID','Material','Description','PD_Order','UOM_Qty','Plan_quantity','Batch_Estimate','Down_time_code_1','Down_time_description_1','Hrs_1','Down_time_code_2','Down_time_description_2','Hrs_2','Down_time_code_3','Down_time_description_3','Hrs_3','Down_time_code_4','Down_time_description_4','Hrs_4','Down_time_code_5','Down_time_description_5','Hrs_5']
            data_xls = pd.read_excel(f,names=col)
            dimensions = data_xls.shape
            print(data_xls)
            
            
            for i in range(0,dimensions[0]):
                #Plant.append(data_xls['Plant'][i])
                INF_OEE02_Plant = str(data_xls['Plant'][i])
                INF_OEE02_WC_Text =str(data_xls['WC_Text'][i])
                INF_OEE02_Machine_text = str(data_xls['Machine_Text'][i])
                INF_OEE02_Machine_ID = str(data_xls['Machine_ID'][i])
                INF_OEE02_Material = str(data_xls['Material'][i])
                INF_OEE02_Description = str(data_xls['Description'][i])
                INF_OEE02_PD_Order = str(data_xls['PD_Order'][i])
                INF_OEE02_UOM_Qty = str(data_xls['UOM_Qty'][i])
                INF_OEE02_Plan_quantity = str(data_xls['Plan_quantity'][i])
                INF_OEE02_Batch_Estimate = str(data_xls['Batch_Estimate'][i])
                INF_OEE02_Down_time_code1  = str(data_xls['Down_time_code_1'][i])
                INF_OEE02_Down_time_description1 = str(data_xls['Down_time_description_1'][i])
                INF_OEE02_Hrs1 = str(data_xls['Hrs_1'][i])
                INF_OEE02_Down_time_code2  = str(data_xls['Down_time_code_2'][i])
                INF_OEE02_Down_time_description2= str(data_xls['Down_time_description_2'][i])
                INF_OEE02_Hrs2 = str(data_xls['Hrs_2'][i])
                INF_OEE02_Down_time_code3  = str(data_xls['Down_time_code_3'][i])
                INF_OEE02_Down_time_description3 = str(data_xls['Down_time_description_3'][i])
                INF_OEE02_Hrs3 = str(data_xls['Hrs_3'][i])
                INF_OEE02_Down_time_code4  = str(data_xls['Down_time_code_4'][i])
                INF_OEE02_Down_time_description4 = str(data_xls['Down_time_description_4'][i])
                INF_OEE02_Hrs4 = str(data_xls['Hrs_4'][i])
                INF_OEE02_Down_time_code5  = str(data_xls['Down_time_code_5'][i])
                INF_OEE02_Down_time_description5 = str(data_xls['Down_time_description_5'][i])
                INF_OEE02_Hrs5 = str(data_xls['Hrs_5'][i])
                

                
                print("INF_OEE02_Plant --> " ,INF_OEE02_Plant )
                print("INF_OEE02_WC_Text --> " ,INF_OEE02_WC_Text )
                print("INF_OEE02_Machine_text --> " ,INF_OEE02_Machine_text )
                print("INF_OEE02_Machine_ID --> " ,INF_OEE02_Machine_ID )
                print("INF_OEE02_Material --> " ,INF_OEE02_Material )
                print("INF_OEE02_Description --> " ,INF_OEE02_Description )
                print("INF_OEE02_PD_Order --> " ,INF_OEE02_PD_Order )
                print("INF_OEE02_UOM_Qty --> " ,INF_OEE02_UOM_Qty )
                print("INF_OEE02_Plan_quantity --> " ,INF_OEE02_Plan_quantity )
                print("INF_OEE02_Batch_Estimate --> " ,INF_OEE02_Batch_Estimate )
                print("INF_OEE02_Down_time_code1 --> " ,INF_OEE02_Down_time_code1 )
                print("INF_OEE02_Down_time_description1 --> " ,INF_OEE02_Down_time_description1 )
                print("INF_OEE02_Hrs1 --> " ,INF_OEE02_Hrs1 )
                print("INF_OEE02_Down_time_code2 --> " ,INF_OEE02_Down_time_code2 )
                print("INF_OEE02_Down_time_description2 --> " ,INF_OEE02_Down_time_description2 )
                print("INF_OEE02_Hrs2 --> " ,INF_OEE02_Hrs2 )
                print("INF_OEE02_Down_time_code3 --> " ,INF_OEE02_Down_time_code3 )
                print("INF_OEE02_Down_time_description3 --> " ,INF_OEE02_Down_time_description3 )
                print("INF_OEE02_Hrs3 --> " ,INF_OEE02_Hrs3 )
                print("INF_OEE02_Down_time_code4 --> " ,INF_OEE02_Down_time_code4 )
                print("INF_OEE02_Down_time_description4 --> " ,INF_OEE02_Down_time_description4 )
                print("INF_OEE02_Hrs4 --> " ,INF_OEE02_Hrs4 )
                print("INF_OEE02_Down_time_code5 --> " ,INF_OEE02_Down_time_code5 )
                print("INF_OEE02_Down_time_description5 --> " ,INF_OEE02_Down_time_description5 )
                print("INF_OEE02_Hrs5 --> " ,INF_OEE02_Hrs5 )
                
                cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
                INSERT_INF_OEE02 = cnxn.cursor()
                INSERT_INF_OEE02.execute('INSERT INTO OEE_DB.dbo.INF_OEE02 (Plant,W_CText,Machine_Text,MachineID,Material,Description,PDOrder,UOMQty,PlanQuantity,BatchEstimate,DownTimeCode1,DownTimeDescription1,Hrs1,DownTimeCode2,DownTimeDescription2,Hrs2,DownTimeCode3,DownTimeDescription3,Hrs3,DownTimeCode4,DownTimeDescription4,Hrs4,DownTimeCode5,DownTimeDescription5,Hrs5) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)' ,( INF_OEE02_Plant  , INF_OEE02_WC_Text , INF_OEE02_Machine_text  , INF_OEE02_Machine_ID  , INF_OEE02_Material  , INF_OEE02_Description,INF_OEE02_PD_Order,INF_OEE02_UOM_Qty,INF_OEE02_Plan_quantity,INF_OEE02_Batch_Estimate,INF_OEE02_Down_time_code1,INF_OEE02_Down_time_description1,INF_OEE02_Hrs1,INF_OEE02_Down_time_code2,INF_OEE02_Down_time_description2,INF_OEE02_Hrs2,INF_OEE02_Down_time_code3,INF_OEE02_Down_time_description3,INF_OEE02_Hrs3,INF_OEE02_Down_time_code4,INF_OEE02_Down_time_description4,INF_OEE02_Hrs4,INF_OEE02_Down_time_code5,INF_OEE02_Down_time_description5,INF_OEE02_Hrs5))
                cnxn.commit()
            
        elif io == '03':
            print(request.files['file'])
            #print(request.files['file2'])
            
            f = request.files['file']
            col = ['Plant','WC_Text','Machine_Text','Machine_ID','Material','Description','PD_Order','Batch_No','Tag_No','Pallet_No','GR_QTY','Status','GR_Date','GR_Time']
            data_xls = pd.read_excel(f,names=col)
            dimensions = data_xls.shape
            print(data_xls)
            
            for i in range(0,dimensions[0]):
                #Plant.append(data_xls['Plant'][i])
                INF_OEE03_Plant = str(data_xls['Plant'][i])
                INF_OEE03_WC_Text =str(data_xls['WC_Text'][i])
                INF_OEE03_Machine_text = str(data_xls['Machine_Text'][i])
                INF_OEE03_Machine_ID = str(data_xls['Machine_ID'][i])
                INF_OEE03_Material = str(data_xls['Material'][i])
                INF_OEE03_Description = str(data_xls['Description'][i])
                INF_OEE03_PD_Order = str(data_xls['PD_Order'][i])
                INF_OEE03_Batch_No = str(data_xls['Batch_No'][i])
                INF_OEE03_Tag_No = str(data_xls['Tag_No'][i])
                INF_OEE03_Pallet_No = str(data_xls['Pallet_No'][i])
                INF_OEE03_GR_QTY = str(data_xls['GR_QTY'][i])
                INF_OEE03_Status = str(data_xls['Status'][i])
                INF_OEE03_GR_Date = str(data_xls['GR_Date'][i])
                INF_OEE03_GR_Time = str(data_xls['GR_Time'][i])
                
                print("INF_OEE03_Plant --> " ,INF_OEE03_Plant )
                print("INF_OEE03_WC_Text --> " ,INF_OEE03_WC_Text )
                print("INF_OEE03_Machine_text --> " ,INF_OEE03_Machine_text )
                print("INF_OEE03_Machine_ID --> " ,INF_OEE03_Machine_ID )
                print("INF_OEE03_Material --> " ,INF_OEE03_Material )
                print("INF_OEE03_Description --> " ,INF_OEE03_Description )
                print("INF_OEE03_PD_Order --> " ,INF_OEE03_PD_Order )
                print("INF_OEE03_Batch_No --> " ,INF_OEE03_Batch_No )
                print("INF_OEE03_Tag_No --> " ,INF_OEE03_Tag_No )
                print("INF_OEE03_Pallet_No --> " ,INF_OEE03_Pallet_No )
                print("INF_OEE03_GR_QTY --> " ,INF_OEE03_GR_QTY )
                print("INF_OEE03_Status --> " ,INF_OEE03_Status )
                print("INF_OEE03_GR_Date --> " ,INF_OEE03_GR_Date )
                print("INF_OEE03_GR_Time --> " ,INF_OEE03_GR_Time )
                
                cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
                INSERT_INF_OEE03 = cnxn.cursor()
                INSERT_INF_OEE03.execute('INSERT INTO OEE_DB.dbo.INF_OEE03 (Plant,W_CText,Machine_Text,MachineID,Material,Description,PDOrder,BatchNo,TagNo,PalletNo,GR_QTY_EA,Status,GRDate,GRTime) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)' ,( INF_OEE03_Plant  , INF_OEE03_WC_Text , INF_OEE03_Machine_text  , INF_OEE03_Machine_ID  , INF_OEE03_Material  , INF_OEE03_Description,INF_OEE03_PD_Order,INF_OEE03_Batch_No,INF_OEE03_Tag_No,INF_OEE03_Pallet_No,INF_OEE03_GR_QTY,INF_OEE03_Status,INF_OEE03_GR_Date,INF_OEE03_GR_Time))
                cnxn.commit()
                
        elif io == '04':
            print(request.files['file'])
            #print(request.files['file2'])
            
            f = request.files['file']
            col = ['Plant','WC_Text','Machine_Text','Machine_ID','Material','Description','PD_Order','Date','QC_time','QC_Qty','GR_Dep']
            data_xls = pd.read_excel(f,names=col)
            dimensions = data_xls.shape
            print(data_xls)
            
            for i in range(0,dimensions[0]):
                #Plant.append(data_xls['Plant'][i])
                INF_OEE04_Plant = str(data_xls['Plant'][i])
                INF_OEE04_WC_Text =str(data_xls['WC_Text'][i])
                INF_OEE04_Machine_text = str(data_xls['Machine_Text'][i])
                INF_OEE04_Machine_ID = str(data_xls['Machine_ID'][i])
                INF_OEE04_Material = str(data_xls['Material'][i])
                INF_OEE04_Description = str(data_xls['Description'][i])
                INF_OEE04_PD_Order = str(data_xls['PD_Order'][i])
                INF_OEE04_Date = str(data_xls['Date'][i])
                INF_OEE04_QC_time = str(data_xls['QC_time'][i])
                INF_OEE04_QC_Qty = str(data_xls['QC_Qty'][i])
                INF_OEE04_GR_Dep = str(data_xls['GR_Dep'][i])
               
                
                print("INF_OEE03_Plant --> " ,INF_OEE04_Plant )
                print("INF_OEE03_WC_Text --> " ,INF_OEE04_WC_Text )
                print("INF_OEE03_Machine_text --> " ,INF_OEE04_Machine_text )
                print("INF_OEE03_Machine_ID --> " ,INF_OEE04_Machine_ID )
                print("INF_OEE03_Material --> " ,INF_OEE04_Material )
                print("INF_OEE03_Description --> " ,INF_OEE04_Description )
                print("INF_OEE03_PD_Order --> " ,INF_OEE04_PD_Order )
                print("INF_OEE04_Date --> " ,INF_OEE04_Date )
                print("INF_OEE04_QC_time --> " ,INF_OEE04_QC_time )
                print("INF_OEE04_QC_Qty --> " ,INF_OEE04_QC_Qty )
                print("INF_OEE04_GR_Dep --> " ,INF_OEE04_GR_Dep )
                
                
                cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
                INSERT_INF_OEE04 = cnxn.cursor()
                INSERT_INF_OEE04.execute('INSERT INTO OEE_DB.dbo.INF_OEE04 (Plant,W_CText,Machine_Text,MachineID,Material,Description,PDOrder,Date,QCTime,QC_QTY,GR_Dep) VALUES(?,?,?,?,?,?,?,?,?,?,?)' ,( INF_OEE04_Plant  , INF_OEE04_WC_Text , INF_OEE04_Machine_text  , INF_OEE04_Machine_ID  , INF_OEE04_Material  , INF_OEE04_Description,INF_OEE04_PD_Order,INF_OEE04_Date,INF_OEE04_QC_time,INF_OEE04_QC_Qty,INF_OEE04_GR_Dep))
                cnxn.commit()
        else:
            io = "None - Error"
      
    return render_template('testDataExcel.html',io=io)

@app.route('/Data_API') 
def Data_API():
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    workMachine = cnxn.cursor()
    workMachine.execute("""SELECT RecordID ,DateTime , PlantName,MachineID,MachineName,PlannedCode,Date,StartTime,EndTime FROM OEE_DB.dbo.PlannedProductionTime  AS Q
                            WHERE DateTime >= (
                                SELECT MAX(DateTime)
                                FROM OEE_DB.dbo.PlannedProductionTime
                                WHERE MachineID = Q.MachineID AND Date = Q.Date
                            )

                            order by Date asc """)
    payload = []
    content = {}
    for result in workMachine:
        content = {'PlantName': result[2], 'MachineID': str(result[3]), 'MachineName': result[4],'PlannedCode': result[5],'Date': str(result[6]),'StartTime': str(result[7]),'EndTime': str(result[8])}
        payload.append(content)
        content = {}
    #print(payload)
    return json.dumps({"data":payload}, cls = Encoder), 201


@app.route('/DataTableShift')
@flask_login.login_required
def DataTableShift():
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    MachineID = cnxn.cursor()
    MachineID.execute('SELECT MachineID FROM OEE_DB.dbo.Machines WHERE DeleteFlag = 1')
    MachineID_s = []
    len_Machine = 0
    for i in MachineID:
        len_Machine+=1
        MachineID_s.append(i)
        
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    MachineName = cnxn.cursor()
    MachineName.execute('SELECT MachineName FROM OEE_DB.dbo.Machines WHERE DeleteFlag = 1')
    
    MachineName_s = []
    for i in MachineName:
        MachineName_s.append(i)
       
    print(MachineID_s)         
    print(MachineName_s)
    
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    workMachine = cnxn.cursor()
    workMachine.execute("""SELECT RecordID ,DateTime , PlantName,MachineID,MachineName,PlannedCode,Date,StartTime,EndTime FROM OEE_DB.dbo.PlannedProductionTime  AS Q
                            WHERE DateTime >= (
                                SELECT MAX(DateTime)
                                FROM OEE_DB.dbo.PlannedProductionTime
                                WHERE MachineID = Q.MachineID AND Date = Q.Date
                            )
                            order by Date asc """)

    
    
    return render_template('DataTableShift.html',Machines = workMachine,MachineID_s= MachineID_s,MachineName_s=MachineName_s,len_Machine=len_Machine)

@app.route('/dashboard')
@flask_login.login_required
def dashboard():
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    data = cnxn.cursor()
    data.execute("SELECT * FROM OEE_DB.dbo.dashboard_METRICS")
    for i in data:
        HHD_OEE1 = float("{:.2f}".format(i[0] *100))
        TLT_OEE1 = float("{:.2f}".format(i[1] *100))
        Total_OEE1 = float("{:.2f}".format(i[2] *100))
        HHD_OEE2 = float("{:.2f}".format(i[3] *100)) 
        TLT_OEE2 = float("{:.2f}".format(i[4] *100))
        Total_OEE2 = float("{:.2f}".format(i[5] *100))
        HHD_Yield = float("{:.2f}".format(i[6] *100))
        TLT_Yield = float("{:.2f}".format(i[7] *100))
        Total_Yield = float("{:.2f}".format(i[8] *100))
        
    try:
        return render_template('Metrics.html',HHD_OEE1=HHD_OEE1,TLT_OEE1=TLT_OEE1,Total_OEE1=Total_OEE1,
                            HHD_OEE2=HHD_OEE2,TLT_OEE2=TLT_OEE2,Total_OEE2=Total_OEE2,
                            HHD_Yield=HHD_Yield,TLT_Yield=TLT_Yield,Total_Yield=Total_Yield)
    except:
        return render_template('Metrics.html',HHD_OEE1=0,TLT_OEE1=0,Total_OEE1=0,
                           HHD_OEE2=0,TLT_OEE2=0,Total_OEE2=0,
                           HHD_Yield=0,TLT_Yield=0,Total_Yield=0)

@app.route('/oee_Total/<string:oeemenu>', methods=['GET', 'POST'])
@flask_login.login_required
def oee_Total(oeemenu):
    addPlant = ''
    addYear = '2022'
    
    if request.method == 'POST':
        oeemenu = request.form['oeeMenu']
        selectPlant = request.form['selectPlant']
        
        addYear= str(request.form['SelectYear'])
        
        if selectPlant == 'ALL':
            addPlant = ''
        elif selectPlant == 'TLT':
            addPlant = "AND PlantName ='TLT' " 
        elif selectPlant == 'HHD':
            addPlant = "AND PlantName ='HHD' " 
        
    
    print(oeemenu)
    print(addPlant)
    print(addYear)
            
        
    if oeemenu == 'OEE1':
        print("""
                SELECT 
                    (SELECT ROUND(OEE1FinalCalculation*100,2) FROM OEE_DB.dbo.OEEMonthlyReport WHERE Monthly = 'January """ +addYear+"""'""" +addPlant +""" ) as January,""")
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        data = cnxn.cursor()
        data.execute("""
                SELECT 
                    (SELECT ROUND(OEE1FinalCalculation*100,2) FROM OEE_DB.dbo.OEEMonthlyReport WHERE Monthly = 'January """ +addYear+"""'""" +addPlant +""" ) as January,
                    (SELECT ROUND(OEE1FinalCalculation*100,2) FROM OEE_DB.dbo.OEEMonthlyReport WHERE Monthly = 'February """ +addYear+"""'""" +addPlant +"""  ) as February,
                    (SELECT ROUND(OEE1FinalCalculation*100,2) FROM OEE_DB.dbo.OEEMonthlyReport WHERE Monthly = 'March """ +addYear+"""'""" +addPlant +""" ) as March,
                    (SELECT ROUND(OEE1FinalCalculation*100,2) FROM OEE_DB.dbo.OEEMonthlyReport WHERE Monthly = 'April """ +addYear+"""'""" +addPlant +"""  ) as April,
                    (SELECT ROUND(OEE1FinalCalculation*100,2) FROM OEE_DB.dbo.OEEMonthlyReport WHERE Monthly = 'May """ +addYear+"""'""" +addPlant +"""  ) as May,
                    (SELECT ROUND(OEE1FinalCalculation*100,2) FROM OEE_DB.dbo.OEEMonthlyReport WHERE Monthly = 'June """ +addYear+"""'""" +addPlant +"""  ) as June,
                    (SELECT ROUND(OEE1FinalCalculation*100,2) FROM OEE_DB.dbo.OEEMonthlyReport WHERE Monthly = 'July """ +addYear+"""'""" +addPlant +"""  ) as July,
                    (SELECT ROUND(OEE1FinalCalculation*100,2) FROM OEE_DB.dbo.OEEMonthlyReport WHERE Monthly = 'August """ +addYear+"""'""" +addPlant +"""  ) as August,
                    (SELECT ROUND(OEE1FinalCalculation*100,2) FROM OEE_DB.dbo.OEEMonthlyReport WHERE Monthly = 'September """ +addYear+"""'""" +addPlant +"""  ) as September,
                    (SELECT ROUND(OEE1FinalCalculation*100,2) FROM OEE_DB.dbo.OEEMonthlyReport WHERE Monthly = 'October """ +addYear+"""'""" +addPlant +"""  ) as October,
                    (SELECT ROUND(OEE1FinalCalculation*100,2) FROM OEE_DB.dbo.OEEMonthlyReport WHERE Monthly = 'November """ +addYear+"""'""" +addPlant +"""  ) as November,
                    (SELECT ROUND(OEE1FinalCalculation*100,2) FROM OEE_DB.dbo.OEEMonthlyReport WHERE Monthly = 'December """ +addYear+"""'""" +addPlant +"""  ) as December

                    """)
        
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        data1 = cnxn.cursor()
        data1.execute("""
                SELECT 
                    (SELECT ROUND(Per_PantDownTime*100,2) FROM OEE_DB.dbo.OEEMonthlyReport WHERE Monthly = 'January """ +addYear+"""'""" +addPlant +""" ) as January,
                    (SELECT ROUND(Per_PantDownTime*100,2) FROM OEE_DB.dbo.OEEMonthlyReport WHERE Monthly = 'February """ +addYear+"""'""" +addPlant +""" ) as February,
                    (SELECT ROUND(Per_PantDownTime*100,2) FROM OEE_DB.dbo.OEEMonthlyReport WHERE Monthly = 'March """ +addYear+"""'""" +addPlant +""" ) as March,
                    (SELECT ROUND(Per_PantDownTime*100,2) FROM OEE_DB.dbo.OEEMonthlyReport WHERE Monthly = 'April """ +addYear+"""'""" +addPlant +""" ) as April,
                    (SELECT ROUND(Per_PantDownTime*100,2) FROM OEE_DB.dbo.OEEMonthlyReport WHERE Monthly = 'May """ +addYear+"""'""" +addPlant +""" ) as May,
                    (SELECT ROUND(Per_PantDownTime*100,2) FROM OEE_DB.dbo.OEEMonthlyReport WHERE Monthly = 'June """ +addYear+"""'""" +addPlant +""" ) as June,
                    (SELECT ROUND(Per_PantDownTime*100,2) FROM OEE_DB.dbo.OEEMonthlyReport WHERE Monthly = 'July """ +addYear+"""'""" +addPlant +""" ) as July,
                    (SELECT ROUND(Per_PantDownTime*100,2) FROM OEE_DB.dbo.OEEMonthlyReport WHERE Monthly = 'August """ +addYear+"""'""" +addPlant +""" ) as August,
                    (SELECT ROUND(Per_PantDownTime*100,2) FROM OEE_DB.dbo.OEEMonthlyReport WHERE Monthly = 'September """ +addYear+"""'""" +addPlant +""") as September,
                    (SELECT ROUND(Per_PantDownTime*100,2) FROM OEE_DB.dbo.OEEMonthlyReport WHERE Monthly = 'October """ +addYear+"""'""" +addPlant +""" ) as October,
                    (SELECT ROUND(Per_PantDownTime*100,2) FROM OEE_DB.dbo.OEEMonthlyReport WHERE Monthly = 'November """ +addYear+"""'""" +addPlant +""" ) as November,
                    (SELECT ROUND(Per_PantDownTime*100,2) FROM OEE_DB.dbo.OEEMonthlyReport WHERE Monthly = 'December """ +addYear+"""'""" +addPlant +""" ) as December

                    """)
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        oee = cnxn.cursor()
        oee.execute("""
                    SELECT ROUND(AVG(OEE1FinalCalculation)*100,0) FROM OEE_DB.dbo.OEEMonthlyReport WHERE DATENAME(YEAR , DateTime) = DATENAME(YEAR , '""" +addYear+"""')""" +addPlant +"""
                    """)
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        oee_a = cnxn.cursor()
        oee_a.execute("""
                    SELECT ROUND(AVG(OEE_A1)*100,0) FROM OEE_DB.dbo.OEEMonthlyReport WHERE DATENAME(YEAR , DateTime) = DATENAME(YEAR , '""" +addYear+"""')""" +addPlant +"""
                    """)
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        oee_p = cnxn.cursor()
        oee_p.execute("""
                    SELECT ROUND(AVG(OEE_P1)*100,0) FROM OEE_DB.dbo.OEEMonthlyReport WHERE DATENAME(YEAR , DateTime) = DATENAME(YEAR , '""" +addYear+"""')""" +addPlant +"""
                    """)
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        oee_q = cnxn.cursor()
        oee_q.execute("""
                    SELECT ROUND(AVG(OEE_Q_Final)*100,0) FROM OEE_DB.dbo.OEEMonthlyReport WHERE DATENAME(YEAR , DateTime) = DATENAME(YEAR , '""" +addYear+"""')""" +addPlant +"""
                    """)
        
                    
    if oeemenu == 'OEE2':
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        data = cnxn.cursor()
        data.execute("""
                SELECT 
                    (SELECT ROUND(OEE2FinalCalculation*100,2) FROM OEE_DB.dbo.OEEMonthlyReport WHERE Monthly = 'January """ +addYear+"""'""" +addPlant +""" ) as January,
                    (SELECT ROUND(OEE2FinalCalculation*100,2) FROM OEE_DB.dbo.OEEMonthlyReport WHERE Monthly = 'February """ +addYear+"""'""" +addPlant +""" ) as February,
                    (SELECT ROUND(OEE2FinalCalculation*100,2) FROM OEE_DB.dbo.OEEMonthlyReport WHERE Monthly = 'March """ +addYear+"""'""" +addPlant +""" ) as March,
                    (SELECT ROUND(OEE2FinalCalculation*100,2) FROM OEE_DB.dbo.OEEMonthlyReport WHERE Monthly = 'April """ +addYear+"""'""" +addPlant +""" ) as April,
                    (SELECT ROUND(OEE2FinalCalculation*100,2) FROM OEE_DB.dbo.OEEMonthlyReport WHERE Monthly = 'May """ +addYear+"""'""" +addPlant +""" ) as May,
                    (SELECT ROUND(OEE2FinalCalculation*100,2) FROM OEE_DB.dbo.OEEMonthlyReport WHERE Monthly = 'June """ +addYear+"""'""" +addPlant +""" ) as June,
                    (SELECT ROUND(OEE2FinalCalculation*100,2) FROM OEE_DB.dbo.OEEMonthlyReport WHERE Monthly = 'July """ +addYear+"""'""" +addPlant +""" ) as July,
                    (SELECT ROUND(OEE2FinalCalculation*100,2) FROM OEE_DB.dbo.OEEMonthlyReport WHERE Monthly = 'August """ +addYear+"""'""" +addPlant +""" ) as August,
                    (SELECT ROUND(OEE2FinalCalculation*100,2) FROM OEE_DB.dbo.OEEMonthlyReport WHERE Monthly = 'September """ +addYear+"""'""" +addPlant +""" ) as September,
                    (SELECT ROUND(OEE2FinalCalculation*100,2) FROM OEE_DB.dbo.OEEMonthlyReport WHERE Monthly = 'October """ +addYear+"""'""" +addPlant +""" ) as October,
                    (SELECT ROUND(OEE2FinalCalculation*100,2) FROM OEE_DB.dbo.OEEMonthlyReport WHERE Monthly = 'November """ +addYear+"""'""" +addPlant +""" ) as November,
                    (SELECT ROUND(OEE2FinalCalculation*100,2) FROM OEE_DB.dbo.OEEMonthlyReport WHERE Monthly = 'December """ +addYear+"""'""" +addPlant +""" ) as December

                    """)
        
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        data1 = cnxn.cursor()
        data1.execute("""
                SELECT 
                    (SELECT ROUND(Per_PantDownTime2*100,2) FROM OEE_DB.dbo.OEEMonthlyReport WHERE Monthly = 'January """ +addYear+"""'""" +addPlant +""" ) as January,
                    (SELECT ROUND(Per_PantDownTime2*100,2) FROM OEE_DB.dbo.OEEMonthlyReport WHERE Monthly = 'February """ +addYear+"""'""" +addPlant +""" ) as February,
                    (SELECT ROUND(Per_PantDownTime2*100,2) FROM OEE_DB.dbo.OEEMonthlyReport WHERE Monthly = 'March """ +addYear+"""'""" +addPlant +""" ) as March,
                    (SELECT ROUND(Per_PantDownTime2*100,2) FROM OEE_DB.dbo.OEEMonthlyReport WHERE Monthly = 'April """ +addYear+"""'""" +addPlant +""" ) as April,
                    (SELECT ROUND(Per_PantDownTime2*100,2) FROM OEE_DB.dbo.OEEMonthlyReport WHERE Monthly = 'May """ +addYear+"""'""" +addPlant +""" ) as May,
                    (SELECT ROUND(Per_PantDownTime2*100,2) FROM OEE_DB.dbo.OEEMonthlyReport WHERE Monthly = 'June """ +addYear+"""'""" +addPlant +""" ) as June,
                    (SELECT ROUND(Per_PantDownTime2*100,2) FROM OEE_DB.dbo.OEEMonthlyReport WHERE Monthly = 'July """ +addYear+"""'""" +addPlant +""" ) as July,
                    (SELECT ROUND(Per_PantDownTime2*100,2) FROM OEE_DB.dbo.OEEMonthlyReport WHERE Monthly = 'August """ +addYear+"""'""" +addPlant +""" ) as August,
                    (SELECT ROUND(Per_PantDownTime2*100,2) FROM OEE_DB.dbo.OEEMonthlyReport WHERE Monthly = 'September """ +addYear+"""'""" +addPlant +""" ) as September,
                    (SELECT ROUND(Per_PantDownTime2*100,2) FROM OEE_DB.dbo.OEEMonthlyReport WHERE Monthly = 'October """ +addYear+"""'""" +addPlant +""" ) as October,
                    (SELECT ROUND(Per_PantDownTime2*100,2) FROM OEE_DB.dbo.OEEMonthlyReport WHERE Monthly = 'November """ +addYear+"""'""" +addPlant +""" ) as November,
                    (SELECT ROUND(Per_PantDownTime2*100,2) FROM OEE_DB.dbo.OEEMonthlyReport WHERE Monthly = 'December """ +addYear+"""'""" +addPlant +""" ) as December

                    """)
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        oee = cnxn.cursor()
        oee.execute("""
                    SELECT ROUND(AVG(OEE2FinalCalculation)*100,0) FROM OEE_DB.dbo.OEEMonthlyReport WHERE DATENAME(YEAR , DateTime) = DATENAME(YEAR , '""" +addYear+"""')""" +addPlant +"""
                    """)
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        oee_a = cnxn.cursor()
        oee_a.execute("""
                    SELECT ROUND(AVG(OEE_A2)*100,0) FROM OEE_DB.dbo.OEEMonthlyReport WHERE DATENAME(YEAR , DateTime) = DATENAME(YEAR , '""" +addYear+"""')""" +addPlant +"""
                    """)
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        oee_p = cnxn.cursor()
        oee_p.execute("""
                    SELECT ROUND(AVG(OEE_P2)*100,0) FROM OEE_DB.dbo.OEEMonthlyReport WHERE DATENAME(YEAR , DateTime) = DATENAME(YEAR , '""" +addYear+"""')""" +addPlant +"""
                    """)
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        oee_q = cnxn.cursor()
        oee_q.execute("""
                    SELECT ROUND(AVG(OEE_Q_Final)*100,0) FROM OEE_DB.dbo.OEEMonthlyReport WHERE DATENAME(YEAR , DateTime) = DATENAME(YEAR , '""" +addYear+"""')""" +addPlant +"""
                    """)
    oeebarChart = [] 
    DownTimebarChart = [] 

    for i in data:
        oeebarChart.append(i)
    for i in data1:
        DownTimebarChart.append(i)    
        
    for i in oee:
        showoee = i[0]
        print( i[0])
    for i in oee_a:
        showoee_a = i[0]
    for i in oee_p:
        showoee_p = i[0] 
    for i in oee_q:
        showoee_q = i[0]
   
    try:
        return render_template('oee_Total.html',data=oeebarChart,data1 = DownTimebarChart,
                            showoee = showoee , showoee_a = showoee_a , showoee_p =showoee_p ,
                            showoee_q = showoee_q,oeemenu=oeemenu)
    except:
        return render_template('oee_Total.html',data=0,data1 = 0,
                           showoee = 0 , showoee_a = 0 , showoee_p =0 ,
                           showoee_q = 0,oeemenu=0)

@app.route('/oee_MachineV2')
@flask_login.login_required
def oee_MachineV2():
    return render_template('oee_MachineV2.html')

@app.route('/oee_miru')
@flask_login.login_required
def oee_miru():
    return render_template('oee_miru.html')

@app.route('/yield_Machine')
@flask_login.login_required
def yield_Machine():
    return render_template('yield_Machine.html')

@app.route('/yield_total') 
@flask_login.login_required
def yield_total():
    addPlant = ''
    addYear = '2022'
    
    if request.method == 'POST':
        selectPlant = request.form['selectPlant']
        
        addYear= str(request.form['SelectYear'])
        
        if selectPlant == 'ALL':
            addPlant = ''
        elif selectPlant == 'TLT':
            addPlant = "AND PlantName ='TLT' " 
        elif selectPlant == 'HHD':
            addPlant = "AND PlantName ='HHD' " 
            
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    yield_total = cnxn.cursor()
    yield_total.execute("""
                SELECT ROUND(AVG(FinalYield)*100,0) , ROUND(AVG(Yield)*100,0)  FROM OEE_DB.dbo.YieldMonthlyReport WHERE DATENAME(YEAR , DateTime) = DATENAME(YEAR , '""" +addYear+"""')""" +addPlant +"""
                """)
    
    
    for i in yield_total:
        FinalYield = int(i[0])
        Yield_D1 = int(i[1]//10)
        Yield_D2 = int(i[1]%10)
        
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    data1 = cnxn.cursor()
    data1.execute("""
            SELECT 
                (SELECT ROUND(Yield*100,2) FROM OEE_DB.dbo.YieldMonthlyReport WHERE Monthly = 'January """ +addYear+"""'""" +""" AND PlantName ='TLT') as January,
                (SELECT ROUND(Yield*100,2) FROM OEE_DB.dbo.YieldMonthlyReport WHERE Monthly = 'February """ +addYear+"""'""" +""" AND PlantName ='TLT') as February,
                (SELECT ROUND(Yield*100,2) FROM OEE_DB.dbo.YieldMonthlyReport WHERE Monthly = 'March """ +addYear+"""'""" +""" AND PlantName ='TLT') as March,
                (SELECT ROUND(Yield*100,2) FROM OEE_DB.dbo.YieldMonthlyReport WHERE Monthly = 'April """ +addYear+"""'"""  +"""AND PlantName ='TLT' ) as April,
                (SELECT ROUND(Yield*100,2) FROM OEE_DB.dbo.YieldMonthlyReport WHERE Monthly = 'May """ +addYear+"""'""" +""" AND PlantName ='TLT') as May,
                (SELECT ROUND(Yield*100,2) FROM OEE_DB.dbo.YieldMonthlyReport WHERE Monthly = 'June """ +addYear+"""'""" +""" AND PlantName ='TLT') as June,
                (SELECT ROUND(Yield*100,2) FROM OEE_DB.dbo.YieldMonthlyReport WHERE Monthly = 'July """ +addYear+"""'""" +""" AND PlantName ='TLT') as July,
                (SELECT ROUND(Yield*100,2) FROM OEE_DB.dbo.YieldMonthlyReport WHERE Monthly = 'August """ +addYear+"""'""" +""" AND PlantName ='TLT') as August,
                (SELECT ROUND(Yield*100,2) FROM OEE_DB.dbo.YieldMonthlyReport WHERE Monthly = 'September """ +addYear+"""'"""  +""" AND PlantName ='TLT') as September,
                (SELECT ROUND(Yield*100,2) FROM OEE_DB.dbo.YieldMonthlyReport WHERE Monthly = 'October """ +addYear+"""'""" +""" AND PlantName ='TLT') as October,
                (SELECT ROUND(Yield*100,2) FROM OEE_DB.dbo.YieldMonthlyReport WHERE Monthly = 'November """ +addYear+"""'""" +""" AND PlantName ='TLT') as November,
                (SELECT ROUND(Yield*100,2) FROM OEE_DB.dbo.YieldMonthlyReport WHERE Monthly = 'December """ +addYear+"""'"""  +""" AND PlantName ='TLT') as December

                """)
    TLTYield = [] 

    for i in data1:
        TLTYield.append(i)
   
    
    return render_template('yield_total.html',FinalYield=FinalYield,Yield_D1=Yield_D1,Yield_D2=Yield_D2,data1=TLTYield)

@app.route('/Edit_StorageTanks/<string:mode>/<string:id>/<string:Level>/<string:Fname_Lname>',methods=['GET', 'POST'])
@flask_login.login_required
def Edit_StorageTanks(mode,id,Level,Fname_Lname):
    global User,UserLevel

    if request.method == 'POST':
        if mode == 'update':
            StorageTanksID = request.form['StorageTanksID']
            StorageTanksName = request.form['StorageTanksName']
            WorkCenter = request.form['WorkCenter']
            PlantName = request.form['PlantName']
            Material = request.form['Material']
            MainProduct = request.form['MainProduct']
            SubProduct = "-"
            SetTime = request.form['SetTime']
            ValidatedSpeed = request.form['ValidatedSpeed']
            MaxSpeed = request.form['MaxSpeed'] 
             
            cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
            StorageTanks = cnxn.cursor()
            StorageTanks.execute(' UPDATE OEE_DB.dbo.StorageTanks  SET MachineID = ? , MachineName = ?,WorkCenter = ?,PlantName = ?,Material = ?,MainProduct = ?,SubProduct = ?,ValidatedSpeed = ?,SetTime = ?,MaxSpeed = ?,DeleteFlag = ? , DateTime = GETDATE() WHERE RecordID = ? ', ( StorageTanksID  , StorageTanksName , WorkCenter , PlantName ,Material ,MainProduct ,SubProduct,ValidatedSpeed,SetTime,MaxSpeed ,'1',id ))
            cnxn.commit()
        
       

        elif mode == "add":
            StorageTanksID = request.form['StorageTanksID']
            StorageTanksName = request.form['StorageTanksName']
            WorkCenter = request.form['WorkCenter']
            PlantName = request.form['PlantName']
            Material = request.form['Material']
            MainProduct = request.form['MainProduct']
            SubProduct = "-"
            SetTime = request.form['SetTime']
            ValidatedSpeed = request.form['ValidatedSpeed']
            MaxSpeed = request.form['MaxSpeed']
            
            cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
            StorageTanks = cnxn.cursor()
            StorageTanks.execute(' INSERT INTO OEE_DB.dbo.StorageTanks  (MachineID,MachineName,WorkCenter,PlantName ,Material, MainProduct,SubProduct,ValidatedSpeed,SetTime,MaxSpeed,DeleteFlag) VALUES(?,?,?,?,?,?,?,?,?,?,?)' , ( StorageTanksID  , StorageTanksName , WorkCenter , PlantName ,Material, MainProduct ,SubProduct,ValidatedSpeed,SetTime,MaxSpeed ,'1' ))
            cnxn.commit()

        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        update = cnxn.cursor()
        update.execute('INSERT INTO OEE_DB.dbo.EditRecord (EditID,ChangeTopic,NameValue,[User],UserLevel) VALUES(?,?,?,?,?)' ,(2,mode,StorageTanksName,Fname_Lname,Level))
        cnxn.commit()  
            
    if mode == "del":
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        Machines = cnxn.cursor()
        Machines.execute('UPDATE OEE_DB.dbo.StorageTanks  SET DeleteFlag = -1 , DateTime = GETDATE() WHERE RecordID = ? ',id )
        cnxn.commit()   

        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        update = cnxn.cursor()
        update.execute('INSERT INTO OEE_DB.dbo.EditRecord (EditID,ChangeTopic,NameValue,[User],UserLevel) VALUES(?,?,?,?,?)' ,(2,mode,id,Fname_Lname,Level))
        cnxn.commit() 
    
    
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    StorageTanks = cnxn.cursor()
    StorageTanks.execute('SELECT * FROM OEE_DB.dbo.StorageTanks  WHERE DeleteFlag = 1 ORDER BY DateTime DESC')
    
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    Plant = cnxn.cursor()
    Plant.execute('SELECT PlantName FROM OEE_DB.dbo.Plant WHERE DeleteFlag = 1 ')
    lenPlant = 0
    Plant_s = []
    for i in Plant:
        lenPlant+=1
        Plant_s.append(i)
        
    print(Plant_s)
        
    return render_template('Edit_StorageTanks.html',StorageTanks = StorageTanks,Plant=Plant_s,len=lenPlant,Level=Level,Fname_Lname=Fname_Lname)

@app.route('/Edit_Machines/<string:mode>/<string:id>/<string:Level>/<string:Fname_Lname>',methods=['GET', 'POST'])
@flask_login.login_required
def Edit_Machines(mode,id,Level,Fname_Lname):
    if request.method == 'POST':
        if mode == 'update':
            MachineID = request.form['MachineID']
            MachineName = request.form['MachineName']
            WorkCenter = request.form['WorkCenter']
            PlantName = request.form['PlantName']
            Material = request.form['Material']
            MainProduct = request.form['MainProduct']
            SubProduct = "-"
            SetTime = request.form['SetTime']
            ValidatedSpeed = request.form['ValidatedSpeed']
            MaxSpeed = request.form['MaxSpeed'] 
             
            cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
            StorageTanks = cnxn.cursor()
            StorageTanks.execute(' UPDATE OEE_DB.dbo.Machines SET MachineID = ? , MachineName = ?,WorkCenter = ?,PlantName = ?,Material = ?,MainProduct = ?,SubProduct = ?,ValidatedSpeed = ?,SetTime = ?,MaxSpeed = ?,DeleteFlag = ? , DateTime = GETDATE() WHERE RecordID = ? ', ( MachineID  , MachineName , WorkCenter , PlantName ,Material ,MainProduct ,SubProduct,ValidatedSpeed,SetTime,MaxSpeed ,'1',id ))
            cnxn.commit()
        
       

        elif mode == "add":
            MachineID = request.form['MachineID']
            MachineName = request.form['MachineName']
            WorkCenter = request.form['WorkCenter']
            PlantName = request.form['PlantName']
            Material = request.form['Material']
            MainProduct = request.form['MainProduct']
            SubProduct = "-"
            SetTime = request.form['SetTime']
            ValidatedSpeed = request.form['ValidatedSpeed']
            MaxSpeed = request.form['MaxSpeed']
            
            cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
            StorageTanks = cnxn.cursor()
            StorageTanks.execute(' INSERT INTO OEE_DB.dbo.Machines (MachineID,MachineName,WorkCenter,PlantName ,Material, MainProduct,SubProduct,ValidatedSpeed,SetTime,MaxSpeed,DeleteFlag) VALUES(?,?,?,?,?,?,?,?,?,?,?)' , ( MachineID  , MachineName , WorkCenter , PlantName ,Material, MainProduct ,SubProduct,ValidatedSpeed,SetTime,MaxSpeed ,'1' ))
            cnxn.commit()

        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        update = cnxn.cursor()
        update.execute('INSERT INTO OEE_DB.dbo.EditRecord (EditID,ChangeTopic,NameValue,[User],UserLevel) VALUES(?,?,?,?,?)' ,(2,mode,MachineName,Fname_Lname,Level))
        cnxn.commit()  
            
    if mode == "del":
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        Machines = cnxn.cursor()
        Machines.execute('UPDATE OEE_DB.dbo.Machines SET DeleteFlag = -1 , DateTime = GETDATE() WHERE RecordID = ? ',id )
        cnxn.commit()   

        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        update = cnxn.cursor()
        update.execute('INSERT INTO OEE_DB.dbo.EditRecord (EditID,ChangeTopic,NameValue,[User],UserLevel) VALUES(?,?,?,?,?)' ,(2,mode,id,Fname_Lname,Level))
        cnxn.commit() 
    
    
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    Machines = cnxn.cursor()
    Machines.execute('SELECT * FROM OEE_DB.dbo.Machines WHERE DeleteFlag = 1 ORDER BY DateTime DESC')
    
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    Plant = cnxn.cursor()
    Plant.execute('SELECT PlantName FROM OEE_DB.dbo.Plant WHERE DeleteFlag = 1 ')
    lenPlant = 0
    Plant_s = []
    for i in Plant:
        lenPlant+=1
        Plant_s.append(i)
        
    print(Plant_s)
        
    return render_template('Edit_Machines.html',Machines = Machines,Plant=Plant_s,len = lenPlant,Level=Level,Fname_Lname=Fname_Lname)

@app.route('/Edit_Plant/<string:mode>/<string:id>/<string:Level>/<string:Fname_Lname>',methods=['GET', 'POST'])
@flask_login.login_required
def Edit_Plant(mode,id,Level,Fname_Lname):
    if request.method == 'POST':
        if mode == 'update':
            PlantID = request.form['PlantID']
            PlantName = request.form['PlantName']
            
            cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
            Plant = cnxn.cursor()
            Plant.execute(' UPDATE OEE_DB.dbo.Plant SET PlantID = ? , PlantName = ?,DeleteFlag = ? , DateTime = GETDATE() WHERE RecordID = ?', (  PlantID  , PlantName , '1',id ))
            cnxn.commit()
            
        elif mode == "add":
            PlantID = request.form['PlantID']
            PlantName = request.form['PlantName']
            
            cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
            Plant = cnxn.cursor()
            Plant.execute(' INSERT INTO OEE_DB.dbo.Plant (PlantID,PlantName,DeleteFlag) VALUES(?,?,?)' ,( PlantID  , PlantName , '1' ))
            cnxn.commit()

        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        update = cnxn.cursor()
        update.execute('INSERT INTO OEE_DB.dbo.EditRecord (EditID,ChangeTopic,NameValue,[User],UserLevel) VALUES(?,?,?,?,?)' ,(3,mode,PlantName,Fname_Lname,Level))
        cnxn.commit() 
            
    if mode == "del":
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        Plant = cnxn.cursor()
        Plant.execute('UPDATE OEE_DB.dbo.Plant SET DeleteFlag = -1 , DateTime = GETDATE() WHERE RecordID =? ',id )
        cnxn.commit()
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        update = cnxn.cursor()
        update.execute('INSERT INTO OEE_DB.dbo.EditRecord (EditID,ChangeTopic,NameValue,[User],UserLevel) VALUES(?,?,?,?,?)' ,(3,mode,id,Fname_Lname,Level))
        cnxn.commit() 
    
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    Plant = cnxn.cursor()
    Plant.execute('SELECT * FROM OEE_DB.dbo.Plant WHERE DeleteFlag = 1 ORDER BY DateTime DESC')
    
    return render_template('Edit_Plant.html',Plant = Plant,Level=Level,Fname_Lname=Fname_Lname)

@app.route('/Edit_DownTimeCode/<string:mode>/<string:id>/<string:Level>/<string:Fname_Lname>',methods=['GET', 'POST'])
@flask_login.login_required
def Edit_DownTimeCode(mode,id,Level,Fname_Lname):
    if request.method == 'POST':
        if mode == 'update':
            Code = request.form['Code']
            Description = request.form['Description']
            Type = request.form['Type']
            Response = request.form['Response']
            
            cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
            DownTimeCode = cnxn.cursor()
            DownTimeCode.execute('UPDATE OEE_DB.dbo.DownTimeCode SET Code = ?,Description = ?,Type = ?,Response = ?,DeleteFlag = ? , DateTime = GETDATE() WHERE RecordID =? ', ( Code,Description ,Type,Response, '1',id ))
            cnxn.commit()
            
        elif mode == "add":
            
            Code = request.form['Code']
            Description = request.form['Description']
            Type = request.form['Type']
            Response = request.form['Response']
            
            cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
            DownTimeCode = cnxn.cursor()
            DownTimeCode.execute(' INSERT INTO OEE_DB.dbo.DownTimeCode (Code,Description ,Type,Response,DeleteFlag) VALUES(?,?,?,?,?)' , ( Code,Description ,Type,Response, '1' ))
            cnxn.commit()

        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        update = cnxn.cursor()
        update.execute('INSERT INTO OEE_DB.dbo.EditRecord (EditID,ChangeTopic,NameValue,[User],UserLevel) VALUES(?,?,?,?,?)' ,(4,mode,Description,Fname_Lname,Level))
        cnxn.commit()      
    if mode == "del":
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        DownTimeCode = cnxn.cursor()
        DownTimeCode.execute(' UPDATE OEE_DB.dbo.DownTimeCode SET DeleteFlag = -1 , DateTime = GETDATE() WHERE  RecordID = ? ',id )
        cnxn.commit()

        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        update = cnxn.cursor()
        update.execute('INSERT INTO OEE_DB.dbo.EditRecord (EditID,ChangeTopic,NameValue,[User],UserLevel) VALUES(?,?,?,?,?)' ,(4,mode,id,Fname_Lname,Level))
        cnxn.commit() 
    
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    DownTimeCode = cnxn.cursor()
    DownTimeCode.execute('SELECT * FROM OEE_DB.dbo.DownTimeCode WHERE DeleteFlag = 1 ORDER BY DateTime DESC')
    
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    Department = cnxn.cursor()
    Department.execute('SELECT DepartmentName FROM OEE_DB.dbo.Department WHERE DeleteFlag = 1 ')
    lenDepartment = 0
    Department_s = []
    for i in Department:
        lenDepartment+=1
        Department_s.append(i)
        
    #print(Department_s)
        
    return render_template('Edit_DownTimeCode.html',DownTimeCode = DownTimeCode,Department=Department_s,len = lenDepartment,Level=Level,Fname_Lname=Fname_Lname)

@app.route('/Edit_Shift/<string:mode>/<string:id>/<string:Level>/<string:Fname_Lname>',methods=['GET', 'POST'])
@flask_login.login_required
def Edit_Shift(mode,id,Level,Fname_Lname):
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
            
            cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
            Edit_Shift = cnxn.cursor() 
            Edit_Shift.execute('UPDATE OEE_DB.dbo.ShiftCode SET ShiftCodeID = ? , ShiftCodeName = ?,StartTime = ?,EndTime = ?,Break1 = ?,Break2 = ?,Break3 = ?,PlanProductionTime = ?,DeleteFlag = ?  , DateTime = GETDATE() WHERE RecordID = ? ',( ShiftCodeID  , ShiftCodeName,StartTime ,EndTime,Break1,Break2,Break3,PlanProductionTime ,'1',id ))
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
            
            
            cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
            Edit_Shift = cnxn.cursor()
            Edit_Shift.execute('INSERT INTO OEE_DB.dbo.ShiftCode (ShiftCodeID , ShiftCodeName,StartTime,EndTime,Break1,Break2,Break3,PlanProductionTime,DeleteFlag) VALUES(?,?,?,?,?,?,?,?,?)' ,(  ShiftCodeID  , ShiftCodeName,StartTime ,EndTime,Break1,Break2,Break3,PlanProductionTime, '1') )
            cnxn.commit()
        
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        update = cnxn.cursor()
        update.execute('INSERT INTO OEE_DB.dbo.EditRecord (EditID,ChangeTopic,NameValue,[User],UserLevel) VALUES(?,?,?,?,?)' ,(5,mode,ShiftCodeName,Fname_Lname,Level))
        cnxn.commit() 
            
    if mode == "del":
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        Edit_Shift = cnxn.cursor()
        Edit_Shift.execute('UPDATE OEE_DB.dbo.ShiftCode SET DeleteFlag = ? , DateTime = GETDATE() WHERE RecordID = ? ',(-1,id) )
        cnxn.commit()

        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        update = cnxn.cursor()
        update.execute('INSERT INTO OEE_DB.dbo.EditRecord (EditID,ChangeTopic,NameValue,[User],UserLevel) VALUES(?,?,?,?,?)' ,(5,mode,id,Fname_Lname,Level))
        cnxn.commit() 
        
    
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    Edit_Shift = cnxn.cursor()
    Edit_Shift.execute('SELECT * FROM OEE_DB.dbo.ShiftCode WHERE DeleteFlag = 1 ORDER BY DateTime DESC')
    
    
        
    return render_template('Edit_Shift.html',Edit_Shift = Edit_Shift,Level=Level,Fname_Lname=Fname_Lname)

@app.route('/Edit_Standardcolor/<string:mode>/<string:id>/<string:Level>/<string:Fname_Lname>',methods=['GET', 'POST'])
@flask_login.login_required
def Edit_Standardcolor(mode,id,Level,Fname_Lname):
    if request.method == 'POST':
        if mode == 'update':
            Red = request.form['Red']
            Yellow = request.form['Yellow']
            Green = request.form['Green']
            Revision = request.form['Revision']
            
            cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
            DownTimeCode = cnxn.cursor()
            DownTimeCode.execute('UPDATE OEE_DB.dbo.StandardColor SET Red = ? , Yellow = ?,Green = ?,Revision = ?,DeleteFlag = ? , DateTime = GETDATE() WHERE RecordID = ? ', (Red  , Yellow ,Green ,Revision, '1',id ))
            cnxn.commit()
            
        elif mode == "add":
            Red = request.form['Red']
            Yellow = request.form['Yellow']
            Green = request.form['Green']
            Revision = request.form['Revision']
            
            cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
            DownTimeCode = cnxn.cursor()
            DownTimeCode.execute('INSERT INTO StandardColor (Red ,Yellow ,Green ,Revision,DeleteFlag) VALUES(?,?,?,?,?)',( Red  , Yellow ,Green ,Revision, '1' ))
            cnxn.commit()

        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        update = cnxn.cursor()
        update.execute('INSERT INTO OEE_DB.dbo.EditRecord (EditID,ChangeTopic,NameValue,[User],UserLevel) VALUES(?,?,?,?,?)' ,(6,mode,Revision,Fname_Lname,Level))
        cnxn.commit()     
            
   
    
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    Edit_Standardcolor = cnxn.cursor()
    Edit_Standardcolor.execute('SELECT * FROM OEE_DB.dbo.StandardColor WHERE DeleteFlag = 1 ORDER BY DateTime DESC')
    Standardcolor = []
    
    for i in Edit_Standardcolor:
    
        #len_color+=1
        Standardcolor.append(i)
    
        
    return render_template('Edit_Standardcolor.html',Edit_Standardcolor = Standardcolor,Level=Level,Fname_Lname=Fname_Lname)

@app.route('/Edit_UserGroup/<string:mode>/<string:id>/<string:Level>/<string:Fname_Lname>',methods=['GET', 'POST'])
@flask_login.login_required
def Edit_UserGroup(mode,id,Level,Fname_Lname):
    if request.method == 'POST':
        if mode == 'update':
            UserGroupID = request.form['UserGroupID']
            UserGroupName = request.form['UserGroupName']
            
            cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
            Edit_UserGroup = cnxn.cursor()
            Edit_UserGroup.execute('UPDATE OEE_DB.dbo.UserGroup SET UserGroupID = ? , UserGroupName = ? ,DeleteFlag = ? , DateTime = GETDATE() WHERE RecordID = ? ',(UserGroupID,UserGroupName  ,'1',id ))
            cnxn.commit()
            
        elif mode == "add":
            UserGroupID = request.form['UserGroupID']
            UserGroupName = request.form['UserGroupName']
            
            cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
            Edit_UserGroup = cnxn.cursor()
            Edit_UserGroup.execute('INSERT INTO OEE_DB.dbo.UserGroup (UserGroupID , UserGroupName,DeleteFlag) VALUES(?,?,?)' ,( UserGroupID,UserGroupName  ,'1') )
            cnxn.commit()

        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        update = cnxn.cursor()
        update.execute('INSERT INTO OEE_DB.dbo.EditRecord (EditID,ChangeTopic,NameValue,[User],UserLevel) VALUES(?,?,?,?,?)' ,(7,mode,UserGroupName,Fname_Lname,Level))
        cnxn.commit()
            
    if mode == "del":
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        Edit_UserGroup = cnxn.cursor()
        Edit_UserGroup.execute('UPDATE OEE_DB.dbo.UserGroup SET DeleteFlag = ?  , DateTime = GETDATE() WHERE RecordID = ? ',(-1,id) )
        cnxn.commit()

        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        update = cnxn.cursor()
        update.execute('INSERT INTO OEE_DB.dbo.EditRecord (EditID,ChangeTopic,NameValue,[User],UserLevel) VALUES(?,?,?,?,?)' ,(7,mode,id,Fname_Lname,Level))
        cnxn.commit()
    
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    Edit_UserGroup = cnxn.cursor()
    Edit_UserGroup.execute('SELECT * FROM OEE_DB.dbo.UserGroup WHERE DeleteFlag = 1 ORDER BY DateTime DESC')
    
    
        
    return render_template('Edit_UserGroup.html',Edit_UserGroup = Edit_UserGroup,Level=Level,Fname_Lname=Fname_Lname)

@app.route('/Edit_Department/<string:mode>/<string:id>/<string:Level>/<string:Fname_Lname>',methods=['GET', 'POST'])
@flask_login.login_required
def Edit_Department(mode,id,Level,Fname_Lname):
    if request.method == 'POST':
        if mode == 'update':
            Department_ID = request.form['Department_ID']
            Department_Name = request.form['Department_Name']
           
            
            cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
            Department = cnxn.cursor()
            Department.execute('UPDATE OEE_DB.dbo.Department SET DepartmentID = ?,DepartmentName = ?,DeleteFlag = ? , DateTime = GETDATE() WHERE RecordID =? ', ( Department_ID,Department_Name ,'1',id ))
            cnxn.commit()
            
        elif mode == "add":
            
            Department_ID = request.form['Department_ID']
            Department_Name = request.form['Department_Name']
           
            
            cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
            Department = cnxn.cursor()
            Department.execute(' INSERT INTO OEE_DB.dbo.Department (DepartmentID,DepartmentName ,DeleteFlag) VALUES(?,?,?)' , (Department_ID,Department_Name , '1' ))
            cnxn.commit()

        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        update = cnxn.cursor()
        update.execute('INSERT INTO OEE_DB.dbo.EditRecord (EditID,ChangeTopic,NameValue,[User],UserLevel) VALUES(?,?,?,?,?)' ,(9,mode,Department_Name,Fname_Lname,Level))
        cnxn.commit()      
    if mode == "del":
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        Department = cnxn.cursor()
        Department.execute(' UPDATE OEE_DB.dbo.Department SET DeleteFlag = -1 , DateTime = GETDATE() WHERE  RecordID = ? ',id )
        cnxn.commit()

        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        update = cnxn.cursor()
        update.execute('INSERT INTO OEE_DB.dbo.EditRecord (EditID,ChangeTopic,NameValue,[User],UserLevel) VALUES(?,?,?,?,?)' ,(9,mode,id,Fname_Lname,Level))
        cnxn.commit() 
    
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    Department = cnxn.cursor()
    Department.execute('SELECT * FROM OEE_DB.dbo.Department WHERE DeleteFlag = 1 ORDER BY DateTime DESC')
    
    
        
    return render_template('Edit_Department.html',Department = Department,Level=Level,Fname_Lname=Fname_Lname)


@app.route('/hello')
@flask_login.login_required
def hello():
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    workMachine = cnxn.cursor()
    workMachine.execute('SELECT RecordID, PlantID , PlantName,MachineID,MachineName,Date,PlannedCode,StartTime,EndTime FROM OEE_DB.dbo.PlannedProductionTime  ORDER BY DateTime DESC ')

    record = workMachine.fetchone()
    
    return record

@app.route('/Record/<string:Level>/<string:Fname_Lname>')
@flask_login.login_required
def Record(Level,Fname_Lname):
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    Record = cnxn.cursor()
    Record.execute('SELECT * FROM OEE_DB.dbo.EditRecord INNER JOIN OEE_DB.dbo.EditCode ON EditRecord.EditID=EditCode.ID ORDER BY DateTime DESC')

    
    
    return render_template('Record.html',Record = Record,Level=Level,Fname_Lname=Fname_Lname)

@app.route('/ReportOEE/<string:Level>/<string:Fname_Lname>',methods=['GET', 'POST'])
@flask_login.login_required
def ReportOEE(Level,Fname_Lname):
    global ansOEE_Plant
    global ansOEE_Machines
    global ansOEE_Shifts
    global ansOEE_StartDate
    global ansOEE_StopDate
    global where
    global ansOEE_UserGroup
    
    global excelOEE_Plant
    global excelOEE_Machines 
    global excelOEE_Shifts   
    global excelOEE_StartDate 
    global excelOEE_StopDate 
    global excelOEE_UserGroup 
    
    ansOEE_Plant = 'ALL'
    ansOEE_Machines = 'ALL'
    ansOEE_Shifts   = 'ALL'
    ansOEE_UserGroup = 'ALL'
    ansOEE_StartDate = ''
    ansOEE_StopDate = ''
    
    
    if request.method == 'POST':
        ansOEE_Plant = request.form['Plant']
        ansOEE_Machines = request.form['Machines']
        ansOEE_Shifts = request.form['Shifts']
        ansOEE_StartDate = request.form['StartDate']
        ansOEE_StopDate = request.form['StopDate']
        ansOEE_UserGroup = request.form['UserGroup']
        print("---------------")
        print(ansOEE_Plant)
        print(ansOEE_Machines)
        print(ansOEE_Shifts)
        print(ansOEE_StartDate)
        print(ansOEE_StopDate)
        print(ansOEE_UserGroup)
        
        
        excelOEE_Plant = ansOEE_Plant
        excelOEE_Machines = ansOEE_Machines
        excelOEE_Shifts   = ansOEE_Shifts
        excelOEE_StartDate = ansOEE_StartDate
        excelOEE_StopDate = ansOEE_StopDate
        excelOEE_UserGroup = ansOEE_UserGroup
    
   
    if ansOEE_Plant == 'ALL':
        ansOEE_Plant = ''
    else : 
        ansOEE_Plant = " AND PlantName = '"+ ansOEE_Plant +"'"
        
    if ansOEE_Machines == 'ALL':
        ansOEE_Machines = ''
    else :  
        ansOEE_Machines = " AND MachineID = '"+ ansOEE_Machines +"'"
       
    if ansOEE_Shifts == 'ALL':
        ansOEE_Shifts = ''
    else : 
        ansOEE_Shifts = " AND ShiftCode = '"+ ansOEE_Shifts +"'"
        
    if ansOEE_UserGroup == 'ALL':
        ansOEE_UserGroup = ''
    else : 
        ansOEE_UserGroup = " AND UserGroupID = '"+ ansOEE_UserGroup +"'"
        
    if ansOEE_StartDate == '':
        ansOEE_StartDate = ''
    else : 
        ansOEE_StartDate = " AND CONVERT(DATE, DateTime) >= '"+ ansOEE_StartDate +"'"
         
    if ansOEE_StopDate == '':
        ansOEE_StopDate = ''
    else : 
        ansOEE_StopDate = " AND CONVERT(DATE, DateTime)  <= '"+ ansOEE_StopDate +"'"
      
  
        
    print("---------------")
    print(ansOEE_Plant)
    print(ansOEE_Machines)
    print(ansOEE_Shifts)
    print(ansOEE_StartDate)
    print(ansOEE_StopDate)
     
    
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    Plant = cnxn.cursor()
    Plant.execute('SELECT PlantName FROM OEE_DB.dbo.Plant  WHERE DeleteFlag = 1')
    
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    Machines = cnxn.cursor()
    Machines.execute('SELECT MachineName ,MachineID FROM OEE_DB.dbo.Machines  WHERE DeleteFlag = 1')

    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    Shifts = cnxn.cursor()
    Shifts.execute('SELECT ShiftCodeName , ShiftCodeID FROM OEE_DB.dbo.ShiftCode  WHERE DeleteFlag = 1')
    
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    UserGroup = cnxn.cursor()
    UserGroup.execute('SELECT UserGroupName , UserGroupID FROM OEE_DB.dbo.UserGroup  WHERE DeleteFlag = 1')

    return render_template('Report_OEE.html',Plant = Plant , Machines = Machines , Shifts = Shifts,UserGroup=UserGroup,Level=Level,Fname_Lname=Fname_Lname)

@app.route('/ReportOEE_Total/<string:Level>/<string:Fname_Lname>',methods=['GET', 'POST'])
@flask_login.login_required
def ReportOEE_Total(Level,Fname_Lname):
    global ansOEE_Total_Plant
    global ansOEE_Total_Machines
    global ansOEE_Total_Shifts
    global ansOEE_Total_StartDate
    global ansOEE_Total_StopDate
    global where
    global ansOEE_Total_UserGroup
    
    global excelOEE_Total_Plant
    global excelOEE_Total_Machines 
    global excelOEE_Total_Shifts   
    global excelOEE_Total_StartDate 
    global excelOEE_Total_StopDate 
    global excelOEE_Total_UserGroup 
    
    ansOEE_Total_Plant = 'ALL'
    ansOEE_Total_Machines = 'ALL'
    ansOEE_Total_Shifts   = 'ALL'
    ansOEE_Total_UserGroup = 'ALL'
    ansOEE_Total_StartDate = ''
    ansOEE_Total_StopDate = ''
    
    
    if request.method == 'POST':
        ansOEE_Total_Plant = request.form['Plant']
        ansOEE_Total_Machines = request.form['Machines']
        ansOEE_Total_Shifts = request.form['Shifts']
        ansOEE_Total_StartDate = request.form['StartDate']
        ansOEE_Total_StopDate = request.form['StopDate']
        ansOEE_Total_UserGroup = request.form['UserGroup']
        print("---------------")
        print(ansOEE_Total_Plant)
        print(ansOEE_Total_Machines)
        print(ansOEE_Total_Shifts)
        print(ansOEE_Total_StartDate)
        print(ansOEE_Total_StopDate)
        print(ansOEE_Total_UserGroup)
        
        
        excelOEE_Total_Plant = ansOEE_Total_Plant
        excelOEE_Total_Machines = ansOEE_Total_Machines
        excelOEE_Total_Shifts   = ansOEE_Total_Shifts
        excelOEE_Total_StartDate = ansOEE_Total_StartDate
        excelOEE_Total_StopDate = ansOEE_Total_StopDate
        excelOEE_Total_UserGroup = ansOEE_Total_UserGroup
    
   
    if ansOEE_Total_Plant == 'ALL':
        ansOEE_Total_Plant = ''
    else : 
        ansOEE_Total_Plant = " AND PlantName = '"+ ansOEE_Total_Plant +"'"
        
    if ansOEE_Total_Machines == 'ALL':
        ansOEE_Total_Machines = ''
    else :  
        ansOEE_Total_Machines = " AND MachineID = '"+ ansOEE_Total_Machines +"'"
       
    if ansOEE_Total_Shifts == 'ALL':
        ansOEE_Total_Shifts = ''
    else : 
        ansOEE_Total_Shifts = " AND ShiftCode = '"+ ansOEE_Total_Shifts +"'"
        
    if ansOEE_Total_UserGroup == 'ALL':
        ansOEE_Total_UserGroup = ''
    else : 
        ansOEE_Total_UserGroup = " AND UserGroupID = '"+ ansOEE_Total_UserGroup +"'"
        
    if ansOEE_Total_StartDate == '':
        ansOEE_Total_StartDate = ''
    else : 
        ansOEE_Total_StartDate = " AND CONVERT(DATE, DateTime) >= '"+ ansOEE_Total_StartDate +"'"
         
    if ansOEE_Total_StopDate == '':
        ansOEE_Total_StopDate = ''
    else : 
        ansOEE_Total_StopDate = " AND CONVERT(DATE, DateTime)  <= '"+ ansOEE_Total_StopDate +"'"
      
  
        
    print("---------------")
    print(ansOEE_Total_Plant)
    print(ansOEE_Total_Machines)
    print(ansOEE_Total_Shifts)
    print(ansOEE_Total_StartDate)
    print(ansOEE_Total_StopDate)
     
    
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    Plant = cnxn.cursor()
    Plant.execute('SELECT PlantName FROM OEE_DB.dbo.Plant  WHERE DeleteFlag = 1')
    
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    Machines = cnxn.cursor()
    Machines.execute('SELECT MachineName ,MachineID FROM OEE_DB.dbo.Machines  WHERE DeleteFlag = 1')

    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    Shifts = cnxn.cursor()
    Shifts.execute('SELECT ShiftCodeName , ShiftCodeID FROM OEE_DB.dbo.ShiftCode  WHERE DeleteFlag = 1')
    
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    UserGroup = cnxn.cursor()
    UserGroup.execute('SELECT UserGroupName , UserGroupID FROM OEE_DB.dbo.UserGroup  WHERE DeleteFlag = 1')

    return render_template('Report_OEE_Total.html',Plant = Plant , Machines = Machines , Shifts = Shifts,UserGroup=UserGroup,Level=Level,Fname_Lname=Fname_Lname)



@app.route('/ReportYield/<string:Level>/<string:Fname_Lname>',methods=['GET', 'POST'])
@flask_login.login_required
def ReportYield(Level,Fname_Lname):
    global ansYield_Plant
    global ansYield_Machines
    global ansYield_Shifts
    global ansYield_StartDate
    global ansYield_StopDate
    global where
    global ansYield_UserGroup
    
    global excelYield_Plant
    global excelYield_Machines 
    global excelYield_Shifts   
    global excelYield_StartDate 
    global excelYield_StopDate 
    global excelYield_UserGroup 
    
    ansYield_Plant = 'ALL'
    ansYield_Machines = 'ALL'
    ansYield_Shifts   = 'ALL'
    ansYield_UserGroup = 'ALL'
    ansYield_StartDate = ''
    ansYield_StopDate = ''
    
    
    if request.method == 'POST':
        ansYield_Plant = request.form['Plant']
        ansYield_Machines = request.form['Machines']
        ansYield_Shifts = 'ALL'
        ansYield_StartDate = request.form['StartDate']
        ansYield_StopDate = request.form['StopDate']
        ansYield_UserGroup = 'ALL'
        print("---------------")
        print(ansYield_Plant)
        print(ansYield_Machines)
        print(ansYield_Shifts)
        print(ansYield_StartDate)
        print(ansYield_StopDate)
        print(ansYield_UserGroup)
        
        
        excelYield_Plant = ansYield_Plant
        excelYield_Machines = ansYield_Machines
        excelYield_Shifts   = ansYield_Shifts
        excelYield_StartDate = ansYield_StartDate
        excelYield_StopDate = ansYield_StopDate
        excelYield_UserGroup = ansYield_UserGroup
    
   
    if ansYield_Plant == 'ALL':
        ansYield_Plant = ''
    else : 
        ansYield_Plant = " AND PlantName = '"+ ansYield_Plant +"'"
        
    if ansYield_Machines == 'ALL':
        ansYield_Machines = ''
    else :  
        ansYield_Machines = " AND MachineID = '"+ ansYield_Machines +"'"
       
    if ansYield_Shifts == 'ALL':
        ansYield_Shifts = ''
    else : 
        ansYield_Shifts = " AND ShiftCode = '"+ ansYield_Shifts +"'"
        
    if ansYield_UserGroup == 'ALL':
        ansYield_UserGroup = ''
    else : 
        ansYield_UserGroup = " AND UserGroupID = '"+ ansYield_UserGroup +"'"
        
    if ansYield_StartDate == '':
        ansYield_StartDate = ''
    else : 
        ansYield_StartDate = " AND CONVERT(DATE, DateTime) >= '"+ ansYield_StartDate +"'"
         
    if ansYield_StopDate == '':
        ansYield_StopDate = ''
    else : 
        ansYield_StopDate = " AND CONVERT(DATE, DateTime)  <= '"+ ansYield_StopDate +"'"
      
  
        
    print("---------------")
    print(ansYield_Plant)
    print(ansYield_Machines)
    print(ansYield_Shifts)
    print(ansYield_StartDate)
    print(ansYield_StopDate)
     
    
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    Plant = cnxn.cursor()
    Plant.execute('SELECT PlantName FROM OEE_DB.dbo.Plant  WHERE DeleteFlag = 1')
    
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    Machines = cnxn.cursor()
    Machines.execute('SELECT MachineName ,MachineID FROM OEE_DB.dbo.Machines  WHERE DeleteFlag = 1')

    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    Shifts = cnxn.cursor()
    Shifts.execute('SELECT ShiftCodeName , ShiftCodeID FROM OEE_DB.dbo.ShiftCode  WHERE DeleteFlag = 1')
    
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    UserGroup = cnxn.cursor()
    UserGroup.execute('SELECT UserGroupName , UserGroupID FROM OEE_DB.dbo.UserGroup  WHERE DeleteFlag = 1')

    return render_template('Report_Yield.html',Plant = Plant , Machines = Machines , Shifts = Shifts,UserGroup=UserGroup,Level=Level,Fname_Lname=Fname_Lname)

    
@app.route('/ReportOverallYield/<string:Level>/<string:Fname_Lname>',methods=['GET', 'POST'])
@flask_login.login_required
def ReportOverallYield(Level,Fname_Lname):
    return render_template('Report_Overall_Yield.html',Level=Level,Fname_Lname=Fname_Lname)

@app.route('/ReportOEEMontly/<string:Level>/<string:Fname_Lname>',methods=['GET', 'POST'])
@flask_login.login_required
def ReportOEEMontly(Level,Fname_Lname):
    global ansOEE_Plant_M
    global ansOEE_Machines_M
    global ansOEE_Shifts_M
    global ansOEE_StartDate_M
    global ansOEE_StopDate_M
    global where
    global ansOEE_UserGroup_M
    global ansOEE_Month_M
    global ansOEE_Month_M_Report
    
    global excelOEE_Plant_M
    global excelOEE_Machines_M 
    global excelOEE_Shifts_M   
    global excelOEE_StartDate_M 
    global excelOEE_StopDate_M 
    global excelOEE_UserGroup_M
    global excelOEE_Month_M
    ansOEE_Plant_M = 'ALL'
    ansOEE_Machines_M = 'ALL'
    ansOEE_Shifts_M   = 'ALL'
    ansOEE_UserGroup_M = 'ALL'
    ansOEE_StartDate_M = ''
    ansOEE_StopDate_M = ''
    ansOEE_Month_M = ''
    
    
    if request.method == 'POST':
        ansOEE_Plant_M = request.form['Plant']
        ansOEE_Machines_M = request.form['Machines']
        ansOEE_Shifts_M = 'ALL'
        ansOEE_Month_M = request.form['Month12']
        ansOEE_UserGroup_M = 'ALL'
        ansOEE_Month_M_Report = ansOEE_Month_M
        ansOEE_Month_M = ansOEE_Month_M.replace("-", "")
     
        print("---------------")
        print(ansOEE_Plant_M)
        print(ansOEE_Machines_M)
        print(ansOEE_Shifts_M)
        print(ansOEE_StartDate_M)
        print(ansOEE_StopDate_M)
        print(ansOEE_UserGroup_M)
        print(ansOEE_Month_M)
        
        
        excelOEE_Plant_M = ansOEE_Plant_M
        excelOEE_Machines_M = ansOEE_Machines_M
        excelOEE_Shifts_M   = ansOEE_Shifts_M
        excelOEE_Month_M = ansOEE_Month_M_Report
       
        excelOEE_UserGroup_M = ansOEE_UserGroup_M
    
   
    if ansOEE_Plant_M == 'ALL':
        ansOEE_Plant_M = ''
    else : 
        ansOEE_Plant_M = " AND PlantName = '"+ ansOEE_Plant_M +"'"
        
    if ansOEE_Machines_M == 'ALL':
        ansOEE_Machines_M = ''
    else :  
        ansOEE_Machines_M = " AND MachineID = '"+ ansOEE_Machines_M +"'"
       
    if ansOEE_Shifts_M == 'ALL':
        ansOEE_Shifts_M = ''
    else : 
        ansOEE_Shifts_M = " AND ShiftCode = '"+ ansOEE_Shifts_M +"'"
        
    if ansOEE_UserGroup_M == 'ALL':
        ansOEE_UserGroup_M = ''
    else : 
        ansOEE_UserGroup_M = " AND UserGroupID = '"+ ansOEE_UserGroup_M +"'"
        
    if ansOEE_Month_M == '':
        ansOEE_Month_M = ''
    else : 
        ansOEE_Month_M = " AND CAST(FORMAT(PostingDate, 'yyyyMM') AS int) = " + ansOEE_Month_M 
         
        
    print("---------------")
    print(ansOEE_Plant_M)
    print(ansOEE_Machines_M)
    print(ansOEE_Shifts_M)
    print(ansOEE_StartDate_M)
    print(ansOEE_StopDate_M)
    print(ansOEE_Month_M)
     
    #--
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    Plant = cnxn.cursor()
    Plant.execute('SELECT PlantName FROM OEE_DB.dbo.Plant  WHERE DeleteFlag = 1')
    
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    Machines = cnxn.cursor()
    Machines.execute('SELECT MachineName ,MachineID FROM OEE_DB.dbo.Machines  WHERE DeleteFlag = 1')

    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    Shifts = cnxn.cursor()
    Shifts.execute('SELECT ShiftCodeName , ShiftCodeID FROM OEE_DB.dbo.ShiftCode  WHERE DeleteFlag = 1')
    
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    UserGroup = cnxn.cursor()
    UserGroup.execute('SELECT UserGroupName , UserGroupID FROM OEE_DB.dbo.UserGroup  WHERE DeleteFlag = 1')

    return render_template('Report_OEE_Montly.html',Plant = Plant , Machines = Machines , Shifts = Shifts,UserGroup=UserGroup,Level=Level,Fname_Lname=Fname_Lname)


@app.route('/ReportYieldMontly/<string:Level>/<string:Fname_Lname>',methods=['GET', 'POST'])
@flask_login.login_required
def ReportYieldMontly(Level,Fname_Lname):
    global ansYield_Plant_M
    global ansYield_Machines_M
    global ansYield_Shifts_M
    global ansYield_StartDate_M
    global ansYield_StopDate_M
    global where
    global ansYield_UserGroup_M
    global ansYield_Month_M
    global ansYield_Month_M_Report
    
    global excelYield_Plant_M
    global excelYield_Machines_M 
    global excelYield_Shifts_M   
    global excelYield_StartDate_M 
    global excelYield_StopDate_M 
    global excelYield_UserGroup_M
    global excelYield_Month_M
    ansYield_Plant_M = 'ALL'
    ansYield_Machines_M = 'ALL'
    ansYield_Shifts_M   = 'ALL'
    ansYield_UserGroup_M = 'ALL'
    ansYield_StartDate_M = ''
    ansYield_StopDate_M = ''
    ansYield_Month_M = ''
    excelYield_Month_M = ''
    
    
    if request.method == 'POST':
        ansYield_Plant_M = request.form['Plant']
        ansYield_Machines_M = request.form['Machines']
        ansYield_Shifts_M = 'ALL'
        ansYield_Month_M = request.form['Month12']
        ansYield_UserGroup_M = 'ALL'
        ansYield_Month_M_Report = ansYield_Month_M
        ansYield_Month_M = ansYield_Month_M.replace("-", "")
     
        print("---------------")
        print(ansYield_Plant_M)
        print(ansYield_Machines_M)
        print(ansYield_Shifts_M)
        print(ansYield_StartDate_M)
        print(ansYield_StopDate_M)
        print(ansYield_UserGroup_M)
        print(ansYield_Month_M)
        
        
        excelYield_Plant_M = ansYield_Plant_M
        excelYield_Machines_M = ansYield_Machines_M
        excelYield_Shifts_M   = ansYield_Shifts_M
        excelYield_Month_M = ansYield_Month_M_Report
       
        excelYield_UserGroup_M = ansYield_UserGroup_M
    
   
    if ansYield_Plant_M == 'ALL':
        ansYield_Plant_M = ''
    else : 
        ansYield_Plant_M = " AND PlantName = '"+ ansYield_Plant_M +"'"
        
    if ansYield_Machines_M == 'ALL':
        ansYield_Machines_M = ''
    else :  
        ansYield_Machines_M = " AND MachineID = '"+ ansYield_Machines_M +"'"
       
    if ansYield_Shifts_M == 'ALL':
        ansYield_Shifts_M = ''
    else : 
        ansYield_Shifts_M = " AND ShiftCode = '"+ ansYield_Shifts_M +"'"
        
    if ansYield_UserGroup_M == 'ALL':
        ansYield_UserGroup_M = ''
    else : 
        ansYield_UserGroup_M = " AND UserGroupID = '"+ ansYield_UserGroup_M +"'"
        
    if ansYield_Month_M == '':
        ansYield_Month_M = ''
    else : 
        ansYield_Month_M = " AND CAST(FORMAT(PostingDate, 'yyyyMM') AS int) = " + ansYield_Month_M 
         
        
    print("---------------")
    print(ansYield_Plant_M)
    print(ansYield_Machines_M)
    print(ansYield_Shifts_M)
    print(ansYield_StartDate_M)
    print(ansYield_StopDate_M)
    print(ansYield_Month_M)
     
    
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    Plant = cnxn.cursor()
    Plant.execute('SELECT PlantName FROM OEE_DB.dbo.Plant  WHERE DeleteFlag = 1')
    
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    Machines = cnxn.cursor()
    Machines.execute('SELECT MachineName ,MachineID FROM OEE_DB.dbo.Machines  WHERE DeleteFlag = 1')

    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    Shifts = cnxn.cursor()
    Shifts.execute('SELECT ShiftCodeName , ShiftCodeID FROM OEE_DB.dbo.ShiftCode  WHERE DeleteFlag = 1')
    
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    UserGroup = cnxn.cursor()
    UserGroup.execute('SELECT UserGroupName , UserGroupID FROM OEE_DB.dbo.UserGroup  WHERE DeleteFlag = 1')

    return render_template('Report_Yield_Montly.html',Plant = Plant , Machines = Machines , Shifts = Shifts,UserGroup=UserGroup,Level=Level,Fname_Lname=Fname_Lname)


@app.route('/Report_OEE_API' ,methods=["GET", "POST"])

def Report_OEE_API():
    global ansOEE_Plant
    global ansOEE_Machines
    global ansOEE_Shifts
    global ansOEE_StartDate
    global ansOEE_StopDate
    global ansOEE_UserGroup
    global where
    
    print("SELECT * FROM OEE_DB.dbo.View_OEEReport  WHERE OEE_Q2 IS NOT NULL " +ansOEE_Plant+ansOEE_Machines+ansOEE_Shifts+ansOEE_StartDate+ansOEE_StopDate)
        
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    ReportOEE = cnxn.cursor()
    ReportOEE.execute("SELECT * FROM OEE_DB.dbo.View_OEEReport WHERE OEE_Q2 IS NOT NULL "  +ansOEE_Plant+ansOEE_Machines+ansOEE_Shifts+ansOEE_UserGroup+ansOEE_StartDate+ansOEE_StopDate + " ORDER BY PDOrder ASC ")
   
    payload = []
    content = {}
    for result in ReportOEE:
        content = {'Plant': result[2], 'work_time': str(result[34] +" / " + result[33] ), 'Posting_Date': str(result[3]),'PD_order': result[4],'Material_number': str(result[5]),'Machine_Text': str(result[8]),'Material_Description': str(result[6]),'MachineID': str(result[7]),'Validate_Speed': str(result[9]),'Q1':  str(float("{:.2f}".format(result[25] * 100 ))) + '%','Plan_DT': str(result[10]),'Unlan_DT': str(result[11]),'ka_time': str(result[12]),'getwork_time_1': str(result[13]),'getwork_time_2': str(result[14]),'number_of_product': str(result[15]),'number_should_of_product_1':  float("{:.2f}".format(result[16])),'number_should_of_product_2':  float("{:.2f}".format(result[17])),'product_Qty': str(result[18]),'Return_Qty': str(result[19]),'product_Qty_F': str(result[20]),'UserGroup': str(result[32]),'Q2': str(float("{:.2f}".format(result[38] * 100 ))) + '%','Availability_A1': str(float("{:.2f}".format(result[21] * 100 ))) + '%','Availability_A2': str(float("{:.2f}".format(result[22] * 100 ))) + '%','Performance_P1': str(float("{:.2f}".format(result[23] * 100 ))) + '%','Performance_P2': str(float("{:.2f}".format(result[24] * 100 ))) + '%','Quality1F': str(float("{:.2f}".format(result[26] * 100 ))) + '%','Quality2F': str(float("{:.2f}".format(result[39] * 100 ))) + '%','OEE1': str(float("{:.2f}".format(result[27] * 100 ))) + '%','OEE2': str(float("{:.2f}".format(result[28] * 100 ))) + '%','OEE1_F': str(float("{:.2f}".format(result[29] * 100 ))) + '%','OEE2_F': str(float("{:.2f}".format(result[30] * 100 ))) + '%'}
        payload.append(content)
        content = {}
    #print(payload)
    return json.dumps({"data":payload}, cls = Encoder), 201

@app.route('/Report_OEE_Total_API' ,methods=["GET", "POST"])

def Report_OEE_Total_API():
    global ansOEE_Total_Plant
    global ansOEE_Total_Machines
    global ansOEE_Total_Shifts
    global ansOEE_Total_StartDate
    global ansOEE_Total_StopDate
    global ansOEE_Total_UserGroup
    global where
    
    print("SELECT * FROM OEE_DB.dbo.OEEReport_Total  WHERE OEE_Q2 IS NOT NULL " +ansOEE_Total_Plant+ansOEE_Total_Machines+ansOEE_Total_Shifts+ansOEE_Total_StartDate+ansOEE_Total_StopDate)
        
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    ReportOEE = cnxn.cursor()
    ReportOEE.execute("SELECT * FROM OEE_DB.dbo.OEEReport_Total WHERE OEE_Q2 IS NOT NULL "  +ansOEE_Total_Plant+ansOEE_Total_Machines+ansOEE_Total_Shifts+ansOEE_Total_UserGroup+ansOEE_Total_StartDate+ansOEE_Total_StopDate + " ORDER BY PDOrder ASC ")
   
    payload = []
    content = {}
    for result in ReportOEE:
        content = {'Plant': result[2], 'work_time': str(result[34] +" / " + result[33] ), 'Posting_Date': str(result[3]),'PD_order': result[4],'Material_number': str(result[5]),'Machine_Text': str(result[8]),'Material_Description': str(result[6]),'MachineID': str(result[7]),'Validate_Speed': str(result[9]),'Q1':  str(float("{:.2f}".format(result[25] * 100 ))) + '%','Plan_DT': str(result[10]),'Unlan_DT': str(result[11]),'ka_time': str(result[12]),'getwork_time_1': str(result[13]),'getwork_time_2': str(result[14]),'number_of_product': str(result[15]),'number_should_of_product_1':  float("{:.2f}".format(result[16])),'number_should_of_product_2':  float("{:.2f}".format(result[17])),'product_Qty': str(result[18]),'Return_Qty': str(result[19]),'product_Qty_F': str(result[20]),'UserGroup': str(result[32]),'Q2': str(float("{:.2f}".format(result[38] * 100 ))) + '%','Availability_A1': str(float("{:.2f}".format(result[21] * 100 ))) + '%','Availability_A2': str(float("{:.2f}".format(result[22] * 100 ))) + '%','Performance_P1': str(float("{:.2f}".format(result[23] * 100 ))) + '%','Performance_P2': str(float("{:.2f}".format(result[24] * 100 ))) + '%','Quality1F': str(float("{:.2f}".format(result[26] * 100 ))) + '%','Quality2F': str(float("{:.2f}".format(result[39] * 100 ))) + '%','OEE1': str(float("{:.2f}".format(result[27] * 100 ))) + '%','OEE2': str(float("{:.2f}".format(result[28] * 100 ))) + '%','OEE1_F': str(float("{:.2f}".format(result[29] * 100 ))) + '%','OEE2_F': str(float("{:.2f}".format(result[30] * 100 ))) + '%'}
        payload.append(content)
        content = {}
    #print(payload)
    return json.dumps({"data":payload}, cls = Encoder), 201

@app.route('/Report_OEE_API_EXCEL' ,methods=["GET", "POST"])

def Report_OEE_API_EXCEL():
    global ansOEE_Plant
    global ansOEE_Machines
    global ansOEE_Shifts
    global ansOEE_StartDate
    global ansOEE_StopDate
    global ansOEE_UserGroup
    global where
    
    print("SELECT * FROM OEE_DB.dbo.View_OEEReport  WHERE OEE_Q2 IS NOT NULL " +ansOEE_Plant+ansOEE_Machines+ansOEE_Shifts+ansOEE_StartDate+ansOEE_StopDate)
        
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    ReportOEE = cnxn.cursor()
    ReportOEE.execute("SELECT * FROM OEE_DB.dbo.View_OEEReport WHERE OEE_Q2 IS NOT NULL "  +ansOEE_Plant+ansOEE_Machines+ansOEE_Shifts+ansOEE_UserGroup+ansOEE_StartDate+ansOEE_StopDate + " ORDER BY PDOrder ASC ")
   
    payload = []
    content = {}
    for result in ReportOEE:
        #content = {'Plant': result[2], 'work_time': str(result[34] +" / " + result[33] ), 'Posting_Date': str(result[3]),'PD_order': result[4],'Material_number': str(result[5]),'Machine_Text': str(result[8]),'Material_Description': str(result[6]),'MachineID': str(result[7]),'Validate_Speed': str(result[10]),'Q1':  float("{:.2f}".format(result[25])),'Plan_DT': str(result[10]),'Unlan_DT': str(result[11]),'ka_time': str(result[12]),'getwork_time_1': str(result[13]),'getwork_time_2': str(result[14]),'number_of_product': str(result[15]),'number_should_of_product_1':  float("{:.2f}".format(result[16])),'number_should_of_product_2':  float("{:.2f}".format(result[17])),'product_Qty': str(result[18]),'Return_Qty': str(result[19]),'product_Qty_F': str(result[20]),'UserGroup': str(result[32]),'Q2': float("{:.2f}".format(result[38])),'Availability_A1': float("{:.2f}".format(result[21])),'Availability_A2': float("{:.2f}".format(result[22])),'Performance_P1': float("{:.2f}".format(result[23])),'Performance_P2': float("{:.2f}".format(result[24])),'Quality1F': float("{:.2f}".format(result[26])),'Quality2F': float("{:.2f}".format(result[39])),'OEE1': float("{:.2f}".format(result[27])),'OEE2': float("{:.2f}".format(result[28])),'OEE1_F': float("{:.2f}".format(result[29])),'OEE2_F': float("{:.2f}".format(result[30]))}
        content = {'Plant': result[2], '??????????????????????????????': str(result[34] +" / " + result[33] ), 'Posting Date': str(result[3]),'PD order': result[4],'Material number': str(result[5]),'Machine Text': str(result[8]),'Material Description': str(result[6]),'MachineID': str(result[7]),'Validate Speed': str(result[9]),'Plan DT': str(result[10]),'Unlan DT': str(result[11]),'?????????????????? (min)': result[12],'??????????????????????????????????????????1 (min)': str(result[13]),'??????????????????????????????????????????2 (min)': str(result[14]),'?????????????????????????????????????????????????????????????????? (Unit)': str(result[15]),'?????????????????????????????????????????????????????????????????????????????????1 (Unit)':  float("{:.2f}".format(result[16])),'?????????????????????????????????????????????????????????????????????????????????2 (Unit)':  float("{:.2f}".format(result[17])),'??????????????????????????????????????????????????????????????????????????? (Unit)': str(result[18]),'Return Qty (after 30 day) (Unit)': str(result[19]),'???????????????????????????????????????????????????????????????????????????????????????????????? (Unit)': str(result[20]),'UserGroup': str(result[32]),'Availability (A1)': str(float("{:.2f}".format(result[21] * 100))) + '%','Availability (A2)': str(float("{:.2f}".format(result[22] * 100))) + '%','Performance (P1)': str(float("{:.2f}".format(result[23] * 100))) + '%','Performance (P2)': str(float("{:.2f}".format(result[24] * 100))) + '%','Quality by PD order (Q1)':  str(float("{:.2f}".format(result[25] * 100))) + '%','Quality by shift (Q2)': str(float("{:.2f}".format(result[38] * 100))) + '%','Quality Final by PD order (Q1)': str(float("{:.2f}".format(result[26] * 100))) + '%','Quality Final by Shift (Q2)': str(float("{:.2f}".format(result[39] * 100))) + '%','OEE1': str(float("{:.2f}".format(result[27] * 100))) + '%','OEE2': str(float("{:.2f}".format(result[28] * 100))) + '%','OEE1_F': str(float("{:.2f}".format(result[29] * 100))) + '%','OEE2_F': str(float("{:.2f}".format(result[30] * 100))) + '%'}
        payload.append(content)
        content = {}
    #print(payload)
    return json.dumps(payload, cls = Encoder), 201


@app.route('/Report_OEE_Total_API_EXCEL' ,methods=["GET", "POST"])

def Report_OEE_Total_API_EXCEL():
    global ansOEE_Toatl_Plant
    global ansOEE_Toatl_Machines
    global ansOEE_Toatl_Shifts
    global ansOEE_Toatl_StartDate
    global ansOEE_Toatl_StopDate
    global ansOEE_Toatl_UserGroup
    global where
    
    print("SELECT * FROM OEE_DB.dbo.OEEReport_Total  WHERE OEE_Q2 IS NOT NULL " +ansOEE_Total_Plant+ansOEE_Total_Machines+ansOEE_Total_Shifts+ansOEE_Total_StartDate+ansOEE_Total_StopDate)
        
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    ReportOEE = cnxn.cursor()
    ReportOEE.execute("SELECT * FROM OEE_DB.dbo.OEEReport_Total WHERE OEE_Q2 IS NOT NULL "  +ansOEE_Total_Plant+ansOEE_Total_Machines+ansOEE_Total_Shifts+ansOEE_Total_UserGroup+ansOEE_Total_StartDate+ansOEE_Total_StopDate + " ORDER BY PDOrder ASC ")
   
    payload = []
    content = {}
    for result in ReportOEE:
        #content = {'Plant': result[2], 'work_time': str(result[34] +" / " + result[33] ), 'Posting_Date': str(result[3]),'PD_order': result[4],'Material_number': str(result[5]),'Machine_Text': str(result[8]),'Material_Description': str(result[6]),'MachineID': str(result[7]),'Validate_Speed': str(result[10]),'Q1':  float("{:.2f}".format(result[25])),'Plan_DT': str(result[10]),'Unlan_DT': str(result[11]),'ka_time': str(result[12]),'getwork_time_1': str(result[13]),'getwork_time_2': str(result[14]),'number_of_product': str(result[15]),'number_should_of_product_1':  float("{:.2f}".format(result[16])),'number_should_of_product_2':  float("{:.2f}".format(result[17])),'product_Qty': str(result[18]),'Return_Qty': str(result[19]),'product_Qty_F': str(result[20]),'UserGroup': str(result[32]),'Q2': float("{:.2f}".format(result[38])),'Availability_A1': float("{:.2f}".format(result[21])),'Availability_A2': float("{:.2f}".format(result[22])),'Performance_P1': float("{:.2f}".format(result[23])),'Performance_P2': float("{:.2f}".format(result[24])),'Quality1F': float("{:.2f}".format(result[26])),'Quality2F': float("{:.2f}".format(result[39])),'OEE1': float("{:.2f}".format(result[27])),'OEE2': float("{:.2f}".format(result[28])),'OEE1_F': float("{:.2f}".format(result[29])),'OEE2_F': float("{:.2f}".format(result[30]))}
        content = {'Plant': result[2], '??????????????????????????????': str(result[34] +" / " + result[33] ), 'Posting Date': str(result[3]),'PD order': result[4],'Material number': str(result[5]),'Machine Text': str(result[8]),'Material Description': str(result[6]),'MachineID': str(result[7]),'Validate Speed': str(result[9]),'Plan DT': str(result[10]),'Unlan DT': str(result[11]),'?????????????????? (min)': result[12],'??????????????????????????????????????????1 (min)': str(result[13]),'??????????????????????????????????????????2 (min)': str(result[14]),'?????????????????????????????????????????????????????????????????? (Unit)': str(result[15]),'?????????????????????????????????????????????????????????????????????????????????1 (Unit)':  float("{:.2f}".format(result[16])),'?????????????????????????????????????????????????????????????????????????????????2 (Unit)':  float("{:.2f}".format(result[17])),'??????????????????????????????????????????????????????????????????????????? (Unit)': str(result[18]),'Return Qty (after 30 day) (Unit)': str(result[19]),'???????????????????????????????????????????????????????????????????????????????????????????????? (Unit)': str(result[20]),'UserGroup': str(result[32]),'Availability (A1)': str(float("{:.2f}".format(result[21] * 100))) + '%','Availability (A2)': str(float("{:.2f}".format(result[22] * 100))) + '%','Performance (P1)': str(float("{:.2f}".format(result[23] * 100))) + '%','Performance (P2)': str(float("{:.2f}".format(result[24] * 100))) + '%','Quality by PD order (Q1)':  str(float("{:.2f}".format(result[25] * 100))) + '%','Quality by shift (Q2)': str(float("{:.2f}".format(result[38] * 100))) + '%','Quality Final by PD order (Q1)': str(float("{:.2f}".format(result[26] * 100))) + '%','Quality Final by Shift (Q2)': str(float("{:.2f}".format(result[39] * 100))) + '%','OEE1': str(float("{:.2f}".format(result[27] * 100))) + '%','OEE2': str(float("{:.2f}".format(result[28] * 100))) + '%','OEE1_F': str(float("{:.2f}".format(result[29] * 100))) + '%','OEE2_F': str(float("{:.2f}".format(result[30] * 100))) + '%'}
        payload.append(content)
        content = {}
    #print(payload)
    return json.dumps(payload, cls = Encoder), 201

    
@app.route('/Report_OEE_Excel')
@flask_login.login_required
def Report_OEE_Excel():
   
    global excelOEE_Plant
    global excelOEE_Machines 
    global excelOEE_Shifts   
    global excelOEE_StartDate 
    global excelOEE_StopDate 
    global excelOEE_UserGroup 
        
    if excelOEE_StopDate == '':
        excelOEE_StopDate = 'ALL'
   
         
    if excelOEE_StartDate == '':
        excelOEE_StartDate = 'ALL'
  
    df = pd.read_json('http://172.30.2.2:5001//Report_OEE_API_EXCEL')
    print(df)
    df.to_excel('OEE_Report1.xlsx',index=False)
    
    time.sleep(1)
    
    wabu = openpyxl.load_workbook('OEE_Report1.xlsx')
    washi = wabu.active
    washi.insert_rows(1,5)
    washi['A1'] = 'Report OEE'
    washi['A1'].alignment = Alignment(vertical='center')
    washi['A1'].alignment = Alignment(horizontal='center')
    washi['A1'].font = Font(color='FFFFFF',
                        size=24,bold=True)
    washi['A1'].fill = PatternFill(patternType='solid',fgColor='154360')
    
    washi.merge_cells('A1:F1')
    
    washi['A3'] = 'By Plant'
    washi['A3'].font = Font(color='FFFFFF',
                        size=12,bold=True)
    washi['A3'].fill = PatternFill(patternType='solid',fgColor='154360')
    
    washi['A4'] = 'By Machine'
    washi['A4'].font = Font(color='FFFFFF',
                        size=12,bold=True)
    washi['A4'].fill = PatternFill(patternType='solid',fgColor='154360')
    
    washi['C3'] = 'By Shifts'
    washi['C3'].font = Font(color='FFFFFF',
                        size=12,bold=True)
    washi['C3'].fill = PatternFill(patternType='solid',fgColor='154360')
    
    washi['C4'] = 'By UserGroup'
    washi['C4'].font = Font(color='FFFFFF',
                        size=12,bold=True)
    washi['C4'].fill = PatternFill(patternType='solid',fgColor='154360')
    
    washi['E3'] = 'Start Date'
    washi['E3'].font = Font(color='FFFFFF',
                       size=12,bold=True)
    washi['E3'].fill = PatternFill(patternType='solid',fgColor='154360')
    
    washi['E4'] = 'Stop Date'
    washi['E4'].font = Font(color='FFFFFF',
                       size=12,bold=True)
    washi['E4'].fill = PatternFill(patternType='solid',fgColor='154360')
    
    washi['E3'] = 'Start Date'
    washi['E3'].font = Font(color='FFFFFF',
                       size=12,bold=True)
    washi['E3'].fill = PatternFill(patternType='solid',fgColor='154360')
    
    washi['B3'] = str(excelOEE_Plant)
    washi['B3'].font = Font(color='000000',
                       size=12,bold=True)
    washi['B3'].fill = PatternFill(patternType='solid',fgColor='AED6F1')
    
    washi['B4'] = str(excelOEE_Machines)
    washi['B4'].font = Font(color='000000',
                       size=12,bold=True)
    washi['B4'].fill = PatternFill(patternType='solid',fgColor='AED6F1')
    
    washi['D3'] = str(excelOEE_Shifts)
    washi['D3'].font = Font(color='000000',
                       size=12,bold=True)
    washi['D3'].fill = PatternFill(patternType='solid',fgColor='AED6F1')
    
    washi['D4'] = str(excelOEE_UserGroup)
    washi['D4'].font = Font(color='000000',
                       size=12,bold=True)
    washi['D4'].fill = PatternFill(patternType='solid',fgColor='AED6F1')
    
    washi['F3'] = str(excelOEE_StartDate)
    washi['F3'].font = Font(color='000000',
                       size=12,bold=True)
    washi['F3'].fill = PatternFill(patternType='solid',fgColor='AED6F1')
    
    washi['F4'] = str(excelOEE_StopDate)
    washi['F4'].font = Font(color='000000',
                       size=12,bold=True)
    washi['F4'].fill = PatternFill(patternType='solid',fgColor='AED6F1')
    
    washi.column_dimensions['A'].width = 16
    washi.column_dimensions['B'].width = 25
    washi.column_dimensions['C'].width = 20
    washi.column_dimensions['D'].width = 20
    washi.column_dimensions['E'].width = 20
    washi.column_dimensions['F'].width = 25
    wabu.save('OEE_Report1.xlsx')
    
    return send_file('..\OEE_Report1.xlsx') 

@app.route('/Report_OEE_Total_Excel')
@flask_login.login_required
def Report_OEE_Total_Excel():
   
    global excelOEE_Total_Plant
    global excelOEE_Total_Machines 
    global excelOEE_Total_Shifts   
    global excelOEE_Total_StartDate 
    global excelOEE_Total_StopDate 
    global excelOEE_Total_UserGroup 
        
    if excelOEE_Total_StopDate == '':
        excelOEE_Total_StopDate = 'ALL'
   
         
    if excelOEE_Total_StartDate == '':
        excelOEE_Total_StartDate = 'ALL'
  
    df = pd.read_json('http://172.30.2.2:5001//Report_OEE_Total_API_EXCEL')
    print(df)
    df.to_excel('OEE_Report1_Total.xlsx',index=False)
    
    time.sleep(1)
    
    wabu = openpyxl.load_workbook('OEE_Report1_Total.xlsx')
    washi = wabu.active
    washi.insert_rows(1,5)
    washi['A1'] = 'Report OEE(Total)'
    washi['A1'].alignment = Alignment(vertical='center')
    washi['A1'].alignment = Alignment(horizontal='center')
    washi['A1'].font = Font(color='FFFFFF',
                        size=24,bold=True)
    washi['A1'].fill = PatternFill(patternType='solid',fgColor='154360')
    
    washi.merge_cells('A1:F1')
    
    washi['A3'] = 'By Plant'
    washi['A3'].font = Font(color='FFFFFF',
                        size=12,bold=True)
    washi['A3'].fill = PatternFill(patternType='solid',fgColor='154360')
    
    washi['A4'] = 'By Machine'
    washi['A4'].font = Font(color='FFFFFF',
                        size=12,bold=True)
    washi['A4'].fill = PatternFill(patternType='solid',fgColor='154360')
    
    washi['C3'] = 'By Shifts'
    washi['C3'].font = Font(color='FFFFFF',
                        size=12,bold=True)
    washi['C3'].fill = PatternFill(patternType='solid',fgColor='154360')
    
    washi['C4'] = 'By UserGroup'
    washi['C4'].font = Font(color='FFFFFF',
                        size=12,bold=True)
    washi['C4'].fill = PatternFill(patternType='solid',fgColor='154360')
    
    washi['E3'] = 'Start Date'
    washi['E3'].font = Font(color='FFFFFF',
                       size=12,bold=True)
    washi['E3'].fill = PatternFill(patternType='solid',fgColor='154360')
    
    washi['E4'] = 'Stop Date'
    washi['E4'].font = Font(color='FFFFFF',
                       size=12,bold=True)
    washi['E4'].fill = PatternFill(patternType='solid',fgColor='154360')
    
    washi['E3'] = 'Start Date'
    washi['E3'].font = Font(color='FFFFFF',
                       size=12,bold=True)
    washi['E3'].fill = PatternFill(patternType='solid',fgColor='154360')
    
    washi['B3'] = str(excelOEE_Total_Plant)
    washi['B3'].font = Font(color='000000',
                       size=12,bold=True)
    washi['B3'].fill = PatternFill(patternType='solid',fgColor='AED6F1')
    
    washi['B4'] = str(excelOEE_Total_Machines)
    washi['B4'].font = Font(color='000000',
                       size=12,bold=True)
    washi['B4'].fill = PatternFill(patternType='solid',fgColor='AED6F1')
    
    washi['D3'] = str(excelOEE_Total_Shifts)
    washi['D3'].font = Font(color='000000',
                       size=12,bold=True)
    washi['D3'].fill = PatternFill(patternType='solid',fgColor='AED6F1')
    
    washi['D4'] = str(excelOEE_Total_UserGroup)
    washi['D4'].font = Font(color='000000',
                       size=12,bold=True)
    washi['D4'].fill = PatternFill(patternType='solid',fgColor='AED6F1')
    
    washi['F3'] = str(excelOEE_Total_StartDate)
    washi['F3'].font = Font(color='000000',
                       size=12,bold=True)
    washi['F3'].fill = PatternFill(patternType='solid',fgColor='AED6F1')
    
    washi['F4'] = str(excelOEE_Total_StopDate)
    washi['F4'].font = Font(color='000000',
                       size=12,bold=True)
    washi['F4'].fill = PatternFill(patternType='solid',fgColor='AED6F1')
    
    washi.column_dimensions['A'].width = 16
    washi.column_dimensions['B'].width = 25
    washi.column_dimensions['C'].width = 20
    washi.column_dimensions['D'].width = 20
    washi.column_dimensions['E'].width = 20
    washi.column_dimensions['F'].width = 25
    wabu.save('OEE_Report1_Total.xlsx')
    
    return send_file('..\OEE_Report1_Total.xlsx') 
        
        
@app.route('/Report_Yield_API' ,methods=["GET", "POST"])

def Report_Yield_API():
    global ansYield_Plant
    global ansYield_Machines
    global ansYield_Shifts
    global ansYield_StartDate
    global ansYield_StopDate
    global ansYield_UserGroup
    global where
    
    print("SELECT * FROM OEE_DB.dbo.View_YieldReport WHERE Yield IS NOT NULL AND QC_Status = 'P' " +ansYield_Plant+ansYield_Machines+ansYield_Shifts+ansYield_StartDate+ansYield_StopDate)
        
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    ReportYield = cnxn.cursor()
    ReportYield.execute("SELECT * FROM OEE_DB.dbo.View_YieldReport WHERE Yield IS NOT NULL "  +ansYield_Plant+ansYield_Machines+ansYield_Shifts+ansYield_UserGroup+ansYield_StartDate+ansYield_StopDate)
   
    payload = []
    content = {}
    for result in ReportYield:
        content = {'Plant': result[3], 'Posting_Date': str(result[4]),'PD_order': result[5],'Material_number': result[6],'Material_Description': result[7],'MachineName': result[9],'MachineID': result[8],'QA_Status': result[10],'Input_Qty':  result[13],'Output_Qty': result[14],'Return_Qty': result[15],'Yield': str(float("{:.2f}".format(result[17] * 100))) + '%','Final_Yield': str(float("{:.2f}".format(result[18] * 100))) + '%'}
        payload.append(content)
        content = {}
    print(payload)
    return json.dumps({"data":payload}, cls = Encoder), 201


@app.route('/Report_Yield_API_EXCEL' ,methods=["GET", "POST"])

def Report_Yield_API_EXCEL():
    global ansYield_Plant
    global ansYield_Machines
    global ansYield_Shifts
    global ansYield_StartDate
    global ansYield_StopDate
    global ansYield_UserGroup
    global where
    
    print("SELECT * FROM OEE_DB.dbo.View_YieldReport WHERE Yield IS NOT NULL AND QC_Status = 'P' " +ansYield_Plant+ansYield_Machines+ansYield_Shifts+ansYield_StartDate+ansYield_StopDate)
        
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    ReportYield = cnxn.cursor()
    ReportYield.execute("SELECT * FROM OEE_DB.dbo.View_YieldReport WHERE Yield IS NOT NULL "  +ansYield_Plant+ansYield_Machines+ansYield_Shifts+ansYield_UserGroup+ansYield_StartDate+ansYield_StopDate)
   
    payload = []
    content = {}
    for result in ReportYield:
        content = {'Plant': result[3], 'Posting_Date': str(result[4]),'PD_order': result[5],'Material_number': result[6],'Material_Description': result[7],'MachineName': result[9],'MachineID': result[8],'QA_Status': result[10],'Input_Qty':  result[13],'Output_Qty': result[14],'Return_Qty': result[15],'Yield': str(float("{:.2f}".format(result[17] * 100))) + '%','Final_Yield': str(float("{:.2f}".format(result[18] * 100))) + '%'}
        payload.append(content)
        content = {}
    print(payload)
    return json.dumps(payload, cls = Encoder), 201

@app.route('/Report_Yield_Excel')
@flask_login.login_required
def Report_Yield_Excel():
   
    global excelYield_Plant
    global excelYield_Machines 
    global excelYield_Shifts   
    global excelYield_StartDate 
    global excelYield_StopDate 
    global excelYield_UserGroup 
        
    if excelYield_StopDate == '':
        excelYield_StopDate = 'ALL'
   
         
    if excelYield_StartDate == '':
        excelYield_StartDate = 'ALL'
  
    df = pd.read_json('http://172.30.2.2:5001//Report_Yield_API_EXCEL')
    df.to_excel('Yield_Report1.xlsx',index=False)
    
    time.sleep(1)
    wabu = openpyxl.load_workbook('Yield_Report1.xlsx')
    washi = wabu.active
    washi.insert_rows(1,5)
    washi['A1'] = 'Report Yield'
    washi['A1'].alignment = Alignment(vertical='center')
    washi['A1'].alignment = Alignment(horizontal='center')
    washi['A1'].font = Font(color='FFFFFF',
                        size=24,bold=True)
    washi['A1'].fill = PatternFill(patternType='solid',fgColor='154360')
    
    washi.merge_cells('A1:F1')
    
    washi['A3'] = 'By Plant'
    washi['A3'].font = Font(color='FFFFFF',
                        size=12,bold=True)
    washi['A3'].fill = PatternFill(patternType='solid',fgColor='154360')
    
    washi['A4'] = 'By Machine'
    washi['A4'].font = Font(color='FFFFFF',
                        size=12,bold=True)
    washi['A4'].fill = PatternFill(patternType='solid',fgColor='154360')

    
    washi['D3'] = 'Start Date'
    washi['D3'].font = Font(color='FFFFFF',
                       size=12,bold=True)
    washi['D3'].fill = PatternFill(patternType='solid',fgColor='154360')
    
    washi['D4'] = 'Stop Date'
    washi['D4'].font = Font(color='FFFFFF',
                       size=12,bold=True)
    washi['D4'].fill = PatternFill(patternType='solid',fgColor='154360')
    
    
    washi['B3'] = str(excelYield_Plant)
    washi['B3'].font = Font(color='000000',
                       size=12,bold=True)
    washi['B3'].fill = PatternFill(patternType='solid',fgColor='AED6F1')
    
    washi['B4'] = str(excelYield_Machines)
    washi['B4'].font = Font(color='000000',
                       size=12,bold=True)
    washi['B4'].fill = PatternFill(patternType='solid',fgColor='AED6F1')
    
    
    washi['E3'] = str(excelYield_StartDate)
    washi['E3'].font = Font(color='000000',
                       size=12,bold=True)
    washi['E3'].fill = PatternFill(patternType='solid',fgColor='AED6F1')
    
    washi['E4'] = str(excelYield_StopDate)
    washi['E4'].font = Font(color='000000',
                       size=12,bold=True)
    washi['E4'].fill = PatternFill(patternType='solid',fgColor='AED6F1')
    
    washi.column_dimensions['A'].width = 16
    washi.column_dimensions['B'].width = 25
    washi.column_dimensions['C'].width = 20
    washi.column_dimensions['D'].width = 20
    washi.column_dimensions['E'].width = 25

    wabu.save('Yield_Report1.xlsx')
    
    return send_file('..\Yield_Report1.xlsx') 

@app.route('/Report_M_OEE_API' ,methods=["GET", "POST"])

def Report_M_OEE_API():
        
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    OEEReport_Monthly_Show = cnxn.cursor()
    OEEReport_Monthly_Show.execute('Select * from OEE_DB.dbo.OEEMonthlyReport')    
    payload = []
    content = {}
    
    for result in OEEReport_Monthly_Show:
        
        content = {'Month': result[1] , 'Plant': result[3],'MachineID': str(result[4]),'Machine_Text': str(result[5]),'PlanDownTime':  result[6],'UnplanDownTime': str(result[7]),'RunTime1': str(result[8]),'RunTime2': str(result[9]),'Per_PantDownTime':  str(float("{:.2f}".format(result[10] *100))) + '%','Per_UnplanDowntime':  str(float("{:.2f}".format(result[11] *100 )) ) + '%','Per_Downtime': str(float("{:.2f}".format(result[12] *100))) + '%','Per_PantDownTime2': str(float("{:.2f}".format(result[13] *100))) + '%','Per_UnplanDowntime2': str(float("{:.2f}".format(result[14] * 100))) + '%','Per_Downtime2':str(float("{:.2f}".format(result[15] *100))) + '%','TotalCount': float("{:.2f}".format(result[16])),'IdealCount1': float("{:.2f}".format(result[17])),'IdealCount2': float("{:.2f}".format(result[18])),'GoodCount': float("{:.2f}".format(result[19])),'PostReturn': float("{:.2f}".format(result[20])),'FinalGoodCount': float("{:.2f}".format(result[21])),'OEE_A1': str(float("{:.2f}".format(result[22] *100))) + '%','OEE_A2': str(float("{:.2f}".format(result[23] *100))) + '%','OEE_P1': str(float("{:.2f}".format(result[24] *100))) + '%','OEE_P2': str(float("{:.2f}".format(result[25] *100))) + '%','OEE_Q': str(float("{:.2f}".format(result[26] *100))) + '%','OEE_Q_Finnal': str(float("{:.2f}".format(result[27] *100))) + '%','OEE1Calculation': str(float("{:.2f}".format(result[28] *100))) + '%','OEE2Calculation': str(float("{:.2f}".format(result[29] *100))) + '%','OEE1FinalCalculation': str(float("{:.2f}".format(result[30] *100))) + '%','OEE2FinalCalculation': str(float("{:.2f}".format(result[31] *100))) + '%'}
        payload.append(content)
        content = {}
        
    #print(payload)
    return json.dumps({"data":payload}, cls = Encoder), 201

@app.route('/Report_M_OEE_API_Excel' ,methods=["GET", "POST"])

def Report_M_OEE_API_Excel():
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    OEEReport_Monthly_Show = cnxn.cursor()
    OEEReport_Monthly_Show.execute('Select * from OEE_DB.dbo.OEEMonthlyReport')    
    payload = []
    content = {}
    
    for result in OEEReport_Monthly_Show:
            
        content = {'Month':  result[1]  , 'Plant': result[3],'MachineID': str(result[4]),'Machine_Text': str(result[5]),'PlanDownTime':  result[6],'UnplanDownTime': str(result[7]),'RunTime1': str(result[8]),'RunTime2': str(result[9]),'Per_PantDownTime':  str(float("{:.2f}".format(result[10] *100))) + '%','Per_UnplanDowntime':  str(float("{:.2f}".format(result[11] *100 )) ) + '%','Per_Downtime': str(float("{:.2f}".format(result[12] *100))) + '%','Per_PantDownTime2': str(float("{:.2f}".format(result[13] *100))) + '%','Per_UnplanDowntime2': str(float("{:.2f}".format(result[14] * 100))) + '%','Per_Downtime2':str(float("{:.2f}".format(result[15] *100))) + '%','TotalCount': float("{:.2f}".format(result[16])),'IdealCount1': float("{:.2f}".format(result[17])),'IdealCount2': float("{:.2f}".format(result[18])),'GoodCount': float("{:.2f}".format(result[19])),'PostReturn': float("{:.2f}".format(result[20])),'FinalGoodCount': float("{:.2f}".format(result[21])),'OEE_A1': str(float("{:.2f}".format(result[22] *100))) + '%','OEE_A2': str(float("{:.2f}".format(result[23] *100))) + '%','OEE_P1': str(float("{:.2f}".format(result[24] *100))) + '%','OEE_P2': str(float("{:.2f}".format(result[25] *100))) + '%','OEE_Q': str(float("{:.2f}".format(result[26] *100))) + '%','OEE_Q_Finnal': str(float("{:.2f}".format(result[27] *100))) + '%','OEE1Calculation': str(float("{:.2f}".format(result[28] *100))) + '%','OEE2Calculation': str(float("{:.2f}".format(result[29] *100))) + '%','OEE1FinalCalculation': str(float("{:.2f}".format(result[30] *100))) + '%','OEE2FinalCalculation': str(float("{:.2f}".format(result[31] *100))) + '%'}
        payload.append(content)
        content = {}
        
    #print(payload)
    return json.dumps(payload, cls = Encoder), 201

@app.route('/Report_OEE_M_Excel')
@flask_login.login_required
def Report_OEE_M_Excel():
   
    global excelOEE_Plant_M
    global excelOEE_Machines_M 
    global excelOEE_Shifts_M  
    global excelOEE_Month_M 
   
  
    df = pd.read_json('http://172.30.2.2:5001/Report_M_OEE_API_Excel')
    df.to_excel('OEE_Montly_Report.xlsx',index=False)
    
    time.sleep(1)
    wabu = openpyxl.load_workbook('OEE_Montly_Report.xlsx')
    washi = wabu.active
    washi.insert_rows(1,5)
    washi['A1'] = 'Report OEE (Montly)'
    washi['A1'].alignment = Alignment(vertical='center')
    washi['A1'].alignment = Alignment(horizontal='center')
    washi['A1'].font = Font(color='FFFFFF',
                        size=24,bold=True)
    washi['A1'].fill = PatternFill(patternType='solid',fgColor='154360')
    
    washi.merge_cells('A1:F1')
    
    washi['A3'] = 'By Plant'
    washi['A3'].font = Font(color='FFFFFF',
                        size=12,bold=True)
    washi['A3'].fill = PatternFill(patternType='solid',fgColor='154360')
    
    washi['A4'] = 'By Machine'
    washi['A4'].font = Font(color='FFFFFF',
                        size=12,bold=True)
    washi['A4'].fill = PatternFill(patternType='solid',fgColor='154360')

    
    washi['E3'] = 'Year-Month'
    washi['E3'].font = Font(color='FFFFFF',
                       size=12,bold=True)
    washi['E3'].fill = PatternFill(patternType='solid',fgColor='154360')
    
    
    washi['B3'] = str(excelOEE_Plant)
    washi['B3'].font = Font(color='000000',
                       size=12,bold=True)
    washi['B3'].fill = PatternFill(patternType='solid',fgColor='AED6F1')
    
    washi['B4'] = str(excelOEE_Machines)
    washi['B4'].font = Font(color='000000',
                       size=12,bold=True)
    washi['B4'].fill = PatternFill(patternType='solid',fgColor='AED6F1')
    
   
    
    washi['F3'] = str(excelOEE_Month_M)
    washi['F3'].font = Font(color='000000',
                       size=12,bold=True)
    washi['F3'].fill = PatternFill(patternType='solid',fgColor='AED6F1')
    
   
    
    washi.column_dimensions['A'].width = 16
    washi.column_dimensions['B'].width = 25
    washi.column_dimensions['C'].width = 20
    washi.column_dimensions['D'].width = 20
    washi.column_dimensions['E'].width = 20
    washi.column_dimensions['F'].width = 25
    wabu.save('OEE_Montly_Report.xlsx')
    
    return send_file('..\OEE_Montly_Report.xlsx') 

@app.route('/Report_M_Yield_API' ,methods=["GET", "POST"])

def Report_M_Yield_API():
    
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    YieldReport_Monthly_Show = cnxn.cursor()
    YieldReport_Monthly_Show.execute('Select * from OEE_DB.dbo.YieldMonthlyReport')    
    payload = []
    content = {}

    for result in YieldReport_Monthly_Show:
        
        content = {'Month': result[11] , 'Plant': result[2],'MachineID': str(result[3]),'Machine_Text': str(result[4]),'InputQty': float("{:.2f}".format(result[5])),'OutputQty': float("{:.2f}".format(result[6])),'ReturnQty': float("{:.2f}".format(result[7])),'Yield':  str(float("{:.2f}".format(result[8] * 100))) + '%','FinalYield':  str(float("{:.2f}".format(result[9] * 100))) + '%'}
        payload.append(content)
        content = {}
        
    #print(payload)
    return json.dumps({"data":payload}, cls = Encoder), 201

@app.route('/Report_M_Yield_API_Excel' ,methods=["GET", "POST"])
def Report_M_Yield_API_Excel():
    
    
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    YieldReport_Monthly_Show = cnxn.cursor()
    YieldReport_Monthly_Show.execute('Select * from OEE_DB.dbo.YieldMonthlyReport')    
    payload = []
    content = {}
    
    for result in YieldReport_Monthly_Show:
        
        content = {'Month': result[11] , 'Plant': result[2],'MachineID': str(result[3]),'Machine_Text': str(result[4]),'InputQty': float("{:.2f}".format(result[5])),'OutputQty': float("{:.2f}".format(result[6])),'ReturnQty': float("{:.2f}".format(result[7])),'Yield':  str(float("{:.2f}".format(result[8] * 100))) + '%','FinalYield':  str(float("{:.2f}".format(result[9] * 100))) + '%'}
        payload.append(content)
        content = {}
    

    return json.dumps(payload, cls = Encoder), 201

@app.route('/Report_Yield_M_Excel')
@flask_login.login_required
def Report_Yield_M_Excel():
   
    global excelYield_Plant_M
    global excelYield_Machines_M 
    global excelYield_Shifts_M  
    global excelYield_Month_M 

   
  
    df = pd.read_json('http://172.30.2.2:5001/Report_M_Yield_API_Excel')
    df.to_excel('Yield_Montly_Report.xlsx',index=False)

    time.sleep(1)
    wabu = openpyxl.load_workbook('Yield_Montly_Report.xlsx')
    washi = wabu.active
    washi.insert_rows(1,5)
    washi['A1'] = 'Report Yield'
    washi['A1'].alignment = Alignment(vertical='center')
    washi['A1'].alignment = Alignment(horizontal='center')
    washi['A1'].font = Font(color='FFFFFF',
                        size=24,bold=True)
    washi['A1'].fill = PatternFill(patternType='solid',fgColor='154360')
    
    washi.merge_cells('A1:F1')
    
    washi['A3'] = 'By Plant'
    washi['A3'].font = Font(color='FFFFFF',
                        size=12,bold=True)
    washi['A3'].fill = PatternFill(patternType='solid',fgColor='154360')
    
    washi['A4'] = 'By Machine'
    washi['A4'].font = Font(color='FFFFFF',
                        size=12,bold=True)
    washi['A4'].fill = PatternFill(patternType='solid',fgColor='154360')
    
  
    
    washi['E3'] = 'Year-Month'
    washi['E3'].font = Font(color='FFFFFF',
                       size=12,bold=True)
    washi['E3'].fill = PatternFill(patternType='solid',fgColor='154360')
    
    
    washi['B3'] = str(excelYield_Plant)
    washi['B3'].font = Font(color='000000',
                       size=12,bold=True)
    washi['B3'].fill = PatternFill(patternType='solid',fgColor='AED6F1')
    
    washi['B4'] = str(excelYield_Machines)
    washi['B4'].font = Font(color='000000',
                       size=12,bold=True)
    washi['B4'].fill = PatternFill(patternType='solid',fgColor='AED6F1')
    
    
    washi['F3'] = str(excelYield_Month_M)
    washi['F3'].font = Font(color='000000',
                       size=12,bold=True)
    washi['F3'].fill = PatternFill(patternType='solid',fgColor='AED6F1')
    
   
    washi.column_dimensions['A'].width = 16
    washi.column_dimensions['B'].width = 25
    washi.column_dimensions['C'].width = 20
    washi.column_dimensions['D'].width = 20
    washi.column_dimensions['E'].width = 20
    washi.column_dimensions['F'].width = 25
    wabu.save('Yield_Montly_Report.xlsx')
    
    return send_file('..\Yield_Montly_Report.xlsx') 

#-------------------- API --------------------------------------
@app.route('/API_Login',methods=["GET", "POST"])
def API_Login():    
    global UserLogin
    global UserLevelLogin
    Time = datetime.now()
    payload = []   
    content = {}
    content = {'User': UserLogin, 'Level':UserLevelLogin,'Time': str(Time) }
    payload.append(content)
    content = {}
    #print(payload)
    return json.dumps({"LoginOEE":payload}, cls = Encoder), 201


#--------------------------------------------------------------
@app.route('/batch_report')
def batch_report():
    #cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+ host +';DATABASE='+database+';UID='+user+';PWD='+passwd)
    #SQL_Login = cnxn.cursor()
    #SQL_Login.execute("Exec USP_Journal_Rpt '" + Campaign_ID + "','"+ Lot_ID +"','"+ StartOfPeriod_DT + "','"+EndOfPeriod_DT+"'" )
    return render_template('batch_report.html')

@app.route('/report')
def report():
    #cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+ host +';DATABASE='+database+';UID='+user+';PWD='+passwd)
    #SQL_Login = cnxn.cursor()
    #SQL_Login.execute("Exec USP_Journal_Rpt '" + Campaign_ID + "','"+ Lot_ID +"','"+ StartOfPeriod_DT + "','"+EndOfPeriod_DT+"'" )
    
    return render_template('report.html')


@app.route('/report/RawMaterial/<string:pdOrder>')
def Raw_Material(pdOrder):
    return render_template('reportRawMaterial.html',pdOrder=pdOrder)

@app.route('/report/Raw_Material_API/<string:pdOrder>')
def Raw_Material_API(pdOrder):
    host = "172.30.1.1"
    port = 1433
    database = "managedb"
    user = "sa"
    passwd = "qwerty@2019"
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+ host +';DATABASE='+database+';UID='+user+';PWD='+passwd)
    RM = cnxn.cursor()
    RM.execute("SELECT * FROM [dbo].[View_RM_Process_tab] where RM_PD_ORDER = '" + pdOrder + "'")
    
    payload = []
    content = {}
    for result in RM:
        
        content = {'RM_RAW_ID': result[1], 'RM_NAME': str(result[2]), 'RM_UNIT': result[3],'PW_NEO_NAME': result[4],'RM_PW_TARGET': result[5],'RM_PW_ACTUAL': str(result[6]),'RM_REQ_DATE': str(result[7]),'RM_INS_DT': str(result[8]),'PW_ITEM_TOTAL': str(result[9]),'RM_PW_EACH_ITEM': str(result[10]),'RM_BARCODE_LIST': str(result[11]),'RM_FFTANK_STATUS': str(result[12]),'RM_FFTANK_1': str(result[13]),'RM_SFTANK_1': str(result[14]),'RM_REF_NO': str(result[15]),'UserDisplayName': str(result[16])}
        payload.append(content)
        content = {}
    #print(payload)
    return json.dumps({"data":payload}, cls = Encoder), 201

@app.route('/report/Overview/<string:pdOrder>')
def reportOverview(pdOrder):    
    
    return render_template('reportOverview.html',pdOrder=pdOrder)


@app.route('/report/PreMixing/<string:pdOrder>')
def reportPreMixing(pdOrder):    
    server = "172.30.2.2"
    port = 5432
    database = "OEE_DB"
    username = "sa"
    password = "p@ssw0rd"
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+ server +';DATABASE='+database+';UID='+username+';PWD='+password)
    PreMixing = cnxn.cursor()
    PreMixing.execute("SELECT RecordID, PD_ORDER, PhaseID, Status, Start_time, End_Time, SetPoint1, Actual1, SetPoint2, Actual2, SetPoint3, Actual3, SetPoint4, Actual4, SetPoint5, Actual5, SetPoint6, Actual6, SetPoint7, Actual7, SetPoint8, Actual8, User_Mixing ,DATEDIFF(second,Start_time,End_Time) as Time_Sec  FROM SCADA_DB.dbo.Mixing_Report mr  WHERE PhaseID > 100 AND PhaseID < 200 AND PD_ORDER = '" +pdOrder+ "' ORDER BY Start_time ASC")
    
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+ server +';DATABASE='+database+';UID='+username+';PWD='+password)
    Phase_Parameter = cnxn.cursor()
    Phase_Parameter.execute("SELECT PhaseID ,PhaseName,Parameter1,Parameter2,Parameter3,Parameter4,Parameter5,Parameter6,Parameter7,Parameter8 FROM SCADA_DB.dbo.Phase_Parameter") 
    
    Phase_Parameter_DIR = Phase_Parameter.fetchall()

    insertObject = []
    columnNames = [column[0] for column in Phase_Parameter.description]
    for record in Phase_Parameter_DIR:
        insertObject.append( dict( zip( columnNames , record ) ) )
    print(insertObject)
    
    return render_template('reportPreMixing.html',pdOrder=pdOrder,Phase_Parameter=insertObject,PreMixing=PreMixing,len=len(Phase_Parameter_DIR))

@app.route('/report/MainMixing/<string:pdOrder>')
def reportMainMixing(pdOrder):    
    server = "172.30.2.2"
    port = 5432
    database = "OEE_DB"
    username = "sa"
    password = "p@ssw0rd"
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+ server +';DATABASE='+database+';UID='+username+';PWD='+password)
    MainMixing = cnxn.cursor()
    MainMixing.execute("SELECT RecordID, PD_ORDER, PhaseID, Status, Start_time, End_Time, SetPoint1, Actual1, SetPoint2, Actual2, SetPoint3, Actual3, SetPoint4, Actual4, SetPoint5, Actual5, SetPoint6, Actual6, SetPoint7, Actual7, SetPoint8, Actual8, User_Mixing ,DATEDIFF(second,Start_time,End_Time) as Time_Sec  FROM SCADA_DB.dbo.Mixing_Report mr  WHERE PhaseID > 1 AND PhaseID < 100 AND PD_ORDER = '" +pdOrder+ "' ORDER BY Start_time ASC")
    
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+ server +';DATABASE='+database+';UID='+username+';PWD='+password)
    Phase_Parameter = cnxn.cursor()
    Phase_Parameter.execute("SELECT PhaseID ,PhaseName,Parameter1,Parameter2,Parameter3,Parameter4,Parameter5,Parameter6,Parameter7,Parameter8 FROM SCADA_DB.dbo.Phase_Parameter") 
    
    Phase_Parameter_DIR = Phase_Parameter.fetchall()

    insertObject = []
    columnNames = [column[0] for column in Phase_Parameter.description]
    for record in Phase_Parameter_DIR:
        insertObject.append( dict( zip( columnNames , record ) ) )
    print(insertObject)
    
    return render_template('reportMainMixing.html',pdOrder=pdOrder,Phase_Parameter=insertObject,MainMixing=MainMixing,len=len(Phase_Parameter_DIR))


@app.route('/report/MixingStorage/<string:pdOrder>')
def reportMixingStorage(pdOrder):
    server = "172.30.2.2"
    port = 5432
    database = "OEE_DB"
    username = "sa"
    password = "p@ssw0rd"
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+ server +';DATABASE='+database+';UID='+username+';PWD='+password)
    MixingStorage = cnxn.cursor()
    MixingStorage.execute("SELECT RecordID, PD_ORDER, PhaseID, Status, Start_time, End_Time, SetPoint1, Actual1, SetPoint2, Actual2, SetPoint3, Actual3, SetPoint4, Actual4, SetPoint5, Actual5, SetPoint6, Actual6, SetPoint7, Actual7, SetPoint8, Actual8, User_Mixing ,DATEDIFF(second,Start_time,End_Time) as Time_Sec  FROM SCADA_DB.dbo.Mixing_Report mr  WHERE PhaseID > 200 AND PhaseID < 300 AND PD_ORDER = '" +pdOrder+ "' ORDER BY Start_time ASC")
    
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+ server +';DATABASE='+database+';UID='+username+';PWD='+password)
    Phase_Parameter = cnxn.cursor()
    Phase_Parameter.execute("SELECT PhaseID ,PhaseName,Parameter1,Parameter2,Parameter3,Parameter4,Parameter5,Parameter6,Parameter7,Parameter8 FROM SCADA_DB.dbo.Phase_Parameter") 
    
    Phase_Parameter_DIR = Phase_Parameter.fetchall()

    insertObject = []
    columnNames = [column[0] for column in Phase_Parameter.description]
    for record in Phase_Parameter_DIR:
        insertObject.append( dict( zip( columnNames , record ) ) )
    print(insertObject)
    
    return render_template('reportMixingStorage.html',pdOrder=pdOrder,Phase_Parameter=insertObject,MixingStorage=MixingStorage,len=len(Phase_Parameter_DIR))
 
@app.route('/report/SidePOT_1/<string:pdOrder>')
def reportSidePOT_1(pdOrder):    
    server = "172.30.2.2"
    port = 5432
    database = "OEE_DB"
    username = "sa"
    password = "p@ssw0rd"
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+ server +';DATABASE='+database+';UID='+username+';PWD='+password)
    SidePOT_1 = cnxn.cursor()
    SidePOT_1.execute("SELECT RecordID, PD_ORDER, PhaseID, Status, Start_time, End_Time, SetPoint1, Actual1, SetPoint2, Actual2, SetPoint3, Actual3, SetPoint4, Actual4, SetPoint5, Actual5, SetPoint6, Actual6, SetPoint7, Actual7, SetPoint8, Actual8, User_Mixing ,DATEDIFF(second,Start_time,End_Time) as Time_Sec  FROM SCADA_DB.dbo.Mixing_Report mr  WHERE PhaseID > 300 AND PhaseID < 400 AND PD_ORDER = '" +pdOrder+ "' ORDER BY Start_time ASC")
    
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+ server +';DATABASE='+database+';UID='+username+';PWD='+password)
    Phase_Parameter = cnxn.cursor()
    Phase_Parameter.execute("SELECT PhaseID ,PhaseName,Parameter1,Parameter2,Parameter3,Parameter4,Parameter5,Parameter6,Parameter7,Parameter8 FROM SCADA_DB.dbo.Phase_Parameter") 
    
    Phase_Parameter_DIR = Phase_Parameter.fetchall()

    insertObject = []
    columnNames = [column[0] for column in Phase_Parameter.description]
    for record in Phase_Parameter_DIR:
        insertObject.append( dict( zip( columnNames , record ) ) )
    print(insertObject)
    
    return render_template('reportSidePOT_1.html',pdOrder=pdOrder,Phase_Parameter=insertObject,SidePOT_1=SidePOT_1,len=len(Phase_Parameter_DIR))

@app.route('/report/SidePOT_2/<string:pdOrder>')
def reportSidePOT_2(pdOrder):    
    server = "172.30.2.2"
    port = 5432
    database = "OEE_DB"
    username = "sa"
    password = "p@ssw0rd"
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+ server +';DATABASE='+database+';UID='+username+';PWD='+password)
    SidePOT_2 = cnxn.cursor()
    SidePOT_2.execute("SELECT RecordID, PD_ORDER, PhaseID, Status, Start_time, End_Time, SetPoint1, Actual1, SetPoint2, Actual2, SetPoint3, Actual3, SetPoint4, Actual4, SetPoint5, Actual5, SetPoint6, Actual6, SetPoint7, Actual7, SetPoint8, Actual8, User_Mixing ,DATEDIFF(second,Start_time,End_Time) as Time_Sec  FROM SCADA_DB.dbo.Mixing_Report mr  WHERE PhaseID > 400 AND PhaseID < 500 AND PD_ORDER = '" +pdOrder+ "' ORDER BY Start_time ASC")
    
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+ server +';DATABASE='+database+';UID='+username+';PWD='+password)
    Phase_Parameter = cnxn.cursor()
    Phase_Parameter.execute("SELECT PhaseID ,PhaseName,Parameter1,Parameter2,Parameter3,Parameter4,Parameter5,Parameter6,Parameter7,Parameter8 FROM SCADA_DB.dbo.Phase_Parameter") 
    
    Phase_Parameter_DIR = Phase_Parameter.fetchall()

    insertObject = []
    columnNames = [column[0] for column in Phase_Parameter.description]
    for record in Phase_Parameter_DIR:
        insertObject.append( dict( zip( columnNames , record ) ) )
    print(insertObject)
    
    return render_template('reportSidePOT_2.html',pdOrder=pdOrder,Phase_Parameter=insertObject,SidePOT_2=SidePOT_2,len=len(Phase_Parameter_DIR))

@app.route('/report/QC/<string:pdOrder>')
def reportQC(pdOrder):    
    server = "172.30.2.2"
    database = "OEE_DB"
    username = "sa"
    password = "p@ssw0rd"
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+ server +';DATABASE='+database+';UID='+username+';PWD='+password)
    PD_QC = cnxn.cursor()
    PD_QC.execute("SELECT * FROM SCADA_DB.dbo.QC_Process WHERE PD_Order = ? ORDER BY [DateTime] ASC ",(pdOrder,))
    
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+ server +';DATABASE='+database+';UID='+username+';PWD='+password)
    PD_QC2 = cnxn.cursor()
    PD_QC2.execute("SELECT * FROM SCADA_DB.dbo.QC_Process WHERE PD_Order = ? ORDER BY [DateTime] ASC ",(pdOrder,))
    
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+ server +';DATABASE='+database+';UID='+username+';PWD='+password)
    PD_QC3 = cnxn.cursor()
    PD_QC3.execute("SELECT * FROM SCADA_DB.dbo.QC_Process WHERE PD_Order = ? ORDER BY [DateTime] ASC ",(pdOrder,))
    dataPD = []
    dataPD_len = 0
    for i in PD_QC3:
       
        dataPD.append(i[9])
    dataPD_len = len(dataPD) - 1
    return render_template('reportQC.html',pdOrder=pdOrder,PD_QC = PD_QC,PD_QC2=PD_QC2,dataPD = dataPD,dataPD_len=dataPD_len)


@app.route('/batch_report_API' ,methods=["GET", "POST"])
def batch_report_API():
    global count
    q = request.args.get('q')
    
    print(q)

    if request.method == "POST":
        count+=1
        return redirect(url_for('ReportOEE'))
    else:
        server = "172.30.2.2"
        port = 5432
        database = "OEE_DB"
        username = "sa"
        password = "p@ssw0rd"
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+ server +';DATABASE='+database+';UID='+username+';PWD='+password)
        batch_report = cnxn.cursor()
        batch_report.execute("SELECT PD_Order,Plan_Datetime ,Target_Quantity,Unit, FM_Code,[Batch_No.],Plan_Datetime,Preweight_Datetime,Mixing_Datetime,QC_Datetime,Finished,Status FROM SCADA_DB.dbo.Batch_Report")
        
    
        payload = []
        content = {}
        for result in batch_report:
            content = {'PD': result[0], 'PD_PLAN_DT': str(result[1])[0:10], 'PD_TARGET_QTY': result[2],'PD_UNIT': result[3],'PD_FM_CODE': result[4],'PD_BATCHNO': result[5],'PD_PROC_P_ST': str(result[6]),'PD_PROC_O_ST': str(result[7]),'PD_PROC_M_ST': str(result[8]),'PD_PROC_Q_ED': str(result[9]),'PD_PROC_S_DT': str(result[10]),'PD_STATUS_CODE': str(result[11])}
            payload.append(content)
            content = {}
        #print(payload)
        return json.dumps({"data":payload}, cls = Encoder), 201
         
@app.route('/QC_report')
def QC_report():    
    return render_template('QC_report.html') 


@app.route('/Report_QC_Excel')
def Report_QC_Excel():
  
    df = pd.read_json('http://192.168.1.145:5001//QC_report_Excel_API')
    print(df)
    df.to_excel('QC_report.xlsx',index=False)
    
    time.sleep(1)
    
    wabu = openpyxl.load_workbook('QC_report.xlsx')
    washi = wabu.active
    washi.insert_rows(1,5)
    washi['A1'] = 'QC Report'
    washi['A1'].alignment = Alignment(vertical='center')
    washi['A1'].alignment = Alignment(horizontal='center')
    washi['A1'].font = Font(color='FFFFFF',
                        size=24,bold=True)
    washi['A1'].fill = PatternFill(patternType='solid',fgColor='154360')
    
    washi.merge_cells('A1:F1')
    washi.column_dimensions['A'].width = 20
    washi.column_dimensions['B'].width = 20
    washi.column_dimensions['C'].width = 20
    washi.column_dimensions['D'].width = 20
    washi.column_dimensions['E'].width = 20
    washi.column_dimensions['F'].width = 20
    washi.column_dimensions['G'].width = 20
    washi.column_dimensions['H'].width = 20
    
   
    wabu.save('QC_report.xlsx')
    
    return send_file('..\QC_report.xlsx') 

#ss0000

@app.route('/QC_report_Excel_API' ,methods=["GET", "POST"])
def QC_report_Excel_API():

    
    server = "172.30.2.2"
    port = 5432
    database = "OEE_DB"
    username = "sa"
    password = "p@ssw0rd"
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+ server +';DATABASE='+database+';UID='+username+';PWD='+password)
    PD_QC = cnxn.cursor()
    PD_QC.execute("SELECT DISTINCT PD_Order FROM SCADA_DB.dbo.QC_Process")
    payload = []
    for i in  PD_QC:
        print(i[0])
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+ server +';DATABASE='+database+';UID='+username+';PWD='+password)
        qc_report = cnxn.cursor()
        qc_report.execute("""
                          SELECT Product_Name  , PD_Order , [Lot_No.] ,BAY ,[Tank_S/N] 
                            , ROW_NUMBER() OVER(ORDER BY DateTime) AS RowNum
                            FROM SCADA_DB.dbo.QC_Process
                            WHERE PD_Order = ? AND [Action] = 'QC_RECEIVE' ORDER BY [DateTime] ASC  
                          """,(i[0],))
        
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+ server +';DATABASE='+database+';UID='+username+';PWD='+password)
        qc_reportStart = cnxn.cursor()
        qc_reportStart.execute("""
                          SELECT [DateTime]  AS StartTime , [User]  
                          FROM SCADA_DB.dbo.QC_Process 
                          WHERE [Action] = 'QC_RECEIVE' AND PD_Order = ? ORDER BY [DateTime] ASC  
                          """,(i[0],))
        
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+ server +';DATABASE='+database+';UID='+username+';PWD='+password)
        qc_reportStop = cnxn.cursor()
        qc_reportStop.execute("""
                          SELECT [DateTime]  AS StopTime , [User] 
                          FROM SCADA_DB.dbo.QC_Process 
                          WHERE ([Action] = 'QC_PASS' OR [Action] = 'QC_REJECT' or [Action] = 'QC_HOLD') 
                          AND PD_Order = ? ORDER BY [DateTime] ASC  

                          """,(i[0],))

        
        content = {}
        for result,dataDateStart,dataDateStop in zip(qc_report,qc_reportStart,qc_reportStop):
            content = {'Product_Name': str(result[0]), 'PD_Order': result[1],'Lot_No': result[2],'BAY': result[3],'Tank_SN': result[4],'NO': str(result[5]),'QC_START': str(dataDateStart[0])[0:19],'QC_FINISH': str(dataDateStop[0])[0:19],'QC_TIME': (dataDateStop[0] - dataDateStart[0]).total_seconds() // 60,'UserStart': str(dataDateStart[1])+ " / " +str(dataDateStop[1])}
            payload.append(content)
            content = {}
            
    return json.dumps(payload, cls = Encoder), 201

@app.route('/QC_report_API',methods=["GET", "POST"])
def QC_report_API():    
 
    server = "172.30.2.2"
    port = 5432
    database = "OEE_DB"
    username = "sa"
    password = "p@ssw0rd"
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+ server +';DATABASE='+database+';UID='+username+';PWD='+password)
    PD_QC = cnxn.cursor()
    PD_QC.execute("SELECT DISTINCT PD_Order FROM SCADA_DB.dbo.QC_Process")
    payload = []
    for i in  PD_QC:
        print(i[0])
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+ server +';DATABASE='+database+';UID='+username+';PWD='+password)
        qc_report = cnxn.cursor()
        qc_report.execute("""
                          SELECT Product_Name  , PD_Order , [Lot_No.] ,BAY ,[Tank_S/N] 
                            , ROW_NUMBER() OVER(ORDER BY DateTime) AS RowNum
                            FROM SCADA_DB.dbo.QC_Process
                            WHERE PD_Order = ? AND [Action] = 'QC_RECEIVE' ORDER BY [DateTime] ASC  
                          """,(i[0],))
        
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+ server +';DATABASE='+database+';UID='+username+';PWD='+password)
        qc_reportStart = cnxn.cursor()
        qc_reportStart.execute("""
                          SELECT [DateTime]  AS StartTime , [User]  
                          FROM SCADA_DB.dbo.QC_Process 
                          WHERE [Action] = 'QC_RECEIVE' AND PD_Order = ? ORDER BY [DateTime] ASC  
                          """,(i[0],))
        
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+ server +';DATABASE='+database+';UID='+username+';PWD='+password)
        qc_reportStop = cnxn.cursor()
        qc_reportStop.execute("""
                          SELECT [DateTime]  AS StopTime , [User] 
                          FROM SCADA_DB.dbo.QC_Process 
                          WHERE ([Action] = 'QC_PASS' OR [Action] = 'QC_REJECT' or [Action] = 'QC_HOLD') 
                          AND PD_Order = ? ORDER BY [DateTime] ASC  

                          """,(i[0],))

        
        content = {}
        for result,dataDateStart,dataDateStop in zip(qc_report,qc_reportStart,qc_reportStop):
            content = {'Product_Name': str(result[0]), 'PD_Order': result[1],'Lot_No': result[2],'BAY': result[3],'Tank_SN': result[4],'NO': str(result[5]),'QC_START': str(dataDateStart[0])[0:19],'QC_FINISH': str(dataDateStop[0])[0:19],'QC_TIME': (dataDateStop[0] - dataDateStart[0]).total_seconds() // 60,'UserStart': str(dataDateStart[1])+ " / " + str(dataDateStop[1])}
            payload.append(content)
            content = {}
    #print(payload)
    return json.dumps({"data":payload}, cls = Encoder), 201

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True ,port=5001)