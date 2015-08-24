---
layout: default
title: home
permalink: /
---

This will be my home page

Here is a list of articles/posts, which can be created in the \_posts subdirectory
<ul>
  {% for post in site.posts limit:5%}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a>
      {{ post.excerpt }}
    </li>
  {% endfor %}
</ul>

Edited through the web by Andy, far too late on Tuesday night, then demo'd to Peter.
