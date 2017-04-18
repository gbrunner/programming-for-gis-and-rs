# Web Mapping Development

25 April 2017

Jacob Wasilkowski, Esri

[https://jwasilgeo.github.io](https://jwasilgeo.github.io)

## The grand plan!

- Intro to HTML, JS, CSS; what's the purpose of each and how do they work together?

- HTML: basic "index.html" page sections and elements
  - `<head>`
  - `<body>`
  - `<style>`
  - `<script>`
  - `<div>`
  - `<a>`

- JS: syntax introduction
  - `var` declarations
  - strings
  - numbers
  - booleans
  - arrays (_think: python list_)
  - objects (_think: python dict_)
  - functions/methods
  - if, else if, else blocks

- Important: start thinking in terms of user interaction **"events"**, instead of _just_ top-to-bottom script execution.

  ![](https://pbs.twimg.com/media/B-SjB7XIcAAoOzU.jpg)

- **Hands on:** create index.html page, insert `<script>` tag, and play with [Chrome developer tools](https://developer.chrome.com/devtools) and the `console.log();` method

- Intro to [ArcGIS API for JavaScript](https://js.arcgis.com)

- Walk through code in ["Get started with MapView - Create a 2D map"](https://developers.arcgis.com/javascript/latest/sample-code/get-started-mapview/index.html)

- **Hands on:** getting started with [JS Bin](https://jsbin.com)
  - Why? Your browser will block functionality if browsing files directly from hard drive. You must use a web server. JS Bin is interactive and easy to experiment with, just like Python Notebooks.

- **Challenge:** change web map to be centered on and zoomed in to St. Louis; change the basemap

- **Hands on:** work with HTML layout elements and CSS to create a floating "title" and a "side panel"

- **Hands on:** add a "feature layer" to the web map

- **Challenge:** make it 3D! Super easy with [`SceneView`](https://developers.arcgis.com/javascript/latest/api-reference/esri-views-SceneView.html).

- Discuss [`gh-pages` branches](https://pages.github.com/) in Github repos.

## Resources

- [ArcGIS API for JavaScript](https://js.arcgis.com)

- [ArcGIS Geodev Hackerlabs](https://github.com/Esri/geodev-hackerlabs)

- ["JavaScript: The Good Parts"](http://ezp.slu.edu/login?url=http://search.ebscohost.com/login.aspx?direct=true&db=cat00825a&AN=slu.b3608207&site=eds-live), Douglas Crockford (2008).
  - A must-read which will go by quickly! It is available at SLU Libraries...you don't really have a good excuse to avoid this book.

- [Mozilla Developer Network: JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

- [DevDocs.io](http://devdocs.io/)
