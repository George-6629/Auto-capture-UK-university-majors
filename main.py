from selenium import webdriver
from bs4 import BeautifulSoup
import time
import requests
import csv
import json

driver = webdriver.Chrome(r"D:\ChromeDriver\chromedriver.exe")

'''
Aberdeen University spider
'''
def Aberdeen_University():
    server = 'https://www.findaphd.com/'
    target_under = 'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/?limit=All'
    target_post = 'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/?limit=All'
    target_phd = 'https://www.findaphd.com/phds/aberdeen-university/?40w000'
    shape_under = 'table'
    shape_post = 'table'
    label_under = 'a'
    label_post = 'a'
    label_class = ''
    classes_under = 'prospectus_results_table'
    classes_post = 'prospectus_results_table'
    university_name = 'University of Aberdeen'
    html_under = HTMLRequest(target_under)
    course_under = HTMLParserNormal(html_under, shape_under, classes_under, label_under, label_class)
    html_post = HTMLRequest(target_post)
    course_post = HTMLParserNormal(html_post, shape_post, classes_post, label_post, label_class)
    try:
        course_PhD, course_PhDD = get_contents_findaphd(target_phd, server)
    except:
        course_PhD = []
        course_PhDD = []
        print("被findaphd锁域名，稍后再试", university_name)
    DataOutput(course_under, course_post, course_PhD, course_PhDD, university_name)


'''
Aberdeen University spider
'''


def Aberystwyth_University():
    server = 'https://courses.aber.ac.uk/atoz/#'
    shape = 'div'
    classes = 'content-primary-main'
    label = 'a'
    label_class = 'course'
    university_name = 'Aberystwyth University'
    next_url = []
    next_ul = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    for each in next_ul:
        next_url.append(server + each)
    for each in next_url:
        html = HTMLRequest(each)
        course_under, course_post, course_PhD, course_PhDD = HTMLParserClassified(html, shape, classes, label,label_class)
    DataOutput(course_under, course_post, course_PhD, course_PhDD, university_name)


'''
Aston University
'''


def Aston_University():
    target = 'https://www.aston.ac.uk/courses-atoz'
    shape = 'div'
    classes = 'view-content'
    label = 'div'
    label_class = 'title'
    university_name = 'Aston University'
    html = HTMLRequest(target)
    course_under, course_post, course_PhD, course_PhDD = HTMLParserClassified(html, shape, classes, label, label_class)
    DataOutput(course_under, course_post, course_PhD, course_PhDD, university_name)

'''Birkbeck, University of London'''
def Birkbeck():
    target_under = 'https://search.bbk.ac.uk/search/courses/?q=&level=UGProgramme&year=2021%2F2022&start_rank='
    target_post = 'https://search.bbk.ac.uk/search/courses/?q=&level=PGProgramme&year=2021%2F2022&start_rank='
    target_phd = 'https://search.bbk.ac.uk/search/courses/?q=&level=PHDProgramme&year=2021%2F2022&start_rank='
    shape_under = 'ol'
    shape_post = 'ol'
    shape_phd = 'ol'
    classes_under = 'menu vertical menu--listing menu--listing--purple v-space-3'
    classes_post = 'menu vertical menu--listing menu--listing--purple v-space-3'
    classes_phd = 'menu vertical menu--listing menu--listing--purple v-space-3'
    label = 'div'
    label_class = 'column medium-6 large-8'
    university_name = 'Birkbeck,University of London'
    next_url_under = []
    next_url_post = []
    next_url_phd = []
    num_under=336
    num_post=278
    num_phd=34
    course_under = []
    course_post = []
    course_PhD = []
    course_PhDD = []
    for i in range(1, num_under, 20):
        next_url_under.append(target_under + str(i))
    for i in range(1, num_post, 20):
        next_url_post.append(target_post + str(i))
    for i in range(1, num_phd, 20):
        next_url_phd.append(target_phd + str(i))
    for each in next_url_under:
        html = HTMLRequest(each)
        a_course_under = HTMLParserNormal(html,shape_under,classes_under,label,label_class)
        course_under.extend(a_course_under)
    for each in next_url_post:
        html = HTMLRequest(each)
        a_course_post = HTMLParserNormal(html,shape_post,classes_post,label,label_class)
        course_post.extend(a_course_post)
    for each in next_url_phd:
        html = HTMLRequest(each)
        a_course_PhD = HTMLParserNormal(html,shape_phd,classes_phd,label,label_class)
        course_PhD.extend(a_course_PhD)
    DataOutput(course_under, course_post, course_PhD, course_PhDD, university_name)

'''Brunel University'''
def Brunel_University():
    target_under = 'https://www.brunel.ac.uk/study/Course-listing?courseLevel=0%2f2%2f24%2f28%2f43&page='
    target_post = 'https://www.brunel.ac.uk/study/Course-listing?courseLevel=0%2f2%2f24%2f28%2f44&page='
    target_phd = 'https://www.brunel.ac.uk/study/Course-listing?courseLevel=0%2f2%2f24%2f28%2f872&page='
    shape_under = 'table'
    shape_post = 'table'
    shape_phd = 'table'
    classes_under = 'large-only resultsTable'
    classes_post = 'large-only resultsTable'
    classes_phd = 'large-only resultsTable'
    label = 'a'
    label_class = ''
    university_name = 'Brunel University'
    next_url_under = []
    next_url_post = []
    next_url_phd = []
    num_under = 12
    num_post = 11
    num_phd = 7
    course_under = []
    course_post = []
    course_PhD = []
    course_PhDD = []
    for i in range(num_under):
        next_url_under.append(target_under + str(i+1))
    for i in range(num_post):
        next_url_post.append(target_post + str(i+1))
    for i in range(num_phd):
        next_url_phd.append(target_phd + str(i+1))
    for each in next_url_under:
        html = HTMLRequest(each)
        a_course_under = HTMLParserNormal(html, shape_under, classes_under, label, label_class)
        course_under.extend(a_course_under)
    for each in next_url_post:
        html = HTMLRequest(each)
        a_course_post = HTMLParserNormal(html, shape_post, classes_post, label, label_class)
        course_post.extend(a_course_post)
    for each in next_url_phd:
        html = HTMLRequest(each)
        a_course_PhD = HTMLParserNormal(html, shape_phd, classes_phd, label, label_class)
        course_PhD.extend(a_course_PhD)
    DataOutput(course_under, course_post, course_PhD, course_PhDD, university_name)

'''Cardiff University'''
def Cardiff():
    target_under = 'https://www.cardiff.ac.uk/study/undergraduate/courses/a-to-z'
    target_post = 'https://www.cardiff.ac.uk/study/postgraduate/taught/courses'
    target_phd = 'https://www.cardiff.ac.uk/study/postgraduate/research/programmes/a-to-z'
    shape_under = 'table'
    shape_post = 'div'
    shape_phd = 'table'
    classes_under = 'table'
    classes_post = 'search-results'
    classes_phd = 'table'
    label = 'a'
    label_class = ''
    university_name = 'Cardiff University'
    html_under = HTMLRequest(target_under)
    html_post = HTMLRequest(target_post)
    html_phd = HTMLRequest(target_phd)
    course_under = HTMLParserNormal2(html_under,shape_under,classes_under,label,label_class)
    course_post = HTMLParserNormal(html_post,shape_post,classes_post,label,label_class)
    course_PhD = HTMLParserNormal2(html_phd,shape_phd,classes_phd,label,label_class)
    course_PhDD = []
    DataOutput(course_under, course_post, course_PhD, course_PhDD, university_name)

'''City, University of London'''
def City_London():
    target = 'https://www.city.ac.uk/prospective-students/courses?start_rank='
    shape = 'div'
    classes = 'finder__results'
    label = 'h3'
    label_class = 'card__heading'
    university_name = 'City,University of London'
    course_under = []
    course_post = []
    course_PhD = []
    course_PhDD = []
    num_page = 638
    next_url = []
    for i in range(1, num_page, 10):
        if i != 381:
            next_url.append(target + str(i))
    for each in next_url:
        html = HTMLSelenium(each)
        a_course_under, a_course_post, a_course_phd, a_course_phdd = HTMLParserClassified(html, shape, classes, label, label_class)
        course_under.extend(a_course_under)
        course_post.extend(a_course_post)
        course_PhD.extend(a_course_phd)
        course_PhDD.extend(a_course_phdd)
    DataOutput(course_under, course_post, course_PhD, course_PhDD, university_name)


'''Durham University'''
def Durham():
    target ='https://www.dur.ac.uk/courses/all/#indexA'
    shape = 'tr'
    university_name = 'Durham University'
    a_course_under = []
    a_course_post = []
    req = requests.get(url=target)
    req.encoding = 'GBK'
    req.encoding = 'utf-8'
    htm = req.text
    bf = BeautifulSoup(htm)
    texts1 = bf.find_all(shape, class_='BSc Undergraduate 2021 FT')
    texts2 = bf.find_all(shape, class_='BA Undergraduate 2021 FT')
    texts3 = bf.find_all(shape, class_='BEng Undergraduate 2021 FT')
    texts4 = bf.find_all(shape, class_='LLB Undergraduate 2021 FT')
    for each in texts1:
        a_course_under.append(each.text.replace('\n', ' ').split('             ')[-1])
    for each in texts2:
        a_course_under.append(each.text.replace('\n', ' ').split('             ')[-1])
    for each in texts3:
        a_course_under.append(each.text.replace('\n', ' ').split('             ')[-1])
    for each in texts4:
        a_course_under.append(each.text.replace('\n', ' ').split('             ')[-1])
    texts5 = bf.find_all(shape, class_='LLM PostgraduateTaught 2021 FT')
    texts6 = bf.find_all(shape, class_='MA PostgraduateTaught 2021 PTFT')
    texts7 = bf.find_all(shape, class_='MSc PostgraduateTaught 2021 FT')
    texts8 = bf.find_all(shape, class_='MBA PostgraduateTaught 2021 PT')
    texts9 = bf.find_all(shape, class_='MBiol PostgraduateTaught 2021 PTFT')
    texts10 = bf.find_all(shape, class_='MChem PostgraduateTaught 2021 PTFT')
    texts11 = bf.find_all(shape, class_='MDS PostgraduateTaught 2021 PTFT')
    texts12 = bf.find_all(shape, class_='MEng PostgraduateTaught 2021 PTFT')
    texts13 = bf.find_all(shape, class_='MESM PostgraduateTaught 2021 PTFT')
    texts14 = bf.find_all(shape, class_='MMath PostgraduateTaught 2021 PTFT')
    texts15 = bf.find_all(shape, class_='MPhys PostgraduateTaught 2021 PTFT')
    texts16 = bf.find_all(shape, class_='MSci PostgraduateTaught 2021 PTFT')
    texts17 = bf.find_all(shape, class_='MSW PostgraduateTaught 2021 PTFT')
    for each in texts5:
        a_course_post.append(each.text.replace('\n', ' ').split('             ')[-1])
    for each in texts6:
        a_course_post.append(each.text.replace('\n', ' ').split('             ')[-1])
    for each in texts7:
        a_course_post.append(each.text.replace('\n', ' ').split('             ')[-1])
    for each in texts8:
        a_course_post.append(each.text.replace('\n', ' ').split('             ')[-1])
    for each in texts9:
        a_course_post.append(each.text.replace('\n', ' ').split('             ')[-1])
    for each in texts10:
        a_course_post.append(each.text.replace('\n', ' ').split('             ')[-1])
    for each in texts11:
        a_course_post.append(each.text.replace('\n', ' ').split('             ')[-1])
    for each in texts12:
        a_course_post.append(each.text.replace('\n', ' ').split('             ')[-1])
    for each in texts13:
        a_course_post.append(each.text.replace('\n', ' ').split('             ')[-1])
    for each in texts14:
        a_course_post.append(each.text.replace('\n', ' ').split('             ')[-1])
    for each in texts15:
        a_course_post.append(each.text.replace('\n', ' ').split('             ')[-1])
    for each in texts16:
        a_course_post.append(each.text.replace('\n', ' ').split('             ')[-1])
    for each in texts17:
        a_course_post.append(each.text.replace('\n', ' ').split('             ')[-1])
    print(a_course_under)
    print(a_course_post)

    target_phd ='https://www.findaphd.com/phds/durham-university/?40Mg00'
    server = 'https://www.findaphd.com/'
    try:
        course_PhD, course_PhDD = get_contents_findaphd(target_phd, server)
    except:
        course_PhD = []
        course_PhDD = []
        print("被findaphd锁域名，稍后再试", university_name)
    DataOutput(a_course_under, a_course_post, course_PhD, course_PhDD, university_name)

