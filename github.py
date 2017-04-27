# -*- coding: utf-8 -*-
from grab.spider import Spider, Task


class GithubSpider(Spider):
    start_url = 'http://localhost:8000/showcases.html'

    def task_generator(self):
        yield Task('start', url=self.start_url)

    def task_start(self, grab, task):
        explore_grid_hrefs = grab.doc(
            '//a[contains(@class, "exploregrid-item")]').attr_list('href')
        for href in explore_grid_hrefs:
            url = grab.make_url_absolute(href)
            print(url)

if __name__ == '__main__':
    bot = GithubSpider()
    bot.run()
