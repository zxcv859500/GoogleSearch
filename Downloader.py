from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Downloader:

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

     #Donwload() : 페이지 안의 모든 검색 결과를 다운 한 후 다음 검색결과 페이지로 넘어감
     def Download(self):

          while(1):
               link = self.browser.current_url
               Error_cnt = 0

               idx = 1
               while(1):
                    if idx == 11:
                         break

                    if Error_cnt >= 11:
                         return False
                    try:
                         self.browser.find_element_by_xpath('//*[@id="rso"]/div/div/div[{}]/div/div/h3/a'\
                                                       .format(idx)).click()
                    except:
                         self.browser.get(link)
                         self.browser.implicitly_wait(3)
                         Error_cnt += 1
                         idx -= 1

                    idx += 1

                    time.sleep(2)

               self.browser.get(link)
               self.browser.implicitly_wait(3)
               try:
                    next_btn = self.browser.find_element_by_xpath('//*[@id="pnnext"]')
               except:
                    print('Cannot find next button')
                    return False

               next_btn.click()


if __name__ == '__main__':
     down = Downloader()
     down.Setting('C:\\Users\\조나단\\Desktop\\Test\\')
     down.GetSearchPage('롤')
     down.Download()