'''Goldsmiths, University of London'''
def Goldsmiths():
    target_under = 'https://www.gold.ac.uk/ug/a-z/'
    target_post = 'https://www.gold.ac.uk/pg/a-z/'
    shape_under = 'div'
    shape_post = 'div'
    classes_under = 'content'
    classes_post = 'content'
    university_name = 'Goldsmiths, University of London'
    course_under = []
    a_post = []
    a_PhD = []
    a_PhDD = []
    req = requests.get(url=target_under)
    req.encoding = 'GBK'
    req.encoding = 'utf-8'
    htm = req.text
    bf = BeautifulSoup(htm)
    texts = bf.find_all(shape_under, class_=classes_under)
    a_bf = BeautifulSoup(str(texts[1]))
    a = a_bf.find_all('h3', class_='teaser__title')
    for each in a:
        if each.text not in course_under:
            course_under.append(each.text)

    req = requests.get(url=target_post)
    req.encoding = 'GBK'
    req.encoding = 'utf-8'
    htm = req.text
    bf = BeautifulSoup(htm)
    texts = bf.find_all(shape_post, class_=classes_post)
    a_bf = BeautifulSoup(str(texts[1]))
    a = a_bf.find_all('h3', class_='teaser__title')
    for i in range(len(a)):
        if a[i].text.strip().replace('\t', '').replace('\n', '') not in a_post:
            if 'MSc' in str(a[i].text):
                a_post.append(a[i].text.strip().replace('\t', '').replace('\n', ''))
            elif 'MSci' in str(a[i].text):
                a_post.append(a[i].text.strip().replace('\t', '').replace('\n', ''))
            elif 'MBA' in str(a[i].text):
                a_post.append(a[i].text.strip().replace('\t', '').replace('\n', ''))
            elif 'MEng' in str(a[i].text):
                a_post.append(a[i].text.strip().replace('\t', '').replace('\n', ''))
            elif 'MPhil' in str(a[i].text):
                a_post.append(a[i].text.strip().replace('\t', '').replace('\n', ''))
            elif 'PgCert' in str(a[i].text):
                a_post.append(a[i].text.strip().replace('\t', '').replace('\n', ''))
            elif 'PgDip' in str(a[i].text):
                a_post.append(a[i].text.strip().replace('\t', '').replace('\n', ''))
            elif 'MA' in str(a[i].text):
                a_post.append(a[i].text.strip().replace('\t', '').replace('\n', ''))
            elif 'MRes' in str(a[i].text):
                a_post.append(a[i].text.strip().replace('\t', '').replace('\n', ''))
            elif 'GradCert' in str(a[i].text):
                a_post.append(a[i].text.strip().replace('\t', '').replace('\n', ''))
            elif 'PGCE' in str(a[i].text):
                a_post.append(a[i].text.strip().replace('\t', '').replace('\n', ''))
            elif 'MEd' in str(a[i].text):
                a_post.append(a[i].text.strip().replace('\t', '').replace('\n', ''))
            elif 'LLM' in str(a[i].text):
                a_post.append(a[i].text.strip().replace('\t', '').replace('\n', ''))
            elif 'MPH' in str(a[i].text):
                a_post.append(a[i].text.strip().replace('\t', '').replace('\n', ''))
            elif 'Research' in str(a[i].text):
                a_post.append(a[i].text.strip().replace('\t', '').replace('\n', ''))
        if a[i].text.strip().replace('\t', '').replace('\n', '') not in a_PhD:
            if 'PhD' in str(a[i].text):
                a_PhD.append(a[i].text.strip().replace('\t', '').replace('\n', ''))
            elif 'DClinPsych' in str(a[i].text):
                a_PhD.append(a[i].text.strip().replace('\t', '').replace('\n', ''))
            elif 'DST' in str(a[i].text):
                a_PhD.append(a[i].text.strip().replace('\t', '').replace('\n', ''))
            elif 'Doctorate' in str(a[i].text):
                a_PhD.append(a[i].text.strip().replace('\t', '').replace('\n', ''))
            elif 'PHD' in str(a[i].text):
                a_PhD.append(a[i].text.strip().replace('\t', '').replace('\n', ''))
    DataOutput(course_under, a_post, a_PhD, a_PhDD, university_name)

'''Heriot-Watt University'''
def Heriot_Watt():
    target = 'https://search.hw.ac.uk/s/search.html?collection=uk-courses&facetScope=&query=&num_ranks=309'
    shape = 'table'
    classes = 'hw_course-search__courses'
    label = 'a'
    label_class = ''
    university_name = 'Heriot-Watt University'
    html = HTMLRequest(target)
    course_under, course_post, course_PhD, course_PhDD = HTMLParserClassified(html, shape, classes, label, label_class)
    DataOutput(course_under, course_post, course_PhD, course_PhDD, university_name)

'''Imperial College London'''
def Imperial():
    server = 'https://www.findaphd.com/'
    target_under = 'https://www.imperial.ac.uk/study/ug/courses/'
    target_post = 'https://www.imperial.ac.uk/study/pg/courses/'
    target_phd = 'https://www.findaphd.com/phds/imperial-college-london/?400s00'
    shape_under = 'ol'
    shape_post = 'ol'
    classes_under = 'index-groups courses primary'
    classes_post = 'index-groups courses primary'
    label = 'h4'
    label_class = 'title'
    university_name = 'Imperial College London'
    html = HTMLRequest(target_under)
    course_under = HTMLParserNormal(html, shape_under, classes_under, label, label_class)
    html = HTMLRequest(target_post)
    course_post = HTMLParserNormal(html, shape_post, classes_post, label, label_class)
    try:
        course_PhD, course_PhDD = get_contents_findaphd(target_phd, server)
    except:
        course_PhD = []
        course_PhDD = []
        print("被findaphd锁域名，稍后再试", university_name)
    DataOutput(course_under, course_post, course_PhD, course_PhDD, university_name)

'''Kings College London'''
def Kings():
    server = 'https://www.kcl.ac.uk/search/courses'
    university_name = 'Kings College London'
    a_under = []
    a_post = []
    a_PhD = []
    a_PhDD = []
    # 找到所有需要遍历的页面，存储到next_url中
    next_url = [server]
    for i in range(23):
        next_url.append(server + '?coursesPage=' + str(i + 1))
    print(next_url)
    for i in range(len(next_url) - 1):
        html = HTMLRequest(next_url[i])
        bf = BeautifulSoup(html)
        texts = bf.find_all('div', class_='Cardstyled__CardStyled-sc-147a7mv-0 fyoFZN')
        for x in range(len(texts)):
            con_bf = BeautifulSoup(str(texts[x]))
            h3 = con_bf.find_all('h3', class_='Headingstyled__DynamicHeading-sc-1544wc-0 dYlryA')
            art = con_bf.find_all('article')
            if h3[0].text.strip().replace('\t', '').replace('\n', '') not in a_under:
                if 'Undergraduate' in art[0].text:
                    a_under.append(h3[0].text.strip().replace('\t', '').replace('\n', ''))
            if h3[0].text.strip().replace('\t', '').replace('\n', '') not in a_post:
                if 'MSc' in str(art[0].text):
                    a_post.append(h3[0].text.strip().replace('\t', '').replace('\n', ''))
                elif 'MSci' in str(art[0].text):
                    a_post.append(h3[0].text.strip().replace('\t', '').replace('\n', ''))
                elif 'MBA' in str(art[0].text):
                    a_post.append(h3[0].text.strip().replace('\t', '').replace('\n', ''))
                elif 'MEng' in str(art[0].text):
                    a_post.append(h3[0].text.strip().replace('\t', '').replace('\n', ''))
                elif 'MPhil' in str(art[0].text):
                    a_post.append(h3[0].text.strip().replace('\t', '').replace('\n', ''))
                elif 'PgCert' in str(art[0].text):
                    a_post.append(h3[0].text.strip().replace('\t', '').replace('\n', ''))
                elif 'PgDip' in str(art[0].text):
                    a_post.append(h3[0].text.strip().replace('\t', '').replace('\n', ''))
                elif 'MA' in str(art[0].text):
                    a_post.append(h3[0].text.strip().replace('\t', '').replace('\n', ''))
                elif 'MRes' in str(art[0].text):
                    a_post.append(h3[0].text.strip().replace('\t', '').replace('\n', ''))
                elif 'GradCert' in str(art[0].text):
                    a_post.append(h3[0].text.strip().replace('\t', '').replace('\n', ''))
                elif 'PGCE' in str(art[0].textt):
                    a_post.append(h3[0].text.strip().replace('\t', '').replace('\n', ''))
                elif 'MEd' in str(art[0].text):
                    a_post.append(h3[0].text.strip().replace('\t', '').replace('\n', ''))
                elif 'LLM' in str(art[0].text):
                    a_post.append(h3[0].text.strip().replace('\t', '').replace('\n', ''))
                elif 'MPH' in str(art[0].text):
                    a_post.append(h3[0].text.strip().replace('\t', '').replace('\n', ''))
                elif 'Research' in str(art[0].text):
                    a_post.append(h3[0].text.strip().replace('\t', '').replace('\n', ''))
            if h3[0].text.strip().replace('\t', '').replace('\n', '') not in a_PhD:
                if 'PhD' in str(art[0].text):
                    a_PhD.append(h3[0].text.strip().replace('\t', '').replace('\n', ''))
                elif 'DClinPsych' in str(art[0].text):
                    a_PhD.append(h3[0].text.strip().replace('\t', '').replace('\n', ''))
                elif 'DST' in str(art[0].text):
                    a_PhD.append(h3[0].text.strip().replace('\t', '').replace('\n', ''))
                elif 'Doctorate' in str(art[0].text):
                    a_PhD.append(h3[0].text.strip().replace('\t', '').replace('\n', ''))
                elif 'PHD' in str(art[0].text):
                    a_PhD.append(h3[0].text.strip().replace('\t', '').replace('\n', ''))
    DataOutput(a_under, a_post, a_PhD, a_PhDD, university_name)

'''Lancaster University'''
def Lancaster():
    target_under = 'https://www.lancaster.ac.uk/study/undergraduate/courses/?entryYear=previous'
    target_post = 'https://www.lancaster.ac.uk/study/postgraduate/postgraduate-courses/'
    university_name = 'Lancaster University'
    shape_under = 'nav'
    shape_post = 'nav'
    classes_under = 'a-z'
    classes_post = 'a-z'
    label = 'a'
    label_class = ''
    course_under = []
    html = HTMLRequest(target_under)
    a_under = HTMLParserNormal(html, shape_under, classes_under, label, label_class)
    for i in range(16,len(a_under)):
        course_under.append(a_under[i])
    html = HTMLRequest(target_post)
    a_under, course_post, course_PhD, course_PhDD = HTMLParserClassified(html, shape_post, classes_post, label, label_class)
    DataOutput(course_under, course_post, course_PhD, course_PhDD, university_name)

