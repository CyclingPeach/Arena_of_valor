import 导库

'''
    获取一个英雄的所有信息
    Param:{
        url_one          一个英雄的网页链接
        one_hero_info    一个英雄的信息
    }
'''

def get_hero_info(one_hero_soup):      
    '''
        英雄属性
    '''
    ## 英雄姓名
    # https://zhidao.baidu.com/question/717441355191056045.html
    name = one_hero_soup.select('body > div.wrapper > div.zk-con1.zk-con > div > div > div.cover > h2')[0]
    name = 导库.lxml.etree.HTML(str(name)).xpath("//h2/text()")[0]
    one_hero_name = {'英雄名':name}

    ## 英雄 属性及属性值
    shuxing_name  = []     # 属性名
    shuxing_value = []    # 属性值
    for i in one_hero_soup.select('body > div.wrapper > div.zk-con1.zk-con > div > div > div.cover > ul > li > em'):  
        shuxing_name.append(导库.lxml.etree.HTML(str(i)).xpath("//em/text()")[0])
    for j in one_hero_soup.select('body > div.wrapper > div.zk-con1.zk-con > div > div > div.cover > ul > li > span > i'):
        shuxing_value.append(j.get('style')[-3:])
    jineng = dict(zip(shuxing_name, shuxing_value))    # 将英雄属性名 和 属性值 合成在一个字典中
    
    ## 将所英雄信息 集在列表中
    one_hero_info = [one_hero_name,jineng]
    return one_hero_info


################################################################################################################################
################################################################################################################################
################################################################################################################################
    

    
'''
    技能介绍
'''
def get_skills_info(one_hreo_soup):
    i = 0
    j = 1
    skill_info = {}
    skill_select_str = 'body > div.wrapper > div.zkcontent > div > div.zk-con3.zk-con > div.skill.ls.fl > div > div > div > p'

    while j <= 7:    # 暂时只设置 4 个技能，第五个技能暂时不知道这么写
        skill_name_lable    = one_hero_soup.select(skill_select_str)[i].select('b')   [0]
        skill_energy_lable  = one_hero_soup.select(skill_select_str)[i].select('span')[0]
        skill_consume_lable = one_hero_soup.select(skill_select_str)[i].select('span')[1]
        skill_desc_lable    = one_hero_soup.select(skill_select_str)[j]

        skill_name    = 导库.lxml.etree.HTML(str(skill_name_lable)).   xpath("//text()")[0]
        skill_energy  = 导库.lxml.etree.HTML(str(skill_energy_lable)). xpath("//text()")[0]
        skill_consume = 导库.lxml.etree.HTML(str(skill_consume_lable)).xpath("//text()")[0]
        skill_desc    = 导库.lxml.etree.HTML(str(skill_desc_lable)).   xpath("//text()")[0]

        skill_info[skill_name] = [{'冷却值':int(skill_energy[4:])}, {'消耗':int(skill_consume[3:])}, {'技能描述':skill_desc}]

        i += 2
        j += 2

    return skill_info
    
    
'''
    铭文搭配建议
'''


################################################################################################################################
################################################################################################################################
################################################################################################################################


'''
    技能加点建议
'''
def get_skill_plus_sugg(cont_xph):
    
    get_skill_plus_sugg_head_xpath = '/html/body/div[3]/div[2]/div/div[2]/div[1]/div[@class="sugg-info2 info"]/'
    get_skill_plus_sugg_name  = cont_xph.xpath(get_skill_plus_sugg_head_xpath + 'p[@class="sugg-name"]')
    get_skill_plus_sugg_name3 = cont_xph.xpath(get_skill_plus_sugg_head_xpath + 'p[@class="sugg-name sugg-name3"]')
    items = {}
    items[get_skill_plus_sugg_name [0].xpath("./b/text()")[0]] = get_skill_plus_sugg_name [0].xpath("./span/text()")[0]
    items[get_skill_plus_sugg_name [1].xpath("./b/text()")[0]] = get_skill_plus_sugg_name [1].xpath("./span/text()")[0]
    items[get_skill_plus_sugg_name3[0].xpath("./b/text()")[0]] = get_skill_plus_sugg_name3[0].xpath("./span/text()")[0]

    return items    


################################################################################################################################
################################################################################################################################
################################################################################################################################


