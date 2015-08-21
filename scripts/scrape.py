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



def run():
    r = requests.get('http://www.thameshareandhounds.org.uk/reports.php')
    tree = lxml.html.fromstring(r.text)

    for report_link in tree.cssselect(".leader_text a")[0:2]:

        rel = report_link.get("href")
        if not rel.startswith('/reports.php'):
            continue
        print rel

        report_url = "http://www.thameshareandhounds.org.uk" + rel



        r2 = requests.get(report_url)
        tree2 = lxml.html.fromstring(r2.text)

        #all stories
        content = tree2.cssselect("td div.story_text")[0]

        snippet = lxml.html.tostring(content)


        #Each one starts with e.g. <a name=1234></a>
        snippets = snippet.split("<hr>")
        print "    %d snippets" % len(snippets)
        for snippet in snippets:

            print "========"
            print snippet
            print "========="
            post = lxml.html.fromstring(snippet)

            anchors = post.cssselect('a')
            if anchors:
                print "        id: %s" % anchors[0].get('name')

            # story_id = story.cssselect('a')[0].get('name')
            headline = post.cssselect('div.report_headline')[0]
            print "        headline: %s" % headline
            # title, date_text = headline.split('-')

            # title = title.strip()
            # dd, mm, yyyy = date_text.strip().split("/")
            # dd = int(dd)
            # mm = int(mm)
            # yyyy = int(yyyy)

            # isodate = yyyy + '-' + mm + '-' + dd

            # print "        %s: %s" % (isodate, title)



if __name__=='__main__':
    run()