'''Loughborough University'''
def Loughborough():
    target_under = 'https://www.lboro.ac.uk/study/undergraduate/courses/a-z/'
    target_post = 'https://www.lboro.ac.uk/study/postgraduate/masters-degrees/a-z/'
    target_phd = 'https://www.lboro.ac.uk/study/postgraduate/research-degrees/phd-opportunities/'
    shape_under = 'ul'
    shape_post = 'ul'
    classes_under = 'list list--courses js-courses-list'
    classes_post = 'list list--degrees js-degrees-list'
    university_name = 'Loughborough University'
    label = 'span'
    label_class = 'list__heading-title'
    course_PhD = []
    course_PhDD = []
    html = HTMLRequest(target_under)
    course_under = HTMLParserNormal(html,shape_under,classes_under,label,label_class)
    html = HTMLRequest(target_post)
    course_post = HTMLParserNormal(html,shape_post,classes_post,label,label_class)
    req = requests.get(url=target_phd)
    req.encoding = 'GBK'
    req.encoding = 'utf-8'
    htm = req.text
    bf = BeautifulSoup(htm)
    texts = bf.find_all(shape_post, class_=classes_post)
    a_bf = BeautifulSoup(str(texts[0]))
    a = a_bf.find_all('span', class_='list__heading-title')
    d = a_bf.find_all('p', class_='list__content list__content--department')
    for i in range(len(a)):
        if a[i].text.strip().replace('\r', ' ') not in course_PhD:
            course_PhD.append(a[i].text.strip().replace('\r', ' '))
            course_PhDD.append(d[i].text.replace('\r', ' ').replace('\n', ' ').split(':')[-1].strip())
    DataOutput(course_under, course_post, course_PhD, course_PhDD, university_name)

'''Newcastle University'''
def Newcastle():
    university_name = 'Newcastle University'
    target_under = 'https://www.ncl.ac.uk/undergraduate/degrees/'
    target_post = 'https://www.ncl.ac.uk/postgraduate/courses/#a-z'
    shape_under = 'ul'
    shape_post = 'div'
    classes_under = 'courseSearchResults__courseList'
    classes_post = 'azcontainer contentSeparator tab containAsides tabtp'
    label = 'a'
    label_class = ''
    try:
        driver = webdriver.Chrome(r"D:\ChromeDriver\chromedriver.exe")
        driver.get(target_under)
        driver.find_element_by_partial_link_text("A-Z of courses").click()
        time.sleep(1)
        data = driver.page_source
        course_under = HTMLParserNormal(data, shape_under, classes_under, label, label_class)
        driver.get(target_post)
        driver.find_element_by_partial_link_text("A-Z").click()
        time.sleep(1)
        html = driver.page_source
        a_course, course_post, course_PhD, course_PhDD = HTMLParserClassified(html, shape_post, classes_post, label,label_class)
        driver.close()
    except:
        course_under = []
        course_post =[]
        course_PhD = []
        course_PhDD = []
    DataOutput(course_under, course_post, course_PhD, course_PhDD, university_name)


'''Oxford Brookes University'''
def Oxford_Brookes():
    university_name = 'Oxford Brookes University'
    target_under = 'https://search.brookes.ac.uk/s/search.html?collection=oxford-brookes-course-finder&profile=_default&query=&f.Study+level%7CcourseLevel=undergraduate&start_rank='
    target_post = 'https://search.brookes.ac.uk/s/search.html?collection=oxford-brookes-course-finder&profile=_default&query=&f.Study+level%7CcourseLevel=postgraduate&start_rank='
    amount_under = 190
    amount_post = 139
    shape_under = 'ol'
    shape_post = 'ol'
    classes_under = 'list-unstyled course-list'
    classes_post = 'list-unstyled course-list'

    next_url = []
    for i in range(1, amount_under, 10):
        next_url.append(target_under + str(i + 1))
    print(next_url)
    course_under = []
    for i in range(len(next_url)):
        req = requests.get(url=next_url[i])
        req.encoding = 'GBK'
        req.encoding = 'utf-8'
        htm = req.text
        bf = BeautifulSoup(htm)
        texts = bf.find_all(shape_under, class_=classes_under)
        a_bf = BeautifulSoup(str(texts[0]))
        a = a_bf.find_all('h3', class_='')
        for x in range(0, len(a), 2):
            course_under.append(a[x].text.replace('\n', '').strip().replace('                                             ',
                                                                        '').replace('       ', '').split('\xa0')[0])
    next_url = []
    for i in range(1, amount_post, 10):
        next_url.append(target_post + str(i + 1))
    print(next_url)
    a_post = []
    a_PhD = []
    a_PhDD = []
    for i in range(len(next_url)):
        req = requests.get(url=next_url[i])
        req.encoding = 'GBK'
        req.encoding = 'utf-8'
        htm = req.text
        bf = BeautifulSoup(htm)
        texts = bf.find_all(shape_post, class_=classes_post)
        a_bf = BeautifulSoup(str(texts[0]))
        a = a_bf.find_all('h3', class_='')
        for x in range(0, len(a), 2):
            if 'PhD' in str(a[x].text):
                a_PhD.append(
                    a[x].text.replace('\n', '').strip().replace('                                             ',
                                                                '').replace('       ', '').split('\xa0')[0])
                if 'MSc' in str(a[x].text):
                    a_post.append(
                        a[x].text.replace('\n', '').strip().replace('                                             ',
                                                                    '').replace('       ', '').split('\xa0')[0])
                elif 'MPhil' in str(a[x].text):
                    a_post.append(
                        a[x].text.replace('\n', '').strip().replace('                                             ',
                                                                    '').replace('       ', '').split('\xa0')[0])
                elif 'Master' in str(a[x].text):
                    a_post.append(
                        a[x].text.replace('\n', '').strip().replace('                                             ',
                                                                    '').replace('       ', '').split('\xa0')[0])
                elif 'MRes' in str(a[x].text):
                    a_post.append(
                        a[x].text.replace('\n', '').strip().replace('                                             ',
                                                                    '').replace('       ', '').split('\xa0')[0])
                elif 'MBA' in str(a[x].text):
                    a_post.append(
                        a[x].text.replace('\n', '').strip().replace('                                             ',
                                                                    '').replace('       ', '').split('\xa0')[0])
            else:
                a_post.append(
                    a[x].text.replace('\n', '').strip().replace('                                             ',
                                                                '').replace('       ', '').split('\xa0')[0])
    DataOutput(course_under, a_post, a_PhD, a_PhDD, university_name)

'''Queen Mary, University of London'''
def Queen_Mary():
    university_name = 'Queen Mary, University of London'
    server = 'https://www.findaphd.com/'
    target_under='https://search.qmul.ac.uk/s/search.html?meta_yearentry_sand=2020&collection=queenmary-coursefinder-undergraduate-meta&form=simple&start_rank='
    target_post='https://search.qmul.ac.uk/s/search.html?collection=queenmary-coursefinder-pg&query=&sort=title&start_rank='
    target_phd='https://www.findaphd.com/phds/queen-mary-university-of-london/?40wM00'
    shape_under = 'div'
    shape_post = 'div'
    classes_under = 'slat__container'
    classes_post = 'slat__container'
    label_under = 'h2'
    label_post = 'h4'
    label_class = 'course-card__title'
    course_under=[]
    course_post =[]
    next_url_under = []
    for i in range(1, 140, 10):
        next_url_under.append(target_under + str(i))
    for each in next_url_under:
        html = HTMLRequest(each)
        a_under = HTMLParserNormal2(html,shape_under,classes_under,label_under,label_class)
        course_under.extend(a_under)
    next_url_post = []
    for i in range(1, 300, 10):
        next_url_post.append(target_post + str(i))
    for each in next_url_post:
        html = HTMLRequest(each)
        a_post =HTMLParserNormal2(html,shape_post,classes_post,label_post,label_class)
        course_post.extend(a_post)
    try:
        course_PhD, course_PhDD = get_contents_findaphd(target_phd,server)
    except:
        course_PhD = []
        course_PhDD = []
        print("被findaphd锁域名，稍后再试", university_name)
    DataOutput(course_under, course_post, course_PhD, course_PhDD, university_name)

'''Queens University Belfast'''
def Queens_Belfast():
    university_name = 'Queens University Belfast'
    target='https://www.qub.ac.uk/courses/'
    shape = 'table'
    classes = 'js-datatable'
    label = 'a'
    label_class = ''
    html = HTMLRequest(target)
    course_under, course_post, course_PhD, course_PhDD = HTMLParserClassified(html,shape,classes,label,label_class)
    DataOutput(course_under, course_post, course_PhD, course_PhDD, university_name)


'''Royal Holloway, University of London'''
def Royal_Holloway():
    university_name = 'Royal Holloway, University of London'
    server = 'https://www.findaphd.com/'
    target_under = 'https://www.royalholloway.ac.uk/studying-here/undergraduate-courses/'
    target_post = 'https://www.royalholloway.ac.uk/studying-here/postgraduate-courses/'
    target_phd = 'https://www.findaphd.com/phds/royal-holloway-university-of-london/?40MP00'
    course_under = get_content_RoyalHolloway(target_under)
    course_post = get_content_RoyalHolloway(target_post)
    try:
        course_PhD, course_PhDD = get_contents_findaphd(target_phd,server)
    except:
        course_PhD = []
        course_PhDD = []
        print("被findaphd锁域名，稍后再试", university_name)
    DataOutput(course_under, course_post, course_PhD, course_PhDD, university_name)

'''获取皇家霍洛维的数据'''
def get_content_RoyalHolloway(target):
    li = [chr(i) for i in range(ord("A"), ord("Z") + 1)]
    a_course=[]
    driver = webdriver.Chrome(r"D:\ChromeDriver\chromedriver.exe")
    driver.get(target)
    for eachli in li:
        try:
            driver.find_element_by_link_text(eachli).click()
            time.sleep(1)
            data = driver.page_source
            bf = BeautifulSoup(data)
            texts = bf.find_all('div', class_='courseResults courseResultsLayout1 list contain')
            a_bf = BeautifulSoup(str(texts[0]))
            a = a_bf.find_all('h3', class_='courseTitle')
            for each in a:
                a_course.append(each.text)
        except:
            print("No course name starting with %s"%eachli)
    driver.close()
    return a_course

'''School of Oriental and African Studies (SOAS), University of London'''
def SOAS():
    university_name = 'School of Oriental and African Studies (SOAS), University of London'
    shape = 'article'
    classes = 'white-block'
    label = 'a'
    label_class = ''
    start='https://www.soas.ac.uk/anthropology/programmes/'
    course_under = []
    course_post = []
    course_PhD = []
    course_PhDD =[]
    next_url=[start]
    next_url.append('https://www.soas.ac.uk/soasoas/programmes/')
    next_url.append('https://www.soas.ac.uk/development/programmes/')
    next_url.append('https://www.soas.ac.uk/east-asia/programmes/')
    next_url.append('https://www.soas.ac.uk/economics/programmes/')
    next_url.append('https://www.soas.ac.uk/finance-and-management/programmes/')
    next_url.append('https://www.soas.ac.uk/history-religions-philosophies/programmes/')
    next_url.append('https://www.soas.ac.uk/languages-cultures-linguistics/programmes/')
    next_url.append('https://www.soas.ac.uk/law/programmes/')
    next_url.append('https://www.soas.ac.uk/politics/programmes/')
    for each in next_url:
        html = HTMLRequest(each)
        a_under,a_post,a_PhD,a_PhDD = HTMLParserClassified(html,shape,classes,label,label_class)
        course_under.extend(a_under)
        course_post.extend(a_post)
        course_PhD.extend(a_PhD)
    DataOutput(course_under, course_post, course_PhD, course_PhDD, university_name)

