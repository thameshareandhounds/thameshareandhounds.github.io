"""

Here's an inner story we want to parse.

<a name=1631></a>
<div class=report_headline>Last Friday 5km Race, Hyde Park - 26/6/15</div>
<div class=leader_text>
    <p>In sweltering conditions, Simon Molden finished second in the June Last Friday 5km Race in Hyde Park in a time of 16.49.
    <p>
</div>
<hr>
"""


import os
import sys
import lxml.html
import requests
from bs4 import BeautifulSoup
from pprint import pprint

def run():
    r = requests.get('http://www.thameshareandhounds.org.uk/reports.php')
    tree = lxml.html.fromstring(r.text)

    for report_link in tree.cssselect(".leader_text a")[0:5]:

        rel = report_link.get("href")
        if not rel.startswith('/reports.php?month='):
            continue
        print rel

        report_url = "http://www.thameshareandhounds.org.uk" + rel


        r2 = requests.get(report_url)
        print "retrieved %d bytes" % len(r2.text)






        soup = BeautifulSoup(r2.text, "lxml")
        print "soup is brewing"



        section = soup.find('div', 'story_text')
        print section

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

        continue





        tree = lxml.html.fromstring(r2.text)

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

        print "page has %d posts" % len(output)
        for post in output:
            d = post['date']
            filename = "%s-post.html" % d.isoformat()

            filecontent = """---
            layout: post
            title: %(title)s
            ---

            %(body)s

            """ % (body)

            open(filename, 'w').write(filecontent)
            print "saved", filename

        # tree2 = lxml.html.fromstring(r2.text)

        # #all stories
        # content = tree2.cssselect("td div.story_text")[0]

        # snippet = lxml.html.tostring(content)

        # print snippet
        # continue


        # #Each one starts with e.g. <a name=1234></a>
        # snippets = snippet.split("<hr>")
        # print "    %d snippets" % len(snippets)
        # for snippet in snippets:

        #     print "========"
        #     print snippet
        #     print "========="
        #     post = lxml.html.fromstring(snippet)

        #     anchors = post.cssselect('a')
        #     if anchors:
        #         print "        id: %s" % anchors[0].get('name')

        #     # story_id = story.cssselect('a')[0].get('name')
        #     headline = post.cssselect('div.report_headline')[0]
        #     print "        headline: %s" % headline
        #     # title, date_text = headline.split('-')

        #     # title = title.strip()
        #     # dd, mm, yyyy = date_text.strip().split("/")
        #     # dd = int(dd)
        #     # mm = int(mm)
        #     # yyyy = int(yyyy)

        #     # isodate = yyyy + '-' + mm + '-' + dd

        #     # print "        %s: %s" % (isodate, title)



if __name__=='__main__':
    run()