---
layout: default
title: home
permalink: /
---

<h2>Welcome!</h2>
<p>Based on Wimbledon Common in South West London, Thames Hare and Hounds is the oldest cross-country running club in the world. Our large membership is made up of runners of all ages and abilities. We enjoy a full program of training, racing and social events, at all of which newcomers are very welcome. To find out more about us click <a href="/about/">here</a>.</p>

<ul>
  {% for post in site.posts limit:5 %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a>
      {{ post.excerpt }}
    </li>
  {% endfor %}
</ul>

<h2>Feedback please!</h2>

Please use the <a href="http://forum.thh.run/">forum</a> to give us feedback on the site.

<h2>Upcoming events</h2>
<iframe src="https://www.google.com/calendar/embed?title=TH%26H%20Diary&amp;showTitle=0&amp;showNav=0&amp;showDate=0&amp;showPrint=0&amp;showTabs=0&amp;showCalendars=0&amp;showTz=0&amp;mode=AGENDA&amp;height=400&amp;wkst=2&amp;bgcolor=%23FFFFFF&amp;src=6ohhd97kchnlsu9krcgj11gj53tmb74v%40import.calendar.google.com&amp;color=%23000000&amp;src=pvg9cp9i5qa2oq22ctr5lrh4foubns7q%40import.calendar.google.com&amp;color=%23000000&amp;ctz=Europe%2FLondon" style=" border-width:0 " width="800" height="400" frameborder="0" scrolling="no"></iframe>
