from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from lxml import  etree
# from playsound import playsound

#http://jwglxt.qust.edu.cn/jwglxt/xtgl/index_initMenu.html?jsdm=&_t=1630504720322
#chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\selenum\AutomationProfile"

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver = "C:\Program Files\Google\Chrome\Application\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
# id_list = ['C113029800','C113033900','C113034100','C113034300','C113034400','C113034500','C113034700','C113033800','C113034200','C113034600','C113034000','C113017900','C113022500','C113026700','C113027100','C113027500','C113027600','C113027700','C113027900','C113029200','C113030700','C113031000','C113031900','C113032000','C113032100','C113032300','C113032400','C113032500','C113032600','C113032700','C113032800','C113032900','C113033000','C113033100','C113033200','C113033300','C113033400','C113033500','C113033600','C113033700','C113010700','C113012800','C113013300','C113014600','C113014700','C113014800','C113014900','C113015900','C113017300','C113021300','C113021500','C113030200','C113030300','C113030400','C113031500','C113031600','C113031700','C113031800','C113034900','C113035200','C113036500','C113034800','C113035300','C113035400','C113036300','C113036400','C113035000','C113035100','C113036700','C113036800','C113035500','C113035600','C113035800','C113035900','C113036000','C113036100','C113036200','C113035700','C113036600','C113036900']
# id_list = ['C212015600-2','C212016600','C222019600']
id_list = ['C212016600','C222019600']
while True:
    for id in id_list:
        try:
            driver.find_element_by_css_selector("[placeholder='可输入课程号/课程名称/教学班名称/教师姓名/教师工号查询!']").clear()
            driver.find_element_by_css_selector("[placeholder='可输入课程号/课程名称/教学班名称/教师姓名/教师工号查询!']").send_keys(id)
            driver.find_element_by_class_name('btn').click()
            sleep(0.8)
            page_text = driver.page_source
            tree = etree.HTML(page_text)
            detail1 = tree.xpath('//*[@class="jxbrs"]//text()')[0]  #分子
            detail2= tree.xpath('//*[@class="jxbrl"]//text()')[0]  #分母
            title = tree.xpath('//*[@class="an"]//text()')[0]
            flag = tree.xpath('//*[@class="jsxmzc"]/font//text()')[0]
            if int(detail1) >= int(detail2) :
                detail = "已满"
                print(detail, id,detail1+"/"+detail2,flag)
            else:
                detail = "未满"
                print(detail, id,detail1+"/"+detail2,flag)
                try:
                    if title == "选课":
                        if (flag=='卓越') | (flag=='尔雅'):
                            driver.find_element_by_class_name("an").click()
                            driver.find_element_by_id("btn_confirm").click()
                            driver.find_element_by_id("btn_ok").click()
                        else:
                            driver.find_element_by_class_name("an").click()
                            driver.find_element_by_id("btn_ok").click()
                        # playsound('nsrnsyt.mp3')

                except:
                    pass
                    # playsound('nsrnsyt.mp3')
                # driver.quit()
        except:

            pass