'''Swansea University'''
def Swansea():
    university_name = 'Swansea University'
    target_under = 'https://www.swansea.ac.uk/undergraduate/courses/'
    target_post = 'https://www.swansea.ac.uk/postgraduate/taught/'
    target_phd = 'https://www.swansea.ac.uk/postgraduate/research/'
    shape_under = 'ul'
    shape_post = 'ul'
    shape_phd = 'ul'
    classes_under = 'course--a-to-z'
    classes_post = 'course--a-to-z'
    classes_phd = 'course--a-to-z'
    label = 'a'
    label_class = ''
    course_post =[]
    data =HTMLSelenium(target_under)
    course_under = HTMLParserNormal(data,shape_under,classes_under,label,label_class)
    html = HTMLSelenium(target_post)
    a_post = HTMLParserNormal(html,shape_post,classes_post,label,label_class)
    course_post.extend(a_post)
    driver.get(target_phd)
    driver.find_element_by_link_text('Complete A-Z')
    time.sleep(1)
    html1 = driver.page_source
    a_under,a_post,course_PhD,course_PhDD = HTMLParserClassified(html1,shape_phd,classes_phd,label,label_class)
    course_post.extend(a_post)
    DataOutput(course_under, course_post, course_PhD, course_PhDD, university_name)


'''The London School of Economics and Political Science'''
def LSE():
    university_name = 'The London School of Economics and Political Science'
    server='https://www.lse.ac.uk/Programmes/Search-courses'
    target_under = 'https://www.lse.ac.uk/Programmes/Search-courses?collection=lse-programmes&query&=query,query&f.Study%20Type%7Ctype=undergraduate&=query&start_rank=1'
    target_post = 'https://www.lse.ac.uk/study-at-lse/Graduate/Available-programmes'
    shape_under_url = 'div'
    shape_under = 'div'
    shape_post = 'div'
    classes_under_url = 'pagination'
    classes_under = 'largeList'
    classes_post = 'accordionContainer'
    label_under = 'h1'
    label_post = 'a'
    label_class = ''
    # 找到所有需要遍历的页面，存储到next_url中
    req = requests.get(url=target_under)
    req.encoding = 'GBK'
    req.encoding = 'utf-8'
    htm = req.text
    bf = BeautifulSoup(htm)
    texts = bf.find_all(shape_under_url, class_=classes_under_url)
    next_ul_bf = BeautifulSoup(str(texts[0]))
    next_ul = next_ul_bf.find_all('a')
    next_url = [target_under]
    course_under = []
    for i in range(len(next_ul)):
        next_url.append(server + next_ul[i].get('href'))
    for i in range(len(next_url)-1):
        req = requests.get(url=next_url[i])
        req.encoding = 'GBK'
        req.encoding = 'utf-8'
        htm = req.text
        bf = BeautifulSoup(htm)
        texts = bf.find_all(shape_under, class_=classes_under)
        h1_bf = BeautifulSoup(str(texts[0]))
        h1 = h1_bf.find_all(label_under)
        for each in h1:
            course_under.append(each.text.split('\n')[-1].strip())
    data = HTMLRequest(target_post)
    course_post = []
    course_PhD = []
    course_PhDD = []
    bf = BeautifulSoup(data)
    texts = bf.find_all(shape_post, class_=classes_post)
    a_bf = BeautifulSoup(str(texts[0]))
    a = a_bf.find_all('a')
    for each in a:
        if each.string not in course_PhD:
            if 'PhD' in str(each.string):
                course_PhD.append(each.string)
        if each.string not in course_post:
            if 'MSc' in str(each.string):
                course_post.append(each.string)
            elif 'Master' in str(each.string):
                course_post.append(each.string)
            elif 'MA' in str(each.string):
                course_post.append(each.string)
            elif'MBA'in str(each.string):
                course_post.append(each.string)
            elif 'MPhil' in str(each.string):
                course_post.append(each.string)
    DataOutput(course_under, course_post, course_PhD, course_PhDD, university_name)

'''The University of Edinburgh'''
def Edinburgh():
    university_name = 'The University of Edinburgh'
    target_under = 'https://www.ed.ac.uk/studying/undergraduate/degrees/index.php?action=degreeList'
    target_post = 'https://www.ed.ac.uk/studying/postgraduate/degrees/index.php&edition=2021?r=site%2Fsearch&pgSearch=&yt0=&moa=a'
    shape_under = 'div'
    shape_post = 'div'
    classes_under = 'list-group'
    classes_post = 'list-group'
    label = 'a'
    label_class = 'list-group-item'
    html = HTMLRequest(target_under)
    course_under = HTMLParserNormal2(html, shape_under, classes_under, label, label_class)
    data = HTMLRequest(target_post)
    a_course, course_post, course_PhD, course_PhDD = HTMLParserClassified(data, shape_post, classes_post,label, label_class)
    DataOutput(course_under, course_post, course_PhD, course_PhDD, university_name)

'''University College London'''
def UCL():
    university_name = 'University College London'
    server='https://www.ucl.ac.uk'
    target_under = 'https://www.ucl.ac.uk/prospective-students/undergraduate/subject-areas'
    target_post = 'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/subject-areas'
    target_phd = 'https://www.ucl.ac.uk/prospective-students/graduate/research-degrees/subject-areas'
    shape_under = 'td'
    shape_post = 'td'
    shape_phd = 'td'
    classes_under = 'degree-list__item'
    classes_post = 'degree-list__item'
    classes_phd = 'degree-list__item'
    course_under=get_contents_UCL(target_under,shape_under,classes_under,server)
    course_post=get_contents_UCL(target_post,shape_post,classes_post,server)
    course_PhD=get_contents_UCL(target_phd,shape_phd,classes_phd,server)
    course_PhDD=[]
    DataOutput(course_under, course_post, course_PhD, course_PhDD, university_name)

'''
获取UCL专业
Parameters:
        target - 下载连接(string)
        shape - 网站上目标数据存储类型(string)
        classes - 目标数据class值(string)
        server - 根目录
'''
def get_contents_UCL(target, shape, classes,server):
    req = requests.get(url=target)
    req.encoding = 'GBK'
    req.encoding = 'utf-8'
    htm = req.text
    bf = BeautifulSoup(htm)
    texts = bf.find_all(shape, class_=classes)
    # 获取所有需要遍历的网站域名，存到next_url中
    next_url = []
    degree = []
    for i in range(len(texts)):
        a_bf = BeautifulSoup(str(texts[i]))
        a = a_bf.find_all('a')
        for each in a:
            next_url.append(server + each.get('href'))
    for i in range(len(next_url)):
        requ = requests.get(url=next_url[i])
        requ.encoding = 'GBK'
        requ.encoding = 'utf-8'
        html = requ.text
        h_bf = BeautifulSoup(html)
        texts = h_bf.find_all('div', class_='degree-list__inner')
        d_bf = BeautifulSoup(str(texts[0]))
        d = d_bf.find_all('a')
        for x in range(len(d)):
            degree.append(d[x].string.strip())
    return degree

'''University of Bath'''
def Bath():
    university_name = 'University of Bath'
    target_under = 'https://www.bath.ac.uk/courses/search/?query=&collection=ce-production-courses&f.Type+of+course%7CC=undergraduate&f.Year+of+entry%7CE=2021&start_rank='
    target_post = 'https://www.bath.ac.uk/courses/search/?query=&collection=ce-production-courses&f.Type+of+course%7CC=postgraduate&f.Year+of+entry%7CE=2021&start_rank='
    target_phd = 'https://www.bath.ac.uk/courses/search/?query=&collection=ce-production-courses&f.Type+of+course%7CC=postgraduate+research&f.Year+of+entry%7CE=2021&start_rank='
    shape_under = 'ul'
    shape_post = 'ul'
    shape_phd = 'ul'
    classes_under = 'lined-list no-bullet-list small-padding'
    classes_post = 'lined-list no-bullet-list small-padding'
    classes_phd = 'lined-list no-bullet-list small-padding'
    course_post = []
    course_under=get_contents_under_Bath(target_under, shape_under, classes_under)
    a_post=get_contents_post_Bath(target_post,shape_post,classes_post)
    course_post.extend(a_post)
    a_post,course_PhD=get_contents_phd_Bath(target_phd, shape_phd, classes_phd)
    course_post.extend(a_post)
    course_PhDD = []
    DataOutput(course_under, course_post, course_PhD, course_PhDD, university_name)

'''
获取本科和硕士专业，因为列表中含有硕士专业
Parameters:
        target - 下载连接(string)
        shape - 网站上目标数据存储类型(string)
        classes - 目标数据class值(string)
'''
def get_contents_under_Bath(target, shape, classes):
    a_course = []
    next_url=[]
    for i in range(1,200,10):
        next_url.append(target+str(i))
    for i in range(len(next_url)):
        req = requests.get(url=next_url[i])
        req.encoding = 'GBK'
        req.encoding = 'utf-8'
        htm = req.text
        bf = BeautifulSoup(htm)
        texts = bf.find_all(shape, class_=classes)
        a_bf = BeautifulSoup(str(texts[0]))
        a = a_bf.find_all('a')
        for x in range(len(a)):
            a_course.append(a[x].string.strip().split('–')[0])
    return a_course

def get_contents_post_Bath(target, shape, classes):
    a_post = []
    next_url=[]
    for i in range(1,150,10):
        next_url.append(target+str(i))
    for i in range(len(next_url)):
        req = requests.get(url=next_url[i])
        req.encoding = 'GBK'
        req.encoding = 'utf-8'
        htm = req.text
        bf = BeautifulSoup(htm)
        texts = bf.find_all(shape, class_=classes)
        a_bf = BeautifulSoup(str(texts[0]))
        a = a_bf.find_all('a')
        for x in range(len(a)):
            a_post.append(a[x].string.strip().split('–')[0])
    return a_post
'''
获取博士专业
Parameters:
        target - 下载连接(string)
        shape - 网站上目标数据存储类型(string)
        classes - 目标数据class值(string)
'''


def get_contents_phd_Bath(target, shape, classes):
    a_post = []
    a_PhD=[]
    next_url = []
    for i in range(1, 150, 10):
        next_url.append(target + str(i))
    for i in range(len(next_url)):
        req = requests.get(url=next_url[i])
        req.encoding = 'GBK'
        req.encoding = 'utf-8'
        htm = req.text
        bf = BeautifulSoup(htm)
        texts = bf.find_all(shape, class_=classes)
        a_bf = BeautifulSoup(str(texts[0]))
        a = a_bf.find_all('a')
        for x in range(len(a)):
            if a[x].string.strip():
                if 'PhD' in str(a[x].string.strip()):
                    a_PhD.append(a[x].string.strip().split('–')[0])
                    if 'MSc' in str(a[x].string.strip()):
                        a_post.append(a[x].string.strip().split('–')[0])
                    elif 'MPhil' in str(a[x].string.strip()):
                        a_post.append(a[x].string.strip().split('–')[0])
                    elif 'Master' in str(a[x].string.strip()):
                        a_post.append(a[x].string.strip().split('–')[0])
                else:
                    a_post.append(a[x].string.strip().split('–')[0])
    return a_post,a_PhD

'''University of Birmingham'''
def Birmingham():
    university_name = 'University of Birmingham'
    target_under = 'https://www.birmingham.ac.uk/undergraduate/courses/index.aspx?#CourseComplete_CollegesTab'
    target_post = 'https://www.birmingham.ac.uk/postgraduate/courses/search.aspx#CourseComplete_CollegesTab'
    target_phd = 'https://www.birmingham.ac.uk/postgraduate/courses/research/search.aspx#CourseComplete_CollegesTab'
    shape_under = 'div'
    shape_post = 'div'
    shape_phd = 'div'
    classes_under = 'accordion accordion--no-collapse js-accordion accordion--bold'
    classes_post = 'accordion accordion--no-collapse js-accordion accordion--bold'
    classes_phd = 'accordion accordion--no-collapse js-accordion accordion--bold'
    label = 'li'
    label_class = 'grid__cell unit-1-2--bp2'
    html_under = HTMLRequest(target_under)
    course_under = HTMLParserNormal(html_under, shape_under,classes_under,label, label_class)
    html_post = HTMLRequest(target_post)
    course_post = HTMLParserNormal(html_post, shape_post ,classes_post,label,label_class)
    html_phd = HTMLRequest(target_phd)
    a_under, a_post, course_PhD, course_PhDD = HTMLParserClassified(html_phd, shape_phd, classes_phd, label, label_class)
    course_post.extend(a_post)
    DataOutput(course_under, course_post, course_PhD, course_PhDD, university_name)