'''
    出装建议
    
    参数说明:
        cont_xph    表示 lxml.etree.HTML(content)
        这里和 ‘技能加点建议’ 模块共用 : cont_xph
    
'''
def get_equip_sugg(cont_xph):

    get_equip_sugg = {}
    
    for i in range(1,3):
        header_xpath  = '/html/body/div[3]/div[2]/div/div[2]/div[2]/div[2]/div[' + str(i) + ']/ul/li/a/div'
        tips_xpath    = '/html/body/div[3]/div[2]/div/div[2]/div[2]/div[2]/div[' + str(i) + ']/p'

        JNAME_xpath   = header_xpath + '/div[1]/div/h4'    # 装备名
        Jprice_xpath  = header_xpath + '/div[1]/div/p[1]'  # 出售价
        Jtprice_xpath = header_xpath + '/div[1]/div/p[2]'  # 总价
        Jdesc_xpath   = header_xpath + '/div[2]'           # 描述

        JNAME   = cont_xph.xpath(JNAME_xpath  )
        Jprice  = cont_xph.xpath(Jprice_xpath )
        Jtprice = cont_xph.xpath(Jtprice_xpath)
        Jdesc   = cont_xph.xpath(Jdesc_xpath  )
        Jtips   = cont_xph.xpath(tips_xpath   )

        Jname_lists = []
        Jdesc_lists = []    
        J = list(zip(JNAME, tuple(zip(Jprice, Jtprice, Jdesc))))
        for m,n in J:
            Jdesc_list = n[0].xpath('.//text()') + n[1].xpath('.//text()') + n[2].xpath('.//text()')
            Jname_lists.append(m.xpath('.//text()')[0])
            Jdesc_lists.append(Jdesc_list)
        equip_sugg_desc_dict = dict(zip(Jname_lists, Jdesc_lists))

        Jtip = Jtips[0].xpath('.//text()')
        # print(str(Jtip))    # 这里的 输出还有‘ [] ’这两个中括号，后面有时间再看看是哪里出的问题
        if i == 1:
            get_equip_sugg['推荐出装 一 '] = [{'装备':Jname_lists}, {'小贴士':str(Jtip)[7:-2]}]
        if i == 2:
            get_equip_sugg['推荐出装 二 '] = [{'装备':Jname_lists}, {'小贴士':str(Jtip)[7:-2]}]
    return get_equip_sugg


################################################################################################################################
################################################################################################################################
################################################################################################################################


'''
英雄关系
    参数说明：
        one_hreo_soup:每一位英雄bs4解析的 html

        这里和 ‘技能介绍共用 one_hreo_soup’
'''
def get_relates_list(one_hreo_soup):
    
    relates_list = {}
    herolist_url_herd = 'https://pvp.qq.com/web201605/'

    for i in range(1, 4):
        relate = one_hreo_soup.select('body > div.wrapper > div.zkcontent > div > div.zk-con4.zk-con > div.hero.ls.fl > div.hero-info-box > div > div:nth-child(' + str(i) + ') > div.hero-f1.fl')[0].get_text()

        names = []
        href_url_lables = one_hreo_soup.select('body > div.wrapper > div.zkcontent > div > div.zk-con4.zk-con > div.hero.ls.fl > div.hero-info-box > div > div:nth-child(' + str(i) + ') > div.hero-list.hero-relate-list.fl > ul > li > a')

        for item in href_url_lables:
            href = herolist_url_herd + item.get('href')
            href_response = 导库.requests.get(href)
            href_response.encoding = href_response.apparent_encoding
            href_soup = 导库.BeautifulSoup(href_response.text)    
            name = href_soup.select('body > div.wrapper > div.zk-con1.zk-con > div > div > div.cover > h2')[0].get_text()
            names.append(name)
        names
        first   = {names[0]:one_hreo_soup.select('body > div.wrapper > div.zkcontent > div > div.zk-con4.zk-con > div.hero.ls.fl > div.hero-info-box > div > div:nth-child(' + str(i) + ') > div.hero-list-desc > p')[0].get_text()}
        second  = {names[1]:one_hreo_soup.select('body > div.wrapper > div.zkcontent > div > div.zk-con4.zk-con > div.hero.ls.fl > div.hero-info-box > div > div:nth-child(' + str(i) + ') > div.hero-list-desc > p')[1].get_text()}

        relates_list[relate] = [first,second]

    return relates_list