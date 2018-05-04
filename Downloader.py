from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Downloader:
     def  __init__(self):
          self.path = "C:\\Users\\조나단\\Desktop\\Test\\"

          self.options = webdriver.ChromeOptions()

          profile = {"plugins.plugins_list": [{"enabled": False, "name": "Chrome PDF Viewer"}],
                    "download.default_directory": self.path, "download.extensions_to_open": "applications/pdf"}
          self.options.add_experimental_option("prefs", profile)

          #self.options.add_argument('headless')
          #self.options.add_argument('window')
          #self.options.add_argument('disable-gpu')
          '''
          prefs = {
               'profile.default_content_seetings.popups' : 0,
               'download.default_directroy' : 'C:\\Users\\조나단\\Desktop\\',
               'directory_upgrade' : True,
               'extensions_to_open' : ""
          }
          '''
          #self.options.add_experimental_option('prefs', prefs)

          self.browser = webdriver.Chrome('./chromedriver.exe', chrome_options=self.options)
          self.browser.get('http://www.google.co.kr')
          self.browser.implicitly_wait(3)


     def GetSearchPage(self, keyword):
          search_keyword = keyword + ' filetype:pdf'
          search_bar = self.browser.find_element_by_xpath('//*[@id="lst-ib"]')
          search_bar.send_keys(search_keyword)

          self.browser.implicitly_wait(3)
          #self.browser.get_screenshot_as_file('first_screenshot.png')

          #self.browser.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[3]/center/input[1]').click()
          search_bar.send_keys(Keys.ENTER)
          self.browser.implicitly_wait(3)

          self.browser.get_screenshot_as_file('screenshot.png')

     def Download(self):

          for idx in range(1, 11):
               self.browser.find_element_by_xpath('//*[@id="rso"]/div/div/div[{}]/div/div/h3/a'\
                                                  .format(idx)).click()
               time.sleep(1)

          self.browser.get_screenshot_as_file('screenshot.png')

     def SetPath(self, path):
          pass

down = Downloader()
down.GetSearchPage('블랙핑크')
down.Download()

'''
if __name__ == '__main__':
     options = webdriver.ChromeOptions()
     options.add_argument('headless')
     options.add_argument('window-size=1920x1080')
     options.add_argument('disable-gpu')

     browser = webdriver.Chrome('./chromedriver.exe', chrome_options=options)
     browser.get('http://www.ubuntu.com/')
     browser.implicitly_wait(3)
     browser.get_screenshot_as_file('naver_main_headless.png')
     
     browser.quit()
'''