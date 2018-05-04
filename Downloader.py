from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Downloader:
     def  __init__(self):
          self.options = webdriver.ChromeOptions()
          self.options.add_argument('headless')
          self.options.add_argument('window')
          self.options.add_argument('disable-gpu')

          self.browser = webdriver.Chrome('./chromedriver.exe', chrome_options=self.options)
          self.browser.get('https://www.google.co.kr')
          self.browser.implicitly_wait(3)

          self.path = str

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
          pass

     def SetPath(self, path):
          pass

down = Downloader()
down.GetSearchPage('감사')

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