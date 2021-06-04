# coding:utf-8
import time
import win32gui
import win32con
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random


def Vulbos_login():
    driver.get("https://account.tophant.com/login.html?response_type=code&client_id=11593ba06a82c21a&state=c23395f7e6b99c56702aa9fad01cda50")
    driver.find_element(By.XPATH,'//*[@id="username"]').send_keys("1470551773@qq.com")#输入账号
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("nty143832")#输入密码
    driver.find_element(By.XPATH,'//*[@id="loginBtn"]').click()
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="navbar"]/div/div[3]/div/button')))
    cookie_list = driver.get_cookies()
    return cookie_list

def Vulbox_input(cookie_list,list_data,num):
    for item in cookie_list:
        cookie = {
            'name': item['name'],
            'value': item['value'],
            "expires":None,
            'path': '/',
            'httpOnly': False,
            'HostOnly': False,
            'Secure': False,
        }
        driver.add_cookie(cookie)
    Vul_title = list_data[num]
    Vul_name = list_data[num+1]
    Vul_host = list_data[num+2]
    print(Vul_host)
    Vul_detail = list_data[num+3]
    Vul_url = list_data[num+4]
    Vul_image = list_data[num+5]
    driver.get("https://www.vulbox.com/user/submit-72")
    driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div[2]/div[1]/div/div[2]/form/div[2]/div/input").send_keys(Vul_title)
    driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div[2]/div[1]/div/div[2]/form/div[3]/div/div/div/div[2]/label").click()
    driver.find_element(By.XPATH,'//*[@id="bug_firm_name"]').send_keys(Vul_name)
    driver.find_element(By.XPATH, '//*[@id="bug_firm_url"]').send_keys(Vul_host)

    driver.find_element(By.XPATH,"/html/body/div[5]/div/div/div[2]/div[1]/div/div[2]/form/div[5]/div/div[1]/div").click()
    driver.find_element(By.XPATH,"/html/body/div[5]/div/div/div[2]/div[1]/div/div[2]/form/div[5]/div/div[2]/div/ul/li[1]/a").click()

    #driver.find_element(By.XPATH,"/html/body/div[5]/div/div/div[2]/div[1]/div/div[2]/form/div[6]/div/div/button/span[1]").click()
    driver.find_element(By.XPATH,"/html/body/div[5]/div/div/div[2]/div[1]/div/div[2]/form/div[5]/div/div[2]/div/ul/ul[2]/li[2]/a").click()

    driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div[2]/div[1]/div/div[2]/form/div[8]/div/textarea').send_keys('1.数据库信息泄露\n2.网页篡改：登陆后台后发布恶意内容\n3.网站挂马 : 当拿到webshell时或者获取到服务器的权限以后，可将一些网页木马挂在服务器上，去攻击别人\n4.私自添加系统账号\n5.读写文件获取webshell')


    driver.find_element(By.XPATH,'/html/body/div[5]/div/div/div[2]/div[1]/div/div[2]/form/div[9]/div/input').send_keys(Vul_url)

    driver.find_element(By.XPATH,'/html/body/div[5]/div/div/div[2]/div[1]/div/div[2]/form/div[5]/div/div[1]/div').click()
    driver.find_element(By.XPATH,'/html/body/div[5]/div/div/div[2]/div[1]/div/div[2]/form/div[5]/div/div[2]/div/ul/li[1]/a').click()
    driver.find_element(By.XPATH,'/html/body/div[5]/div/div/div[2]/div[1]/div/div[2]/form/div[5]/div/div[2]/div/ul/ul[2]/li[2]/a').click()

    driver.find_element(By.XPATH,'/html/body/div[5]/div/div/div[2]/div[1]/div/div[2]/form/div[6]/div/div/button').click()
    driver.find_element(By.XPATH,'/html/body/div[5]/div/div/div[2]/div[1]/div/div[2]/form/div[6]/div/div/div/ul/li[2]/a').click()

    driver.find_element(By.XPATH,'/html/body/div[5]/div/div/div[2]/div[1]/div/div[2]/form/div[10]/div/input').send_keys('goods_id')

    driver.find_element(By.XPATH,'/html/body/div[5]/div/div/div[2]/div[1]/div/div[2]/form/div[11]/div/textarea').send_keys('GET /index.php?s=api/goods_detail&goods_id=1%20and%20updatexml(1,concat(0x7e,database(),0x7e),1) HTTP/1.1'+'\n'+'Host: '+Vul_host+'\n'+'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0'+'\n'+'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'+'\n'+'Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2'+'\n'+'Accept-Encoding: gzip, deflate'+'\n'+'Upgrade-Insecure-Requests: 1'+'\n'+'Te: trailers'+'\n'+'Connection: close')

    driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div[2]/div[1]/div/div[2]/form/div[15]/div/div[2]/div[1]/div[4]/p').send_keys("漏洞链接："+Vul_url+'可以查到数据名')

    driver.find_element(By.XPATH,'/html/body/div[5]/div/div/div[2]/div[1]/div/div[2]/form/div[15]/div/div[2]/div[1]/div[1]/ul/li[13]/a').click()
    driver.find_element(By.XPATH,'/html/body/div[5]/div/div/div[2]/div[1]/div/div[2]/form/div[15]/div/div[2]/div[1]/div[1]/ul/li[13]/div/ul/li[1]/a').click()
    time.sleep(1)
    try:
        dialog = win32gui.FindWindow('#32770', u'打开')  # 对话框
        ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
        ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
        Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)  # 上面三句依次寻找对象，直到找到输入框Edit对象的句柄
        button = win32gui.FindWindowEx(dialog, 0, 'Button', None)  # 确定按钮Button
        win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, Vul_image)  # 往输入框输入绝对地址
        win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 按button
        time.sleep(1)
    except:
        win32gui.SendMessage(dialog, win32con.WM_COMMAND, 2, button)  # 按button
    #driver.find_element(By.XPATH,'/html/body/div[4]/div/div/div[2]/div[1]/div/div[2]/form/div[15]/div/div[2]/div[1]/div[4]').send_keys(Keys.ENTER)

    driver.find_element(By.XPATH,'/html/body/div[5]/div/div/div[2]/div[1]/div/div[2]/form/div[17]/div/div/div[1]/div[4]/p').send_keys("1.建议使用统一的规则库对用户的所有输入进行安全性验证，验证不通过的应直接拒绝；\n2.建议所有应用与数据库交互处均使用参数化查询，严禁将用户输入直接与SQL查询语句进行拼接；\n3.对进入数据库的特殊字符进行转义或编码转换；\n4.	严格限制变量类型，数据库中的存储字段必须对应为int型；\n5.数据长度应该严格限制，这能在一定程度上防御比较长的SQL注入语句；\n6.网站每个数据层的编码统一，建议全部使用UTF-8编码，上下层编码不一致有可能导致一些过滤模型被绕过；\n7.严格限制网站用户的数据库的操作权限，给此用户提供仅仅能够满足其工作的权限，从而最大限度的减少注入攻击对数据库的危害；\n8.避免网站显示SQL错误信息，比如类型错误、字段不匹配等，防止攻击者利用这些错误信息进行一些判断。")


    driver.find_element(By.XPATH,'/html/body/div[5]/div/div/div[2]/div[1]/div/div[2]/form/div[18]/div/div/div/span').click()
    driver.find_element(By.XPATH,'/html/body/div[5]/div/div/div[2]/div[1]/div/div[2]/form/div[18]/div/div/div/div/ul[1]/li[2]').click()
    driver.find_element(By.XPATH,'/html/body/div[5]/div/div/div[2]/div[1]/div/div[2]/form/div[18]/div/div/div/div/ul[2]/li').click()
    driver.find_element(By.XPATH,'/html/body/div[5]/div/div/div[2]/div[1]/div/div[2]/form/div[18]/div/div/div/div/ul[3]/li[1]').click()

    driver.find_element(By.XPATH,'/html/body/div[5]/div/div/div[2]/div[1]/div/div[2]/form/div[19]/div/div/div/input').click()
    driver.find_element(By.XPATH,'/html/body/div[5]/div/div/div[2]/div[1]/div/div[2]/form/div[19]/div/div/dl/dd[2]').click()

    driver.find_element(By.XPATH,'/html/body/div[5]/div/div/div[2]/div[1]/div/div[2]/form/div[20]/div/input[1]').click()

    driver.find_element(By.XPATH,'/html/body/div[5]/div/div/div[2]/div[1]/div/div[2]/form/div[21]/div/div/div').click()

    driver.find_element(By.XPATH,'/html/body/div[5]/div/div/div[2]/div[1]/div/div[2]/form/div[23]/div/input[1]').click()

    #driver.find_element(By.XPATH,'//*[@id="submit"]').click()
    #driver.find_element(By.XPATH,'/html/body/div[4]/div/div/div[2]/div[1]/div/div[2]/form/div[15]/div/div[2]/div[1]/div[1]/ul/li[13]/a/span').click()
    #driver.find_element(By.XPATH,'/html/body/div[4]/div/div/div[2]/div[1]/div/div[2]/form/div[15]/div/div[2]/div[1]/div[1]/ul/li[13]/div/ul/li[1]/a').click()

    #time.sleep(1)
    #dialog = win32gui.FindWindow('#32770', u'打开')  # 对话框
    #ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
    #ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
    #Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)  # 上面三句依次寻找对象，直到找到输入框Edit对象的句柄
    #button = win32gui.FindWindowEx(dialog, 0, 'Button', None)  # 确定按钮Button
    #win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, Vul_image)  # 往输入框输入绝对地址
    #win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 按button
    #time.sleep(10)
    #driver.find_element(By.XPATH,"/html/body/div[4]/div/div/div[2]/div[1]/div/div[2]/form/div[17]/div/div/div[1]/div[4]").click()
    #driver.find_element(By.XPATH,'/html/body/div[4]/div/div/div[2]/div[1]/div/div[2]/form/div[17]/div/div/div[1]/div[4]').send_keys("ApiController.class.php 参数过滤严谨")
    #driver.find_element(By.XPATH,'//*[@id="submit"]').click()
    #time.sleep(2)
    print("结束")
    random_time=random.randint(60,120)
    time.sleep(random_time)


