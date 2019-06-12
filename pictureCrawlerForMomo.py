import io
import sys   
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') 
from selenium import webdriver
import requests
import base64
import connectBigquery as big
import time

class imgobj():
    def __init__(self,title,gid,picLink,cat,itemLink):
        self.title = title
        self.gid = gid
        self.picLink = picLink
        self.cat = cat
        self.itemLink =itemLink
        self.img = requests.get(self.picLink).content
        self.base64String = str(base64.b64encode(self.img))
        self.base64String = self.base64String[2:len(self.base64String)-1]


chrome_options = webdriver.ChromeOptions()
driver = webdriver.Remote(command_executor='http://192.168.2.1:4444/wd/hub',
                              desired_capabilities = chrome_options.to_capabilities())
driver.get('https://www.momoshop.com.tw/category/DgrpCategory.jsp?d_code=1306600009&p_orderType=4&showType=chessboardType')
page=1
while (page<11):
    print("now: ",str(page))
    page+=1
    items = driver.find_elements_by_class_name("eachGood")

    for i in items:
    
        gid = i.get_attribute("gcode")
        src = i.find_element_by_tag_name('img').get_attribute('src')
        link = "https://www.momoshop.com.tw/goods/GoodsDetail.jsp?i_code="+str(gid)
        title = i.find_element_by_class_name('prdName').text
        picObj=imgobj(title,gid,src,"Top",link)
    
        with open("./pics/pic-"+str(gid)+".jpg", 'wb') as f:
            f.write(picObj.img)
        big.momoInsert(picObj.gid,picObj.picLink,picObj.title,picObj.base64String,picObj.cat,picObj.itemLink)
    nextBtn = driver.find_element_by_xpath("//a[@pageidx='"+str(page)+"']")
    nextBtn.click()
    time.sleep(0)
driver.quit()

