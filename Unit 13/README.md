# Watch this video
[ArcGIS API for JavaScript: Getting Started](https://www.youtube.com/watch?v=pYHWoSNsSIU)

# Check out ArcGIS JSAPI Samples
[ArcGIS API for JavaScript Sample Code](https://developers.arcgis.com/javascript/latest/sample-code/)

# Learn JS using Esri Hackerlabs
These have not been updated in three or four years, but they used to be awesome. [Check out
the hackerlabs](https://github.com/Esri/geodev-hackerlabs)

# CodePen.io
If you continue with the Advanced course next semester, you will learn JavaScript.
We will use [CodePen.io](https://codepen.io/) as a tool to write and test code.

# Web Mapping Development Intro

Jacob Wasilkowski

[Twitter @JWasilGeo](https://twitter.com/JWasilGeo)

[https://jwasilgeo.github.io](https://jwasilgeo.github.io)

## Intro to HTML, CSS, and JavaScript

What's the purpose of each and how do they work together?

READ :clap: THE :clap: DOCS :clap:

[https://developer.mozilla.org/en-US/docs/Web](https://developer.mozilla.org/en-US/docs/Web)

## JavaScript: syntax intro

```javascript
// variable declaration
let myString;

// and then later assignment
myString = 'sample string';

// variable declaration and assignment at same time
let myNumber = 90210;

console.log(myNumber - 90209); // simple math

// strings
let question = 'Is pizza awesome?';
let answer = 'Without a doubt.';
let qAndA = question + ' ' + answer; // concatenate strings

console.log(qAndA);

// format with template strings
console.log(`${question} ${answer}`);

// booleans
console.log(1.5 === 1.5); // true
console.log(1 + 1 === 3); // false

// arrays
let myArray = [1, 2, 3, 'x', 'y', 'z'];

console.log(myArray[3]);

myArray.push(100);

let stringFromArray = myArray.join(' and ');

console.log(stringFromArray);

// functions
let sumThreeNumbers = function(a, b, c) {
  // do something with the function arguments
  console.log(a, b, c);
  // return the sum
  return a + b + c;
};

// objects
let myObject = {
  name: 'Greg',
  totalCats: 15,
  faveLanguages: ['Python', 'JavaScript'],
  isInCharge: true,
  tellMeSomethingInteresting: function() {
    return this.name + ' has ' + this.totalCats + ' cats.'
  }
};

console.log(myObject.name);

console.log(myObject.tellMeSomethingInteresting());

// conditional statements
let whatHappened;
if (1 === 2) {
  whatHappened = 'bad math';
} else if (true && false) {
  whatHappened = 'bad logic';
} else {
  whatHappened = 'we got to the "else!"';
}
console.log(whatHappened);
```

**Start thinking in terms of user interaction _"events"_ instead of top-to-bottom script execution.**

Obligatory JS meme

![JS meme](https://pbs.twimg.com/media/B-SjB7XIcAAoOzU.jpg)

## HTML and CSS and JavaScript

**Exercise:** create `index.html` page, insert `<script>` tag, and try out the [Chrome developer tools](https://developer.chrome.com/devtools).

  ```html
  <!DOCTYPE html>
  <html>

  <head>
    <title>Title for browser tab.</title>

    <style>
      /* this is a CSS comment */

      .green {
        color: green;
        /* color: rgb(0, 128, 0); */
        /* color: #008000; */
      }

      .italic-sans-serif {
        font-style: italic;
        font-family: sans-serif;
      }
    </style>
  </head>

  <body>
    <!-- this is an HTML comment -->

    <h1>
      Hello, World! (I'm an "h1" element).
    </h1>

    <h2>
      Subtitle (I'm an "h2" element).
    </h2>

    <p>
      Hello, World! (I'm a "p" element.)
    </p>

    <p class="green">
      Hello, World! (I'm a "p" element with a CSS class.)
    </p>

    <div>
      This is a "div" element.
    </div>

    <div class="green italic-sans-serif">
      This is a "div" with several CSS classes.
    </div>

    <a href="https://www.slu.edu/arts-and-sciences/earth-atmospheric-sciences/" target="_blank">
      This is a link that will open in another window.
    </a>

    <p>
      Next are a "button" element followed by a "p" element, both of which are inside of a "div" element.
    </p>

    <div>
      <button id="coolButton">
        Increase the "clickCount" JavaScript variable.
      </button>

      <p id="clickCountDisplay"></p>
    </div>

    <script>
      // this is a JavaScript comment

      let coolButtonReference = document.querySelector('#coolButton');

      let clickCountDisplayReference = document.querySelector('#clickCountDisplay');

      let clickCount = 0;

      clickCountDisplayReference.innerText = clickCount;

      coolButton.addEventListener('click', function () {
        console.log('Hey, I got clicked!');

        clickCount = clickCount + 1;
        // another way to write the same command would be:
        // clickCount += 1;

        console.log('clickCount: ', clickCount);

        clickCountDisplayReference.innerText = clickCount;
      });
    </script>
  </body>

  </html>
  ```

## Let's get mappy in the browser

- Intros to [ArcGIS API for JavaScript](https://js.arcgis.com) and [LeafletJS](https://leafletjs.com/)

- Getting started with [CodePen](https://codepen.io)

  - Why? Your browser will block functionality if browsing files directly from hard drive. You must use a web server. CodePen is interactive and easy to experiment with, just like Python Notebooks.

- **Leaflet exercise**

  1. Copy and paste the contents of `leaflet-demo.html` into a new CodePen.

  2. Set the map's initial position to be centered at and zoomed to St. Louis.

  3. Change the basemap to a [different Esri basemap](https://esri.github.io/esri-leaflet/api-reference/layers/basemap-layer.html).

  4. Add a ["marker" positioned at SLU](https://leafletjs.com/examples/quick-start/#markers-circles-and-polygons) onto the map.

- **Esri exercise**

  1. Copy and paste the contents of `esri-demo.html` into a new CodePen.

  2. Make the Esri demo into 3D! You can instruct the code to use a [`SceneView`](https://developers.arcgis.com/javascript/latest/api-reference/esri-views-SceneView.html) instead of a `MapView`.

## Resources

- ["Maps in JS" presentation by Gavin Rehkemper](https://github.com/gavinr/presentations/tree/master/src/maps-in-js)

- [ArcGIS API for JavaScript](https://js.arcgis.com)

- [LeafletJS](https://leafletjs.com/) (and optionally the [Esri-Leaflet plugin](https://esri.github.io/esri-leaflet/))

- ["JavaScript: The Good Parts", Douglas Crockford (2008)](http://lib.slu.edu/)
  - A must-read which will go by quickly! It is available at SLU Libraries...you don't really have a good excuse to avoid this book.

- [The Modern JavaScript Tutorial](https://javascript.info/)

- [JavaScript for Cats](http://jsforcats.com/) :cat2: :cat: :cat2:

- [Mozilla Dev Network: JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

- [Mozilla Dev Network: A re-introduction to JavaScript (JS tutorial)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/A_re-introduction_to_JavaScript)

- [DevDocs.io](https://devdocs.io/)


# Optional Unit 13 Assignment
This is optional, but the students who complete it
tell me that they got a lot out of it. If you want to learn more about Javascript and the 
ArcGIS JSAPI, complete the following two lessons:
1. [Create a starter app](https://developers.arcgis.com/javascript/latest/display-a-map/)
2. [Add layers to a map](https://developers.arcgis.com/javascript/latest/add-a-feature-layer/)

Copy and past the code into text files and submit the text files.
