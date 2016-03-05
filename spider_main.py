# 爬虫总入口程序

import url_manager, html_download, html_parser, html_output

class SpiderMain(object):

    def __init__(self):
        self.urls = url_manager.urlManager()
        self.download = html_download.htmlDownload()
        self.parser = html_parser.htmlParser()
        self.outputer = html_output.htmlOutput()

    def craw(self, root_url):
        self.urls.add_new_url(root_url)

        count = 1
        while self.urls.has_new_url():
            try: 
                new_url = self.urls.get_new_url()
                print('craw %d : %s' % (count, new_url))
                html_cont = self.download.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                if count == 1000:
                    break
                count = count + 1
            except: 
                print("craw fail")
        self.outputer.output_html()


if __name__ == '__main__':
    root_url = 'http://baike.baidu.com/view/21087.htm'
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