'''University of Bristol'''
def Bristol():
    university_name = 'University of Bristol'
    server='https://www.bristol.ac.uk/study/undergraduate/search/search_results?sort=score&sort=UndergraduateCourse-programname&dir=desc&dir=asc&query=&filter%3AUndergraduateCourse-year=2021&page='
    target_post = 'https://www.bristol.ac.uk/study/postgraduate/search/'
    shape_under = 'ul'
    shape_post = 'ul'
    classes_under = 'list-no-style list-half-spacing course-results-list'
    classes_post = 'list-no-style list-half-spacing prog-results-list'
    label = 'a'
    label_class = ''
    next_url = []
    course_under = []
    for i in range(35):
        next_url.append(server + str(i + 1))
    for each in next_url:
        html = HTMLRequest(each)
        a_under = HTMLParserNormal(html, shape_under,classes_under,label,label_class)
        course_under.extend(a_under)
    data = HTMLRequest(target_post)
    a_under, course_post, course_PhD, course_PhDD = HTMLParserClassified(data,shape_post,classes_post,label,label_class)
    DataOutput(course_under, course_post, course_PhD, course_PhDD, university_name)

'''University of Cambridge'''
def Cambridge():
    university_name = 'University of Cambridge'
    target_under = 'https://www.undergraduate.study.cam.ac.uk/courses?ucam-ref=homepage-signpost'
    target_post = 'https://2021.gaobase.admin.cam.ac.uk/api/courses.datatable?qualification_type%5B%5D=2'
    target_phd = 'https://2021.gaobase.admin.cam.ac.uk/api/courses.datatable?qualification_type%5B%5D=1'
    shape_under = 'div'
    classes_under = 'view-content'
    html_under = HTMLRequest(target_under)
    bf = BeautifulSoup(html_under)
    texts = bf.find_all(shape_under, class_=classes_under)
    course_under = []
    if texts[0]:
        a_bf = BeautifulSoup(str(texts[0]))
        a = a_bf.find_all('a')
        for i in range(len(a)):
            if a[i].string:  # 去空值
                course_under.append(a[i].string)
    if texts[1]:
        a_bf_2 = BeautifulSoup(str(texts[1]))
        a_2 = a_bf_2('a')
        for i in range(len(a_2)):
            if a_2[i].string:
                course_under.append(a_2[i].string)
    course_post = []
    html_post = HTMLRequest(target_post)
    hjson = json.loads(html_post)  # 转换程json数据格式
    for i in range(len(hjson['data']) - 1):
        course_post.append(hjson['data'][i]['full_name'])
    course_PhD = []
    course_PhDD = []
    html_phd = HTMLRequest(target_phd)
    hjson = json.loads(html_phd)  # 转换程json数据格式
    for i in range(len(hjson['data']) - 1):
        course_PhD.append(hjson['data'][i]['full_name'])
        course_PhDD.append(hjson['data'][i]['departments'])
    DataOutput(course_under, course_post, course_PhD, course_PhDD, university_name)

'''University of Dundee'''
def Dundee():
    university_name = 'University of Dundee'
    server = 'https://www.findaphd.com/'
    target_under = 'https://www.dundee.ac.uk/undergraduate/courses'
    target_post = 'https://www.dundee.ac.uk/postgraduate/courses'
    target_phd = 'https://www.findaphd.com/phds/university-of-dundee/?400a10'
    shape_under = 'div'
    shape_post = 'div'
    classes_under = 'page__content'
    classes_post = 'page__content'
    label = 'a'
    label_class = ''
    html_under = HTMLRequest(target_under)
    course_under = HTMLParserNormal(html_under,shape_under,classes_under,label,label_class)
    html_post = HTMLRequest(target_post)
    course_post = HTMLParserNormal(html_post,shape_post,classes_post,label,label_class)
    try:
        course_PhD, course_PhDD = get_contents_findaphd(target_phd,server)
    except:
        course_PhD = []
        course_PhDD = []
        print("被findaphd锁域名，稍后再试", university_name)
    DataOutput(course_under, course_post, course_PhD, course_PhDD, university_name)

'''University of Essex'''
def Essex():
    university_name = 'University of Essex'
    server = 'https://www.essex.ac.uk/course-search?collection=uoe-courses-meta&start_rank='
    shape = 'div'
    classes = 'grid grid--12 no-gutter grid--flex-desktop'
    label = 'h3'
    label_class = 'course-search-card__title purple'
    course_under = []
    course_post = []
    course_PhD = []
    course_PhDD = []
    next_url = []
    for i in range(1, 923, 10):
        next_url.append(server + str(i))
    for each in next_url:
        html = HTMLRequest(each)
        a_under,a_post,a_phd,a_phdd = HTMLParserClassified(html,shape,classes,label,label_class)
        course_under.extend(a_under)
        course_post.extend(a_post)
        course_PhD.extend(a_phd)
        course_PhDD.extend(a_phdd)
    DataOutput(course_under, course_post, course_PhD, course_PhDD, university_name)

'''University of Exeter'''
def Exeter():
    university_name = 'University of Exeter'
    target_under = 'https://www.exeter.ac.uk/undergraduate/courses2021/all-courses/'
    target_post = 'https://www.exeter.ac.uk/postgraduate/courses/all-courses/'
    target_phd_2 = 'https://search.exeter.ac.uk/s/search.html?collection=pgr-meta&course=pgr-meta&query=&profile=phd-projects&start_rank=11'
    target_phd_1 = 'https://search.exeter.ac.uk/s/search.html?collection=pgr-meta&course=pgr-meta&query=&profile=phd-projects&start_rank=1'
    shape_under = 'div'
    shape_post = 'div'
    shape_phd = 'div'
    classes_under = 'col-md-9'
    classes_post = 'col-md-9'
    classes_phd = 'fb-result__intro'
    label = 'a'
    label_class = ''
    course_under =[]
    course_post =[]
    course_PhD = []
    course_PhDD = []
    html_under = HTMLRequest(target_under)
    bf = BeautifulSoup(html_under)
    texts = bf.find_all(shape_under, class_=classes_under)
    a_bf = BeautifulSoup(str(texts[0]))
    a = a_bf.find_all(label)
    for i in range(18, len(a)):
        course_under.append(a[i].text)
    html_post = HTMLRequest(target_post)
    bf = BeautifulSoup(html_post)
    texts = bf.find_all(shape_post, class_=classes_post)
    a_bf = BeautifulSoup(str(texts[0]))
    a = a_bf.find_all(label)
    for i in range(18, len(a)):
        course_post.append(a[i].text)
    html_1 = HTMLRequest(target_phd_1)
    a_phd = HTMLParserNormal2(html_1,shape_phd,classes_phd,label,label_class)
    course_PhD.extend(a_phd)
    html_2 = HTMLRequest(target_phd_2)
    a_phd = HTMLParserNormal2(html_2, shape_phd, classes_phd, label, label_class)
    course_PhD.extend(a_phd)
    DataOutput(course_under, course_post, course_PhD, course_PhDD, university_name)


'''University of Glasgow'''
def Glasgow():
    university_name = 'University of Glasgow'
    target_under = 'https://www.gla.ac.uk/undergraduate/degrees/'
    target_post = 'https://www.gla.ac.uk/postgraduate/taught/'
    target_phd = 'https://www.gla.ac.uk/postgraduate/research/'
    shape_under = 'ul'
    shape_post = 'ul'
    shape_phd = 'ul'
    classes_under = 'programme-list'
    classes_post = 'programme-list'
    classes_phd = 'programme-list'
    label = 'a'
    label_class = ''
    course_post = []
    html_under = HTMLRequest(target_under)
    course_under = HTMLParserNormal(html_under,shape_under,classes_under,label,label_class)
    html_post = HTMLRequest(target_post)
    a_post = HTMLParserNormal(html_post,shape_post,classes_post,label,label_class)
    course_post.extend(a_post)
    html_phd = HTMLRequest(target_phd)
    a_under,a_post,course_PhD,course_PhDD = HTMLParserClassified(html_phd,shape_phd,classes_phd,label,label_class)
    course_post.extend(a_post)
    DataOutput(course_under, course_post, course_PhD, course_PhDD, university_name)

'''University of Kent'''
def Kent():
    university_name = 'University of Kent'
    target_under = 'https://www.kent.ac.uk/courses/undergraduate'
    target_post = 'https://www.kent.ac.uk/courses/postgraduate'
    shape_under = 'div'
    shape_post = 'div'
    classes_under = 'content content--main content--filter'
    classes_post = 'content content--main content--filter'
    label = 'h3'
    label_class = 'card__title'
    html = HTMLSelenium(target_under)
    course_under = HTMLParserNormal(html,shape_under,classes_under,label,label_class)
    data = HTMLSelenium(target_post)
    a_under, course_post,course_PhD,course_PhDD = HTMLParserClassified(data,shape_post,classes_post,label,label_class)
    DataOutput(course_under, course_post, course_PhD, course_PhDD, university_name)


'''University of Leeds'''
def Leeds():
    university_name = 'University of Leeds'
    server = 'https://www.findaphd.com/'
    target_under = 'https://courses.leeds.ac.uk/course-search?query=&type=UG'
    target_post = 'https://courses.leeds.ac.uk/course-search?query=&type=PGT'
    target_phd = 'https://www.findaphd.com/phds/university-of-leeds/?40gg10'
    shape_under = 'div'
    shape_post = 'div'
    classes_under = 'col-xs-12 col-md-9'
    classes_post = 'col-xs-12 col-md-9'
    label = 'a'
    label_class = ''
    html = HTMLSelenium(target_under)
    course_under = HTMLParserNormal(html,shape_under,classes_under,label,label_class)
    html = HTMLSelenium(target_post)
    course_post = HTMLParserNormal(html,shape_post,classes_post,label,label_class)
    try:
        course_PhD,course_PhDD = get_contents_findaphd(target_phd,server)
    except:
        course_PhD = []
        course_PhDD = []
        print("被findaphd锁域名，稍后再试", university_name)
    DataOutput(course_under, course_post, course_PhD, course_PhDD, university_name)


'''University of Leicester'''
def Leicester():
    university_name = 'University of Leicester'
    server='https://le.ac.uk/courses?q=&level=&Page='
    target_phd='https://www.findaphd.com/phds/university-of-leicester/?40wg10'
    server_phd='https://www.findaphd.com/'
    shape = 'ul'
    classes = 'search-result-list'
    label = 'a'
    label_class = ''
    course_under = []
    course_post = []
    course_PhD = []
    course_PhDD = []
    next_url=[]
    for i in range(32):
        next_url.append(server+str(i+1))
    print(next_url)
    for x in range(len(next_url)):
        html = HTMLRequest(next_url[x])
        a_under,a_post,a_phd,a_phdd = HTMLParserClassified(html,shape,classes,label,label_class)
        course_under.extend(a_under)
        course_post.extend(a_post)
        course_PhD.extend(a_phd)
        course_PhDD.extend(a_phdd)
        print('网页页码：(总共32页)', x)
    try:
        a_phd ,a_phdd = get_contents_findaphd(target_phd,server_phd)
        course_PhD.extend(a_phd)
        course_PhDD.extend(a_phdd)
    except:
        course_PhD = []
        course_PhDD = []
        print("被findaphd锁域名，稍后再试", university_name)
    DataOutput(course_under, course_post, course_PhD, course_PhDD, university_name)

