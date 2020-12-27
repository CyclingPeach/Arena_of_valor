import 导库

url = 'https://pvp.qq.com/web201605/herolist.shtml'
response = 导库.requests.get(url)
response.encoding = response.apparent_encoding  # 获取网页真实编码'GB2312'  https://www.cnblogs.com/bw13/p/6549248.html
html = response.text
soup = 导库.BeautifulSoup(html)

data = soup.select(
    'body > div.wrapper > div.zkcontent > div.zk-con-box > div.herolist-box > div.herolist-content > ul.herolist.clearfix > li > a')
data2 = soup.select(
    'body > div.wrapper > div.zkcontent > div.zk-con-box > div.herolist-box > div.herolist-content > ul.herolist.clearfix > li > a > img')


# 获取每个英雄的链接
def get_herolist_urls():
    herolist_urls = []
    herolist_names = []
    herolist_url_herd = 'https://pvp.qq.com/web201605/'

    for item in data:
        href = herolist_url_herd + item.get('href')
        herolist_urls.append(href)
    for item in data2:
        alt = item.get('alt')
        herolist_names.append(alt)

    herolist_dict = dict(zip(herolist_names, herolist_urls))

    # print('链接数量:',len(herolist_urls),'| 英雄数量:',len(herolist_names), ' | 总计:', len(herolist_dict))
    return herolist_dict