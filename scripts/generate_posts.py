import os
import sys
from datetime import date
import MySQLdb
import string

OUTDIR = "../_posts"

TEMPLATE = """---
layout: post
title: "%s"
---

<p class="summary">%s</p>

"""

ALLOWED = string.lowercase + string.digits

def slugify(title):

    maxlen = 40
    length = 0
    out = []
    for word in title.lower().split():
        newword = ''
        for char in word:
            if char in ALLOWED:
                newword += char
        if newword:
            length += len(newword) + 1
            if length > maxlen:
                break
            out.append(newword)
    return '-'.join(out)


def run():
    conn = MySQLdb.connect(user="root", db="thames")

    cur = conn.cursor()

    cur.execute("select * from report order by report_id desc")

    data = cur.fetchall()
    print 'retrieved %d reports' % len(data)

    for (report_id, title, summary, body, updated) in data:

        filename = '%s-%s.html' % (updated, slugify(title))
        fullpath = os.path.join(OUTDIR, str(updated.year), filename)

        f = open(fullpath, 'w')
        content = TEMPLATE % (title, summary)

        if body:
            content += ("""

            <div class="body">
            %s
            </div>
            """ % body)
        f.write(content)
        f.close()
        print filename
if __name__=='__main__':
    run()