'''University of Liverpool'''
def Liverpool():
    university_name = 'University of Liverpool'
    target_under = 'https://www.liverpool.ac.uk/course-search-results/?collection=liverpool-course-search&page=1&query=&f.IsCourse|Z=yes&f.IsCourse|Y=undergraduate&start_rank='
    target_post = 'https://www.liverpool.ac.uk/course-search-results/?collection=liverpool-course-search&page=1&query=&f.IsCourse|Z=yes&f.IsCourse|Y=postgraduate+taught&start_rank='
    target_phd = 'https://www.liverpool.ac.uk/course-search-results/?collection=liverpool-course-search&page=1&query=&f.IsCourse|Z=yes&f.IsCourse|Y=postgraduate+research&start_rank='
    shape = 'section'
    classes = 'clearfix full'
    label = 'h2'
    label_class = ''
    next_url = []
    course_under = []
    course_post = []
    course_PhD = []
    course_PhDD = []
    for i in range(1, 160, 50):
        next_url.append(target_under + str(i))
        next_url.append(target_post + str(i))
        next_url.append(target_phd + str(i))
    for each in next_url:
        html = HTMLRequest(each)
        a_under,a_post,a_phd,a_phdd = HTMLParserClassified(html,shape,classes,label,label_class)
        course_under.extend(a_under)
        course_post.extend(a_post)
        course_PhD.extend(a_phd)
        course_PhDD.extend(a_phdd)
    DataOutput(course_under, course_post, course_PhD, course_PhDD, university_name)

'''University of Manchester'''
def Manchester():
    university_name = 'University of Manchester'
    target_under = 'https://www.manchester.ac.uk/study/undergraduate/courses/2021/basic/'
    target_post = 'https://www.manchester.ac.uk/study/masters/courses/list/basic/'
    target_phd = 'https://www.manchester.ac.uk/study/postgraduate-research/programmes/list/basic/'
    shape_under = 'ul'
    shape_post = 'ul'
    classes_under = 'course-list undergraduate'
    classes_post = 'course-list postgraduate'
    label = 'a'
    label_class = ''
    course_post = []
    course_PhD = []
    course_PhDD = []
    next_url = [target_post,target_phd]
    html = HTMLRequest(target_under)
    course_under = HTMLParserNormal(html,shape_under,classes_under,label,label_class)
    for each in next_url:
        html = HTMLRequest(each)
        a_under,a_post,a_phd,a_phdd = HTMLParserClassified(html,shape_post,classes_post,label,label_class)
        course_post.extend(a_post)
        course_PhD.extend(a_phd)
        course_PhDD.extend(a_phdd)
    DataOutput(course_under, course_post, course_PhD, course_PhDD, university_name)

'''University of Nottingham'''
def Nottingham():
    university_name = 'University of Nottingham'
    target_under = 'https://www.nottingham.ac.uk/ugstudy/courses/2021-courses-a-to-z.aspx'
    target_post = 'https://www.nottingham.ac.uk/pgstudy/courses/courses.aspx'
    course_under = []
    course_post = []
    course_PhD = []
    course_PhDD = []
    next_url_under=[]
    a_course = []
    html = HTMLRequest(target_under)
    bf = BeautifulSoup(html)
    texts = bf.find_all('div', class_='sys_atoz-control')
    a_bf = BeautifulSoup(str(texts[0]))
    a = a_bf.find_all('a')
    for each in a:
        next_url_under.append(target_under+each.get('href'))
    for each in next_url_under:
        html = HTMLRequest(each)
        bf = BeautifulSoup(html)
        course = bf.find_all('div', class_='sys_subitem')
        for each in course:
            a_course.append(each.text.strip())
        course_under.extend(a_course)
    next_url_post=[]
    a_post = []
    a_PhD = []
    a_phdd =[]
    htm = HTMLRequest(target_post)
    bf = BeautifulSoup(htm)
    texts = bf.find_all('div', class_='sys_atoz-control')
    a_bf = BeautifulSoup(str(texts[0]))
    a = a_bf.find_all('a')
    for each in a:
        next_url_post.append(target_post+each.get('href'))
    for each in next_url_post:
        html = HTMLRequest(each)
        bf = BeautifulSoup(html)
        course = bf.find_all('div', class_='courseCard')
        for x in range(len(course)):
            h3_bf = BeautifulSoup(str(course[x]))
            h3 = h3_bf.find('h3')
            if 'PhD' in str(h3.string):
                a_PhD.append(h3.string)
                if 'MSc' in str(h3.string):
                    a_post.append(h3.string)
                elif 'MPhil' in str(h3.string):
                    a_post.append(h3.string)
                elif 'Master' in str(h3.string):
                    a_post.append(h3.string)
                elif 'MRes' in str(h3.string):
                    a_post.append(h3.string)
            else:
                a_post.append(h3.string)
        course_post.extend(a_post)
        course_PhD.extend(a_PhD)
        course_PhDD.extend(a_phdd)
    DataOutput(course_under, course_post, course_PhD, course_PhDD, university_name)

'''University of Oxford'''
def Oxford():
    university_name = 'University of Oxford'
    target_under = 'https://www.ox.ac.uk/admissions/undergraduate/courses/course-listing'
    target_post = 'https://www.ox.ac.uk/admissions/graduate/courses/courses-a-z-listing'
    shape_under = 'table'
    shape_post = 'div'
    classes_under = 'table-reduced'
    classes_post = 'course-title'
    label = 'a'
    label_class = ''
    html = HTMLRequest(target_under)
    course_under = HTMLParserNormal(html,shape_under,classes_under,label,label_class)
    a_PhD = []
    a_PhDD = []
    a_post = []
    htm = HTMLRequest(target_post)
    bf = BeautifulSoup(htm)
    texts = bf.find_all(shape_post, class_=classes_post)  # print(texts[0].text)
    department = bf.find_all('div', class_='course-department')
    for i in range(len(texts)):
        a_bf = BeautifulSoup(str(texts[i]))
        a = a_bf.find_all('a')
        if 'DPhil' in texts[i].text:  # 判断是硕士专业还是博士专业
            a_PhD.append(a[0].string)
            a_PhDD.append(department[i].string)
        elif 'PhD' in texts[i].text:
            a_PhD.append(a[0].string)
            a_PhDD.append(department[i].string)
        else:
            a_post.append(a[0].string)
    DataOutput(course_under, a_post, a_PhD, a_PhDD, university_name)


'''University of Reading'''
def Reading():
    university_name =' University of Reading'
    server = 'https://www.findaphd.com/'
    target_phd='https://www.findaphd.com/phds/university-of-reading/?40gm10'
    a_under=[]
    a_post = []
    req = requests.get(url='http://www.reading.ac.uk/ready-to-study')
    req.encoding = 'GBK'
    req.encoding = 'utf-8'
    htm = req.text
    bf = BeautifulSoup(htm)
    texts = bf.find_all('div', class_='row-margin-small m-margin-bottom accordion')
    a_under_bf=BeautifulSoup(str(texts[0]))
    a_post_bf = BeautifulSoup(str(texts[1]))
    a_under_b=a_under_bf.find_all('a')
    for each in a_under_b:
        a_under.append(each.string)
    a_post_b = a_post_bf.find_all('a')
    for each in a_post_b:
        a_post.append(each.string)
    try:
        a_PhD,a_PhDD = get_contents_findaphd(target_phd,server)
    except:
        a_PhD = []
        a_PhDD = []
        print("被findaphd锁域名，稍后再试", university_name)
    DataOutput(a_under, a_post, a_PhD, a_PhDD, university_name)

'''University of Sheffield'''
def Sheffield():
    university_name = 'University of Sheffield'
    server = 'https://www.findaphd.com/'
    target_under = 'https://www.sheffield.ac.uk/undergraduate/courses/2021'
    target_post = 'https://www.sheffield.ac.uk/postgraduate/taught/courses/2021'
    target_phd = 'https://www.findaphd.com/phds/university-of-sheffield/?400n10'
    shape_under = 'div'
    shape_post = 'div'
    classes_under = 'views-element-container'
    classes_post = 'views-element-container'
    label = 'span'
    label_class = 'listcourse'
    html =HTMLRequest(target_under)
    course_under = HTMLParserNormal(html,shape_under,classes_under,label,label_class)
    data = HTMLRequest(target_post)
    course_post = HTMLParserNormal(data,shape_post,classes_post,label,label_class)
    try:
        course_PhD, course_PhDD = get_contents_findaphd(target_phd,server)
    except:
        course_PhD = []
        course_PhDD = []
        print("被findaphd锁域名，稍后再试", university_name)
    DataOutput(course_under, course_post, course_PhD, course_PhDD, university_name)

'''University of Southampton'''
def Southampton():
    university_name = 'University of Southampton'
    server = 'https://www.findaphd.com/'
    target_under = 'https://www.southampton.ac.uk/courses/undergraduate'
    target_post = 'https://www.southampton.ac.uk/courses/postgraduate-taught'
    target_phd = 'https://www.findaphd.com/phds/university-of-southampton/?40gn10'
    shape_under = 'div'
    shape_post = 'div'
    classes_under = 'views-element-container'
    classes_post = 'views-element-container'
    label = 'div'
    label_class = 'font-bold text-xl text-endeavour hover:text-midnight md:text-2xl leading-tight'
    html = HTMLRequest(target_under)
    course_under = HTMLParserNormal(html, shape_under, classes_under, label, label_class)
    data = HTMLRequest(target_post)
    course_post = HTMLParserNormal(data, shape_post, classes_post, label, label_class)
    try:
        course_PhD, course_PhDD = get_contents_findaphd(target_phd, server)
    except:
        course_PhD = []
        course_PhDD = []
        print("被findaphd锁域名，稍后再试", university_name)
    DataOutput(course_under, course_post, course_PhD, course_PhDD, university_name)

'''University of St Andrews'''
def St_Andrews():
    university_name = 'University of St Andrews'
    server = 'https://www.st-andrews.ac.uk'
    server2 = 'https://www.findaphd.com'
    target_phd = 'https://www.findaphd.com/phds/university-of-st-andrews/?40wn10'
    a_under = []
    a_post = []
    req = requests.get(url='https://www.st-andrews.ac.uk/subjects/study-options/')
    req.encoding = 'GBK'
    req.encoding = 'utf-8'
    htm = req.text
    bf = BeautifulSoup(htm)
    texts = bf.find_all('div', class_='col-sm-4')
    a1_bf = BeautifulSoup(str(texts[7]))
    a2_bf = BeautifulSoup(str(texts[8]))
    a1 = a1_bf.find_all('a')
    a2 = a2_bf.find_all('a')
    next_url=[]
    for each in a1:
        next_url.append(server+each.get('href'))
    for each in a2:
        next_url.append(server+each.get('href'))
    for i in range(len(next_url)):
        req = requests.get(url=next_url[i])
        req.encoding = 'GBK'
        req.encoding = 'utf-8'
        htm = req.text
        bf = BeautifulSoup(htm)
        texts = bf.find_all('a', class_='list-group-item')
        for each in texts:
            if each.text:
                if 'MSc' in str(each.text):
                    a_post.append(each.text)
                elif 'MPhil' in str(each.text):
                    a_post.append(each.text)
                elif 'Master' in str(each.text):
                    a_post.append(each.text)
                elif 'MLitt' in str(each.text):
                    a_post.append(each.text)
                else:
                    a_under.append(each.text)
    try:
        course_PhD,course_PhDD = get_contents_findaphd_StAndrews(target_phd,server2)
    except:
        course_PhD = []
        course_PhDD = []
        print("被findaphd锁域名，稍后再试", university_name)
    DataOutput(a_under, a_post, course_PhD, course_PhDD, university_name)

