from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *
import time

class Downloader:

     def __init__(self):

          self.Current_Page = str
          self.Error_Count = 0

     #Setting(경로) : 크롬 기본 옵션 설정, 다운로드 경로 설정
     def Setting(self, path):
          self.options = webdriver.ChromeOptions()
          self.path = path
          profile = {"plugins.plugins_list": [{"enabled": False, "name": "Chrome PDF Viewer"}],
                     "download.default_directory": path, "download.extensions_to_oepn": "applications/pdf",
                     'download.prompt_for_download': False,
                     'download.directory_upgrade' : True,
                     'safebrowsing.enabled' : False,
                     'safebrowsing.disable_download_protection': True}

          self.options.add_experimental_option("prefs", profile)

          self.options.add_argument('--no-sandbox')
          self.options.add_argument('--headless')
          self.options.add_argument('--window-size=1920x1080')
          self.options.add_argument('--disable-gpu')

     #GetSearchPage(검색어) : 검색 결과 첫 페이지로 이동
     def GetSearchPage(self, keyword):
          self.browser = webdriver.Chrome('./chromedriver.exe', chrome_options=self.options)
          self.browser.command_executor._commands["send_command"] = ("POST",
                                                                     '/session/$sessionId/chromium/send_command')
          self.browser.desired_capabilities['browserName'] = 'ur mum'
          params = {'cmd': 'Page.setDownloadBehavior', 'params' : {'behavior': 'allow', 'downloadPath' : self.path}}
          self.browser.execute("send_command", params)
          self.browser.get('http://www.google.co.kr')
          self.browser.implicitly_wait(3)

          search_keyword = keyword + ' filetype:pdf'
          search_bar = self.browser.find_element_by_xpath('//*[@id="lst-ib"]')
          search_bar.send_keys(search_keyword)

          self.browser.implicitly_wait(3)
          search_bar.send_keys(Keys.ENTER)
          self.browser.implicitly_wait(3)

     def Click_NextBtn(self):

          self.next_btn.click()

     #Donwload() : 해당 페이지의 idx 번째 pdf 다운로드
     def Download(self, idx):

          try:
               self.browser.find_element_by_xpath('//*[@id="rso"]/div/div/div[{}]/div/div/h3/a'\
                                                       .format(idx)).click()
               time.sleep(0.5)
          except NoSuchElementException:
               print('Index numbder({}): No such element'.format(idx))
               return False
          return True

     #현재 검색 페이지의 다음 버튼을 얻고 Current_Page에 현재 링크 주소 저장
     def Page_Surf(self):

          self.Current_Page = self.browser.current_url
          try:
               self.next_btn = self.browser.find_element_by_xpath('//*[@id="pnnext"]')
          except NoSuchElementException:
               print('NextBtn does not exist')
               return False
          return True

     def Refresh(self):

          self.browser.get(self.Current_Page)
          self.browser.implicitly_wait(3)

     def DriverQuit(self):

          self.browser.quit()

if __name__ == '__main__':
     down = Downloader()
     down.Setting('C:\\Users\\조나단\\Desktop\\Test\\')
     down.GetSearchPage('롤')
     down.Download()