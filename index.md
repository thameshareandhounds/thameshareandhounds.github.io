---
layout: default
title: home
permalink: /
---

<h2>Welcome!</h2>
<p>Based on Wimbledon Common in South West London, Thames Hare and Hounds is the oldest cross-country running club in the world. Our large membership is made up of runners of all ages and abilities. We enjoy a full program of training, racing and social events, at all of which newcomers are very welcome. To find out more about us click here.</p>

Here is a list of articles/posts, which can be created in the \_posts subdirectory
<ul>
  {% for post in site.posts limit:5 %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a>
      {{ post.excerpt }}
    </li>
  {% endfor %}
</ul>

Edited through the web by Andy, far too late on Tuesday night, then demo'd to Peter.
