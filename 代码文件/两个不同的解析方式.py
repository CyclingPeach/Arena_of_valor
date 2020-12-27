import 导库

one_hero_url = 'https://pvp.qq.com/web201605/herodetail/506.shtml'

def print_one_hero_soup(oen_hero_url):
    one_hero_response = 导库.requests.get(oen_hero_url)
    one_hero_response.encoding = one_hero_response.apparent_encoding    # 获取网页真实编码    https://www.cnblogs.com/bw13/p/6549248.html
    one_hero_html = one_hero_response.text
    one_hero_soup = 导库.BeautifulSoup(one_hero_html)
    
    return one_hero_soup

def print_one_hero_xpath(one_hero_url):
    
    # options.add_argument('lang=zh_CN.GBK')  # 设置 编码格式
    options = 导库.webdriver.ChromeOptions()
    options.headless = True
    driver = 导库.webdriver.Chrome(chrome_options = options)    # 控制chrome浏览器
    
    driver.get(one_hero_url)
    导库.time.sleep(2)
    content = driver.page_source
    cont_xph = 导库.lxml.etree.HTML(content)
    
    return cont_xph