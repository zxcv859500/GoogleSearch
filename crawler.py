from selenium import webdriver
from pyvirtualdisplay import Display

if __name__ == '__main__':
     display = Display(visible=0, size=(1024, 768))
     display.start()

     browser = webdriver.Chrome()
     browser.get('http://www.ubuntu.com/')
     print(browser.page_source)

     browser.close()
     display.stop()
