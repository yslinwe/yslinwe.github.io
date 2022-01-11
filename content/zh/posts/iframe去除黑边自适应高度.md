---
title: "iframe去除黑边自适应高度"
summary: iframe去除黑边自适应高度
date: 2022-01-11
tags: ["iframe"]
author: "YSL"
draft: false
weight: 2
---

方法出处：https://css-tricks.com/fluid-width-video/

html

```html
<main>
  <p>A video!</p>
  <iframe width="560" height="315" src="https://www.youtube.com/embed/Vbg81kc56FU" frameborder="0"
    allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
  <p>That YouTube iframe is responsive via FitVids.js</p>
</main>
```
css

```css
main {
  background: white;
  height: 100vh;
  max-width: 400px;
  margin: 0 auto;
  padding: 1rem;
}

.fitVids-wrapper {
  position: relative;
  padding-bottom: 56.25%;
  height: 0;
}
.fitVids-wrapper iframe {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}

body {
  margin: 0;
  background-color: #eee;
  background-image: url('data:image/svg+xml,%3Csvg width="52" height="26" viewBox="0 0 52 26" xmlns="http://www.w3.org/2000/svg"%3E%3Cg fill="none" fill-rule="evenodd"%3E%3Cg fill="%239C92AC" fill-opacity="0.4"%3E%3Cpath d="M10 10c0-2.21-1.79-4-4-4-3.314 0-6-2.686-6-6h2c0 2.21 1.79 4 4 4 3.314 0 6 2.686 6 6 0 2.21 1.79 4 4 4 3.314 0 6 2.686 6 6 0 2.21 1.79 4 4 4v2c-3.314 0-6-2.686-6-6 0-2.21-1.79-4-4-4-3.314 0-6-2.686-6-6zm25.464-1.95l8.486 8.486-1.414 1.414-8.486-8.486 1.414-1.414z" /%3E%3C/g%3E%3C/g%3E%3C/svg%3E');
}
```

js

```js
// Vanilla version of FitVids
// Still licencened under WTFPL
//
// Not as robust and fault tolerant as the jQuery version.
// It's BYOCSS.
// And also, I don't support this at all whatsoever.

(function(window, document, undefined) {
  "use strict";

  // List of Video Vendors embeds you want to support
  var players = ['iframe[src*="youtube.com"]', 'iframe[src*="vimeo.com"]'];

  // Select videos
  var fitVids = document.querySelectorAll(players.join(","));

  // If there are videos on the page...
  if (fitVids.length) {
    // Loop through videos
    for (var i = 0; i < fitVids.length; i++) {
      // Get Video Information
      var fitVid = fitVids[i];
      var width = fitVid.getAttribute("width");
      var height = fitVid.getAttribute("height");
      var aspectRatio = height / width;
      var parentDiv = fitVid.parentNode;

      // Wrap it in a DIV
      var div = document.createElement("div");
      div.className = "fitVids-wrapper";
      div.style.paddingBottom = aspectRatio * 100 + "%";
      parentDiv.insertBefore(div, fitVid);
      fitVid.remove();
      div.appendChild(fitVid);

      // Clear height/width from fitVid
      fitVid.removeAttribute("height");
      fitVid.removeAttribute("width");
    }
  }
})(window, document);
```

