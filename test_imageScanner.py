from selenium import webdriver
import requests
import pandas as pd
import yarl
import threading
import time
import logging
log = logging.getLogger(__name__)
count = 0
#Script to run>  pytest --html=solutions_report.html test_bloglinks.py

def urlchecker(listurls):
    report=[]
    i=0
   # while i < 10:
    for href in listurls:
        url = str(listurls[i])
        print(url)
        try:

            r= requests.get(url).status_code
            if(r==200):
                report.append(url + ': <b style="color:green" > GOOD :-) </b>')
                # print(url)
                # print(r)
            else:
                report.append(url + ': <b style="color:red">Not working & status code is: </b>'+str(r))
                # print(url)
                # print(r)

        except:
            report.append(threading.currentThread().getName() + ':' + url +': <b style="color:Yellow"> -- WARNING -- </b>')
            # print(url + "Exception")
        i=i+1

    for d in report:
        files.write(str(d))
        print(d)
        assert d
        files.write('\n')

    return report

def openpages(url,link,i):
    filename = url
    url = 'https://dev:dev@job-www2-1944.dev.swweb.app/' + url
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('--start-maximized')
    driver2 = webdriver.Chrome(options=options)
    driver2.implicitly_wait(10)
    driver2.get(url)
    driver2.set_window_size(1920, 1080)
    driver2.get_screenshot_as_file("/Users/chandra_vadla/PycharmProjects/automation/Demo/resourcesafterfix/"+filename+".png")
    #print(url)
    driver2.close()
    driver2.quit()
    print('exit'+str(i))


def test_loadData():
    print('hello')
    global report2
    global listOfPages
    global linktext
    global numberOfPages
    global files
    global driver2
    global report
    global files2
    report = []
    report.append('STARTED')
    data = pd.read_excel(r'/Users/chandra_vadla/PycharmProjects/automation/imagesnew.xlsx')
    #data = pd.read_excel(r'/Users/chandra_vadla/PycharmProjects/automation/datasheet.xlsx')
    df = pd.DataFrame(data, columns=['Pages'])
    listOfPages = df['Pages'].to_list()
    #print(listOfPages)
    print("Input Data loaded: SUCCESS")
    files = open('/Users/chandra_vadla/PycharmProjects/automation/Demo/hello123.txt', 'a+')
    files.write("STARTED HERE \r\n")
    files2 = open('/Users/chandra_vadla/PycharmProjects/automation/Demo/hello456.txt', 'a+')
    files2.write("STARTED HERE \r\n")
   # print(listOfPages)
    # i=0
    # for pages in listOfPages:
    #     sai = threading.Thread(target=openpages, args=(pages, listOfPages[i],i))
    #     sai.start()
    #     sai.join()
    #     i += 1
    urlchecker(listOfPages)

    print(report)