def get_contents_findaphd_StAndrews(target, server):
    a_PhD = []
    a_PhDD = []
    # 第一次request定位所有需要爬虫网页地址
    req = requests.get(url=target)
    req.encoding = 'GBK'
    req.encoding = 'utf-8'
    htm = req.text
    bf = BeautifulSoup(htm)
    texts = bf.find_all('div', class_='resultsRow phd-result-row-standard phd-result col-xs-24 tight')
    for i in range(len(texts)):
        texts1_bf = BeautifulSoup(str(texts[i]))
        # 课程名称
        texts1 = texts1_bf.find_all('a', class_="courseLink phd-result__title")
        a_PhD.append(texts1[0].string)
        # 防止没有列出部门的课程，防止数据串行
        if 'deptLink phd-result__dept-inst--dept phd-result__dept-inst--title' in str(texts[i]):
            # 部门
            texts2 = texts1_bf.find_all('a', class_="deptLink phd-result__dept-inst--dept phd-result__dept-inst--title")
            a_PhDD.append(texts2[0].string)
        else:
            # 如果部门没有数据，使用校名
            a_PhDD.append(None)
    return a_PhD, a_PhDD


'''University of Stirling'''
def Stirling():
    university_name = 'University of Stirling'
    target = 'https://www.stir.ac.uk/courses/?filter__level=Postgraduate,Undergraduate,module'
    shape = 'div'
    classes = 'c-search-results'
    label = 'a'
    label_class = ''
    html = HTMLSelenium(target)
    course_under,course_post,course_PhD,course_PhDD = HTMLParserClassified(html,shape,classes,label,label_class)
    DataOutput(course_under, course_post, course_PhD, course_PhDD, university_name)


'''University of Strathclyde'''
def Strathclyde():
    university_name = 'University of Strathclyde'
    target = 'https://www.strath.ac.uk/courses/'
    shape = 'div'
    classes = 'searchstriped scroll-show'
    label = 'h2'
    label_class = ''
    html = HTMLRequest(target)
    course_under,course_post,course_PhD,course_PhDD = HTMLParserClassified(html,shape,classes,label,label_class)
    driver.close()
    DataOutput(course_under, course_post, course_PhD, course_PhDD, university_name)

'''University of Surrey'''
def Surrey():
    university_name = 'University of Surrey'
    target_under = 'https://www.surrey.ac.uk/undergraduate'
    target_post = 'https://www.surrey.ac.uk/postgraduate'
    target_phd = 'https://www.surrey.ac.uk/postgraduate/research'
    shape_under = 'div'
    shape_post = 'div'
    shape_phd = 'div'
    classes_under = 'mt-4 text-secondary'
    classes_post = 'mt-4 text-secondary'
    classes_phd = 'mt-4 text-secondary'
    label = 'a'
    label_class = ''
    html = HTMLRequest(target_under)
    course_under = HTMLParserNormal(html,shape_under,classes_under,label,label_class)
    html = HTMLRequest(target_post)
    course_post = HTMLParserNormal(html,shape_post,classes_post,label,label_class)
    html = HTMLRequest(target_phd)
    course_PhD = HTMLParserNormal(html,shape_phd,classes_phd,label,label_class)
    course_PhDD = []
    DataOutput(course_under, course_post, course_PhD, course_PhDD, university_name)

'''University of Sussex'''
def Sussex():
    university_name = 'University of Sussex'
    target_under = 'https://www.sussex.ac.uk/study/undergraduate/'
    target_post = 'https://www.sussex.ac.uk/study/masters/'
    target_phd = 'https://www.sussex.ac.uk/study/phd'
    shape_under = 'div'
    shape_post = 'div'
    shape_phd = 'div'
    classes_under = 'accordion-content'
    classes_post = 'accordion-content'
    classes_phd = 'accordion-content'
    label = 'a'
    label_class = ''
    html = HTMLRequest(target_under)
    course_under = HTMLParserNormal2(html,shape_under,classes_under,label,label_class)
    html = HTMLRequest(target_post)
    course_post = HTMLParserNormal2(html,shape_post,classes_post,label,label_class)
    html = HTMLRequest(target_phd)
    course_PhD = HTMLParserNormal2(html,shape_phd,classes_phd,label,label_class)
    course_PhDD = []
    DataOutput(course_under, course_post, course_PhD, course_PhDD, university_name)

'''University of Warwick'''
def Warwick():
    university_name = 'University of Warwick'
    target_under = 'https://warwick.ac.uk/study/undergraduate/courses/'
    target_post = 'https://warwick.ac.uk/study/postgraduate/taught/courses-2020/'
    target_phd = 'https://warwick.ac.uk/study/postgraduate/research/courses-2020/'
    shape_under = 'div'
    shape_post = 'div'
    classes_under = 'sb-glossary-terms'
    classes_post = 'sb-glossary-terms'
    label_under = 'p'
    label_post = 'h5'
    label_class =''
    course_post = []
    course_PhD = []
    course_PhDD = []
    html =HTMLRequest(target_under)
    course_under = HTMLParserNormal(html,shape_under,classes_under,label_under,label_class)
    next_url = [target_post,target_phd]
    for each in next_url:
        html = HTMLRequest(each)
        a_under,a_post,a_phd,a_phdd = HTMLParserClassified(html,shape_post,classes_post,label_post,label_class)
        course_post.extend(a_post)
        course_PhD.extend(a_phd)
        course_PhDD.extend(a_phdd)
    DataOutput(course_under, course_post, course_PhD, course_PhDD, university_name)

'''University of York'''
def York():
    university_name = 'University of York'
    target_under = 'https://www.york.ac.uk/study/undergraduate/courses/all'
    target_post = 'https://www.york.ac.uk/study/postgraduate/courses/all?mode=taught&q=&level=postgraduate'
    target_phd = 'https://www.york.ac.uk/study/postgraduate/courses/all?mode=research&q=&level=postgraduate'
    shape_under = 'table'
    shape_post = 'table'
    classes_under = 'courses c-table--striped'
    classes_post = 'courses c-table--striped c-table--stacked'
    label = 'strong'
    label_class = ''
    a_PhD = []
    a_PhDD = []
    html = HTMLRequest(target_under)
    course_under = HTMLParserNormal(html,shape_under,classes_under,label,label_class)
    html = HTMLRequest(target_post)
    a_post = HTMLParserNormal(html,shape_post,classes_post,label,label_class)
    html = HTMLRequest(target_phd)
    bf = BeautifulSoup(html)
    texts = bf.find_all(shape_post, class_=classes_post)
    a_bf = BeautifulSoup(str(texts[0]))
    course = a_bf.find_all('td', class_='coursetitle')
    detail = a_bf.find_all('td', class_='detail')
    for i in range(len(course)):
        if course[i].text:
            if 'PhD' in str(detail[i].text):
                a_PhD.append(course[i].text.strip())
                if 'MSc' in str(detail[i].text):
                    a_post.append(course[i].text.strip())
                elif 'MPhil' in str(detail[i].text):
                    a_post.append(course[i].text.strip())
                elif 'Master' in str(detail[i].text):
                    a_post.append(course[i].text.strip())
            else:
                a_post.append(course[i].text.strip())
    DataOutput(course_under, a_post, a_PhD, a_PhDD, university_name)

'''
    Request方法HTML网页下载器
    Parameters:
            target - 下载连接(string)
'''
def HTMLRequest(target):
    req = requests.get(url=target)
    req.encoding = 'GBK'
    req.encoding = 'utf-8'
    html = req.text
    return html

'''
    selenium方法HTML网页下载器
    Parameters:
            target - 下载连接(string)
'''
def HTMLSelenium(target):
    driver.get(target)
    time.sleep(2)
    html = driver.page_source
    return html

'''
    一般形式解析器，不需分类
    Parameters:
            target - 下载连接(string)
            shape - 网站上目标数据存储类型(string)
            classes - 目标数据class值(string)
'''


def HTMLParserNormal(html, shape, classes, label, label_class):
    a_degree = []
    bf = BeautifulSoup(html)
    texts = bf.find_all(shape, class_=classes)
    a_bf = BeautifulSoup(str(texts[0]))
    a = a_bf.find_all(label, class_=label_class)
    for i in range(len(a)):
        if a[i].text.strip not in a_degree:
            a_degree.append(a[i].text.strip().replace('                             ','').replace('       ',' '))
    return a_degree

def HTMLParserNormal2(html, shape, classes, label, label_class):
    a_degree = []
    bf = BeautifulSoup(html)
    texts = bf.find_all(shape, class_=classes)
    for x in range(len(texts)):
        a_bf = BeautifulSoup(str(texts[x]))
        a = a_bf.find_all(label, class_=label_class)
        for i in range(len(a)):
            if a[i].text not in a_degree:
                a_degree.append(a[i].text.strip().replace('                             ','').replace('       ',' '))
    return a_degree

