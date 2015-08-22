from pprint import pprint
import lxml.html
from bs4 import BeautifulSoup
from datetime import date
def parse():
    src = open('months/201506_raw.html').read()
    soup = BeautifulSoup(src, "lxml")
    print "soup is brewing"



    section = soup.find('div', 'story_text')


    anchors = section.findAll('a')
    titles = section.findAll('div', 'report_headline')
    bodies = section.findAll('div', 'leader_text')


    output = []
    for i in range(len(anchors)):
        post = {}
        post['id'] = anchors[i]['name']

        headline = titles[i].string
        title, txtdate = headline.split(' - ')
        post['title'] = title

        d,m,y = txtdate.strip().split("/")
        d = int(d)
        m = int(m)
        y = int(y)
        post['title'] = title.strip()
        post['date'] = date(y,m,d)




        output.append(post)

    pprint(output)
    return

    tree = lxml.html.fromstring(src)

    reports = tree.cssselect("div.story_text")[0]

    print len(reports)

    output = []
    post = {}
    for child in reports:
        if child.tag == 'a':
            post['id'] = child.get("name")
        elif child.tag == 'div':
            klass = child.get("class")
            if klass == 'report_headline':
                headline = child.text
                title, txtdate = headline.split(' - ')
                post['title'] = title

                d,m,y = txtdate.strip().split("/")
                d = int(d)
                m = int(m)
                y = int(y)
                post['title'] = title.strip()
                post['date'] = date(y,m,d)

            elif klass == 'leader_text':
                buf = []
                for grandchild in child:
                    buf.append(lxml.html.tostring(grandchild).strip())
                post['body'] = ''.join(buf)
        elif child.tag == "hr":
            output.append(post)
            post = {}
        

    if post:
        output.append(post)
   
    pprint(output)

    # print lxml.html.tostring(reports, pretty_print=True)

if __name__=='__main__':
    parse()