def Vul_bak():
    print("信息")
    list = []
    with open("D:\\桌面\\学习\\安全\\SRC\\自动提交脚本\\sql_ip_vuln4.txt","r",encoding="gbk") as fp:#读取漏洞信息，需要修改路径
        for i in fp:
            list.append(i.strip("\n"))
        '''
        for t in range(0,6,6):
            Vul_title = list[t]
            Vul_name = list[t+1]
            Vul_host = list[t+2]
            Vul_detail = list[t+3]
            Vul_url = list[t+4]
            Vul_image = list[t+5]
        '''
    return list






if __name__ == '__main__':
    print("主函数")
    d = {"PHPSESSID": "86mva2mjktcuuhlgscf9s5iat0",
         "Key_auth": "64Jv20s9oYTIzjM8aDUe1FExYjESWXdwkin13cODaPs%3D",
         "VulBox_uid": "RmaKQt0Us91OC3B5XS1aBNgpc5sZf%2FK6lvOoQYhv8vGAuVesEwGMnPW8Pe4d5BKG",}
    driver_options = webdriver.ChromeOptions()
    driver_options.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
    driver = webdriver.Chrome(executable_path=r"D:\桌面\学习\安全\SRC\自动提交脚本\chromedriver.exe",options=driver_options)#谷歌浏览器驱动文件，需要修改路径
    cookie_list = Vulbos_login()
    list_data = Vul_bak()
    for i in range(1782,3000,6):#提交数量，每6个一组漏洞
        print(i)
        Vulbox_input(cookie_list,list_data,i)