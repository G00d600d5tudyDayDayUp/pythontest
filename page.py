# coding=UTF-8
# Author: LXY <1015372900@qq.com>
# Data: 2019-8-4

"""
simple test
"""

from urllib import urlopen
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('UTF-8')


def get_page(url):
    response = urlopen(url)
    html = response.read()
    return html


def stand(html):
    soup = BeautifulSoup(html, "html.parser")
    text1 = soup.find("table", border="1").tbody.find_all("td", width="163")
    res = []
    for i in text1:
        res.append(i.get_text())
    return res


if __name__ == "__main__":
    Url = "http://xxgk.hnu.edu.cn/info/1102/4458.htm"
    Html = get_page(Url)
    result = stand(Html)
    for i in result:
        if i == "专业名称":
            continue
        print i

