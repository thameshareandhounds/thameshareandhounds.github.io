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