def HTMLParserClassified(html, shape, classes, label, label_class):
    a_under = []
    a_post = []
    a_PhD = []
    a_PhDD = []
    bf = BeautifulSoup(html)
    texts = bf.find_all(shape, class_=classes)
    a_bf = BeautifulSoup(str(texts[0]))
    a = a_bf.find_all(label, class_=label_class)
    for i in range(len(a)):
        if a[i] not in a_under:
            if 'BSc' in str(a[i].text):
                a_under.append(a[i].text.strip().replace('\t', '').replace('\n', '').replace('\xa0', ' ').replace(
                    '                                                            ', ' ').replace('                  ',
                                                                                                 '').replace(
                    '                 ', '').replace('                             ','').replace('       ',' ').replace('                                            ',''))
            elif 'BEng' in str(a[i].text):
                a_under.append(a[i].text.strip().replace('\t', '').replace('\n', '').replace('\xa0', ' ').replace(
                    '                                                            ', ' ').replace('                  ',
                                                                                                 '').replace(
                    '                 ', '').replace('                             ','').replace('       ',' ').replace('                                            ',''))
            elif 'BA' in str(a[i].text):
                a_under.append(a[i].text.strip().replace('\t', '').replace('\n', '').replace('\xa0', ' ').replace(
                    '                                                            ', ' ').replace('                  ',
                                                                                                 '').replace(
                    '                 ', '').replace('                             ','').replace('       ',' ').replace('                                            ',''))
            elif 'BDS' in str(a[i].text):
                a_under.append(a[i].text.strip().replace('\t', '').replace('\n', '').replace('\xa0', ' ').replace(
                    '                                                            ', ' ').replace('                  ',
                                                                                                 '').replace(
                    '                 ', '').replace('                             ','').replace('       ',' ').replace('                                            ',''))
            elif 'LLB' in str(a[i].text):
                a_under.append(a[i].text.strip().replace('\t', '').replace('\n', '').replace('\xa0', ' ').replace(
                    '                                                            ', ' ').replace('                  ',
                                                                                                 '').replace(
                    '                 ', '').replace('                             ','').replace('       ',' ').replace('                                            ',''))
            elif 'BSW' in str(a[i].text):
                a_under.append(a[i].text.strip().replace('\t', '').replace('\n', '').replace('\xa0', ' ').replace(
                    '                                                            ', ' ').replace('                  ',
                                                                                                 '').replace(
                    '                 ', '').replace('                             ','').replace('       ',' ').replace('                                            ',''))
        if a[i].text not in a_post:
            if 'MSc' in str(a[i].text):
                a_post.append(a[i].text.strip().replace('\t', '').replace('\n', '').replace('\xa0', ' ').replace(
                    '                                                            ', ' ').replace('                  ',
                                                                                                 '').replace(
                    '                 ', '').replace('                             ','').replace('       ',' ').replace('                                            ',''))
            elif 'MSci' in str(a[i].text):
                a_post.append(a[i].text.strip().replace('\t', '').replace('\n', '').replace('\xa0', ' ').replace(
                    '                                                            ', ' ').replace('                  ',
                                                                                                 '').replace(
                    '                 ', '').replace('                             ','').replace('       ',' ').replace('                                            ',''))
            elif 'MBA' in str(a[i].text):
                a_post.append(a[i].text.strip().replace('\t', '').replace('\n', '').replace('\xa0', ' ').replace(
                    '                                                            ', ' ').replace('                  ',
                                                                                                 '').replace(
                    '                 ', '').replace('                             ','').replace('       ',' ').replace('                                            ',''))
            elif 'MEng' in str(a[i].text):
                a_post.append(a[i].text.strip().replace('\t', '').replace('\n', '').replace('\xa0', ' ').replace(
                    '                                                            ', ' ').replace('                  ',
                                                                                                 '').replace(
                    '                 ', '').replace('                             ','').replace('       ',' ').replace('                                            ',''))
            elif 'MPhil' in str(a[i].text):
                a_post.append(a[i].text.strip().replace('\t', '').replace('\n', '').replace('\xa0', ' ').replace(
                    '                                                            ', ' ').replace('                  ',
                                                                                                 '').replace(
                    '                 ', '').replace('                             ','').replace('       ',' ').replace('                                            ',''))
            elif 'PgCert' in str(a[i].text):
                a_post.append(a[i].text.strip().replace('\t', '').replace('\n', '').replace('\xa0', ' ').replace(
                    '                                                            ', ' ').replace('                  ',
                                                                                                 '').replace(
                    '                 ', '').replace('                             ','').replace('       ',' ').replace('                                            ',''))
            elif 'PgDip' in str(a[i].text):
                a_post.append(a[i].text.strip().replace('\t', '').replace('\n', '').replace('\xa0', ' ').replace(
                    '                                                            ', ' ').replace('                  ',
                                                                                                 '').replace(
                    '                 ', '').replace('                             ','').replace('       ',' ').replace('                                            ',''))
            elif 'MA' in str(a[i].text):
                a_post.append(a[i].text.strip().replace('\t', '').replace('\n', '').replace('\xa0', ' ').replace(
                    '                                                            ', ' ').replace('                  ',
                                                                                                 '').replace(
                    '                 ', '').replace('                             ','').replace('       ',' ').replace('                                            ',''))
            elif 'MRes' in str(a[i].text):
                a_post.append(a[i].text.strip().replace('\t', '').replace('\n', '').replace('\xa0', ' ').replace(
                    '                                                            ', ' ').replace('                  ',
                                                                                                 '').replace(
                    '                 ', '').replace('                             ','').replace('       ',' ').replace('                                            ',''))
            elif 'GradCert' in str(a[i].text):
                a_post.append(a[i].text.strip().replace('\t', '').replace('\n', '').replace('\xa0', ' ').replace(
                    '                                                            ', ' ').replace('                  ',
                                                                                                 '').replace(
                    '                 ', '').replace('                             ','').replace('       ',' ').replace('                                            ',''))
            elif 'PGCE' in str(a[i].text):
                a_post.append(a[i].text.strip().replace('\t', '').replace('\n', '').replace('\xa0', ' ').replace(
                    '                                                            ', ' ').replace('                  ',
                                                                                                 '').replace(
                    '                 ', '').replace('                             ','').replace('       ',' ').replace('                                            ',''))
            elif 'MEd' in str(a[i].text):
                a_post.append(a[i].text.strip().replace('\t', '').replace('\n', '').replace('\xa0', ' ').replace(
                    '                                                            ', ' ').replace('                  ',
                                                                                                 '').replace(
                    '                 ', '').replace('                             ','').replace('       ',' ').replace('                                            ',''))
            elif 'LLM' in str(a[i].text):
                a_post.append(a[i].text.strip().replace('\t', '').replace('\n', '').replace('\xa0', ' ').replace(
                    '                                                            ', ' ').replace('                  ',
                                                                                                 '').replace(
                    '                 ', '').replace('                             ','').replace('       ',' ').replace('                                            ',''))
            elif 'MPH' in str(a[i].text):
                a_post.append(a[i].text.strip().replace('\t', '').replace('\n', '').replace('\xa0', ' ').replace(
                    '                                                            ', ' ').replace('                  ',
                                                                                                 '').replace(
                    '                 ', '').replace('                             ','').replace('       ',' ').replace('                                            ',''))
            elif 'Research' in str(a[i].text):
                a_post.append(a[i].text.strip().replace('\t', '').replace('\n', '').replace('\xa0', ' ').replace(
                    '                                                            ', ' ').replace('                  ',
                                                                                                 '').replace(
                    '                 ', '').replace('                             ','').replace('       ',' ').replace('                                            ',''))
        if a[i].text not in a_PhD:
            if 'PhD' in str(a[i].text):
                a_PhD.append(a[i].text.strip().replace('\t', '').replace('\n', '').replace('\xa0', ' ').replace(
                    '                                                            ', ' ').replace('                  ',
                                                                                                 '').replace(
                    '                 ', '').replace('                             ','').replace('       ',' ').replace('                                            ',''))
            elif 'DClinPsych' in str(a[i].text):
                a_PhD.append(a[i].text.strip().replace('\t', '').replace('\n', '').replace('\xa0', ' ').replace(
                    '                                                            ', ' ').replace('                  ',
                                                                                                 '').replace(
                    '                 ', '').replace('                             ','').replace('       ',' ').replace('                                            ',''))
            elif 'DST' in str(a[i].text):
                a_PhD.append(a[i].text.strip().replace('\t', '').replace('\n', '').replace('\xa0', ' ').replace(
                    '                                                            ', ' ').replace('                  ',
                                                                                                 '').replace(
                    '                 ', '').replace('                             ','').replace('       ',' ').replace('                                            ',''))
            elif 'Doctorate' in str(a[i].text):
                a_PhD.append(a[i].text.strip().replace('\t', '').replace('\n', '').replace('\xa0', ' ').replace(
                    '                                                            ', ' ').replace('                  ',
                                                                                                 '').replace(
                    '                 ', '').replace('                             ','').replace('       ',' ').replace('                                            ',''))
            elif 'PHD' in str(a[i].text):
                a_PhD.append(a[i].text.strip().replace('\t', '').replace('\n', '').replace('\xa0', ' ').replace(
                    '                                                            ', ' ').replace('                  ',
                                                                                                 '').replace(
                    '                 ', '').replace('                             ','').replace('       ',' ').replace('                                            ',''))

    return a_under, a_post, a_PhD, a_PhDD


'''
在finaphd网站获取phd专业和对应department
Parameters:
        target - 下载连接(string)
        server - 多个目标网页网页前缀(string)
'''
def get_contents_findaphd(target, server):
    a_PhD = []
    a_PhDD = []
    # 第一次request定位所有需要爬虫网页地址
    req = requests.get(url=target)
    req.encoding = 'GBK'
    req.encoding = 'utf-8'
    htm = req.text
    bf = BeautifulSoup(htm)
    # 定位另外几个网页后缀存到ul中
    ul = bf.find_all('ul', class_='pagi1ngArea')  # print(ul[0])
    a_bf = BeautifulSoup(str(ul[0]))
    a = a_bf.find_all('a')
    last_num = len(a) - 1  # last_num：最后一页  # print(a[last_num].string)  #a[last_num].string：最后一页页码
    next_ul = server + a[0].get('href')  # 网页前后缀相加  #  print(next_ul.split('=')[0])
    # 定义列表存放所有目标网页url
    next_url = [target]  # 添加首页url
    for i in range(int(a[last_num].string) - 1):
        next_url.append(next_ul.split('=')[0] + '=' + str(i + 2))  # print(next_url) #目标网页url列表赋值
    # 第二次request查找phd专业和对应department数据
    for i in range(len(next_url)):
        req = requests.get(url=next_url[i])
        req.encoding = 'GBK'
        req.encoding = 'utf-8'
        htm = req.text
        bf = BeautifulSoup(htm)
        texts = bf.find_all('div', class_='resultsRow phd-result-row-standard phd-result col-xs-24 tight')
        for i in range(len(texts)):
            texts1_bf = BeautifulSoup(str(texts[i]))
            # 课程名称
            texts1 = texts1_bf.find_all('a', class_="courseLink phd-result__title")
            a_PhD.append(texts1[0].string)
            # 防止没有列出部门的课程，防止数据串行
            if 'deptLink phd-result__dept-inst--dept phd-result__dept-inst--title' in str(texts[i]):
                # 部门
                texts2 = texts1_bf.find_all('a',
                                            class_="deptLink phd-result__dept-inst--dept phd-result__dept-inst--title")
                a_PhDD.append(texts2[0].string)
            else:
                # 如果部门没有数据，使用校名
                a_PhDD.append(None)
    return a_PhD, a_PhDD


'''
列表长度补齐，方便写入
Parameters:
        a_under - 本科专业
        a_post - 硕士专业
        a_PhD - 博士专业
        a_PhDD - 博士专业部门
'''


def format(a_under, a_post, a_PhD, a_PhDD):
    maxlen = max(len(a_under), len(a_post), len(a_PhD), len(a_PhDD))
    a_under += [None for i in range(maxlen - len(a_under))]
    a_post += [None for i in range(maxlen - len(a_post))]
    a_PhD += [None for i in range(maxlen - len(a_PhD))]
    a_PhDD += [None for i in range(maxlen - len(a_PhDD))]
    return a_under, a_post, a_PhD, a_PhDD


'''
写入csv文件
Parameters:
        a_under - 本科专业
        a_post - 硕士专业
        a_PhD - 博士专业
        a_PhDD - 博士专业部门
'''


def writer(a_under, a_post, a_PhD, a_PhDD, university_name):
    for i in range(len(a_under)):
        with open("CaptureCourse.csv", "a", newline="", encoding="utf-8") as f:
            filename = ['University Name', 'Undergraduate', 'Postgraduate', 'PhD course', 'PhD Department']
            fp = csv.DictWriter(f, fieldnames=filename)
            fp.writerow(
                {
                    'University Name': university_name,
                    'Undergraduate': a_under[i],
                    'Postgraduate': a_post[i],
                    'PhD course': a_PhD[i],
                    'PhD Department': a_PhDD[i]
                }
            )


'''
数据写入
Parameters:
        data_under - 本科专业
        data_post - 硕士专业
        data_phd - 博士专业
        data_phdd - 博士专业部门
        university_name - 大学名称
'''


def DataOutput(data_under, data_post, data_phd, data_phdd, university_name):
    a_under, a_post, a_PhD, a_PhDD = format(data_under, data_post, data_phd, data_phdd)
    writer(a_under, a_post, a_PhD, a_PhDD, university_name)


if __name__ == '__main__':
    Aberdeen_University()
    Aberystwyth_University()
    Aston_University()
    Birkbeck()
    Brunel_University()
    Cardiff()
    City_London()
    Durham()
    Goldsmiths()
    Heriot_Watt()
    Imperial()
    Kings()
    Lancaster()
    Loughborough()
    Oxford_Brookes()
    Queen_Mary()
    Queens_Belfast()
    SOAS()
    Swansea()
    LSE()
    Edinburgh()
    UCL()
    Bath()
    Birmingham()
    Bristol()
    Cambridge()
    Dundee()
    Essex()
    Exeter()
    Glasgow()
    Kent()
    Leeds()
    Leicester()
    Liverpool()
    Manchester()
    Nottingham()
    Oxford()
    Reading()
    Sheffield()
    Southampton()
    St_Andrews()
    Stirling()
    Strathclyde()
    Surrey()
    Sussex()
    Warwick()
    York()
    Newcastle()
    Royal_Holloway()





