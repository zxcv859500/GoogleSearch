from Downloader import *

class Download_Manager():

    def __init__(self, path, keyword):
        self.page = Downloader()
        self.page.Setting(path)
        self.page.GetSearchPage(keyword)
        self.page.Page_Surf()

        self.Error_Count = 0
        self.idx = 1

    def download(self):

        if self.idx >= 11:

            self.idx = 1
            self.page.Refresh()
            if self.page.Page_Surf() == False:
                print("End of page")
                return True
            print('Next page')
            self.page.Click_NextBtn()
            self.page.Page_Surf()

        print('Downloading {}'.format(self.idx))
        if self.page.Download(self.idx) == False:
            self.page.Refresh()

            if self.Error_Count >= 5:
                print('Error Occur')
                self.Error_Count += 1
                return False

        self.idx += 1

if __name__ == '__main__':
    manage = Download_Manager('C:\\Users\\조나단\\Desktop\\Test\\', '롤')

    while(1):
        flag = manage.download()
        if flag == True:
            manage.page.DriverQuit()
            break