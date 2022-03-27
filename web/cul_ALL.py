import culOEE as step1
import cul_OEE_M as step3
import culOEE_Total as step2
import culOEE_dashboard as step4
import schedule
import time

def start():
    step1.startOEE()
    step1.startOEE()
    step1.startYield()
    step1.startYield()
    step2.startOEE()
    step3.goStart()
    step4.goStart()
    
schedule.every().day.at("1:00").do(start) 

while True:
    schedule.run_pending() # รันตารางเวลา
    time.sleep(1)