# Web Mapping Development Intro

April 2018

Jacob Wasilkowski, [https://jwasilgeo.github.io](https://jwasilgeo.github.io)

## Intro to HTML, CSS, and JavaScript

What's the purpose of each and how do they work together?

Developers are lazy (_supposedly!_). Here's a link to save us some time: [https://developer.mozilla.org/en-US/docs/Web](https://developer.mozilla.org/en-US/docs/Web)

## JavaScript: syntax intro

```javascript
// variable declaration
var myString;

// and then later assignment
myString = 'sample string';

// variable declaration and assignment at same time
var myNumber = 90210;

console.log(myNumber - 90209); // simple math

// strings
var question = 'Is pizza awesome?';
var answer = 'Without a doubt.';
var qAndA = question + ' ' + answer; // concatenate strings

console.log(qAndA);

// booleans
console.log(1.5 === 1.5); // true
console.log(1 + 1 === 3); // false

// arrays
var myArray = [1, 2, 3, 'x', 'y', 'z'];

console.log(myArray[3]);

myArray.push(100);

var stringFromArray = myArray.join(' and ');

console.log(stringFromArray);

// functions
var sumThreeNumbers = function(a, b, c) {
  // do something with the function arguments
  console.log(a, b, c);
  // return the sum
  return a + b + c;
};

// objects
var myObject = {
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
var whatHappened;
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

- **Hands on:** create index.html page, insert `<script>` tag, and play with [Chrome developer tools](https://developer.chrome.com/devtools) and the `console.log();` method

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

      .italic-sans-serif-text {
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

    <h2 class="green">
      Hello, World! (I'm an "h2" element with a CSS class.)
    </h2>

    <div>
      This is a "div" element.
    </div>

    <div class="green italic-sans-serif-text">
      This is a "div" with several CSS classes.
    </div>

    <a href="http://www.slu.edu/peoplefinder/index.php?query=brunner#FacStaff" target="_blank">
      This is a link that will open in another window.
    </a>

    <div>
      Here is a "button" element inside of a "div" element.
      <button id="coolButtonID">
        Increase the clickCount variable.
      </button>
    </div>

    <script>
      // this is a JavaScript comment

      var clickCount = 0;

      var aRandomPhrase = 'I really want a slice of pizza.';

      console.log(aRandomPhrase);

      var coolButton = document.getElementById('coolButtonID');

      coolButton.addEventListener('click', function() {
        console.log('Hey, I got clicked!');

        clickCount = clickCount + 1;
        // another way to write the same command would be:
        // clickCount += 1;

        console.log('clickCount: ', clickCount);
      });
    </script>
  </body>

  </html>
  ```

## Let's get mappy in the browser

- Intros to [ArcGIS API for JavaScript](https://js.arcgis.com) and [LeafletJS](http://leafletjs.com/)

- **Hands on:** getting started with [JS Bin](https://jsbin.com)

  - Why? Your browser will block functionality if browsing files directly from hard drive. You must use a web server. JS Bin is interactive and easy to experiment with, just like Python Notebooks.

- **Challenge:**

  - change the map's initial position to be centered & zoomed to St. Louis

  - change the basemap

- **Hands on:** add a "feature layer" to the web map

- **Challenge:** make it 3D! Super easy with [`SceneView`](https://developers.arcgis.com/javascript/latest/api-reference/esri-views-SceneView.html).

## :octocat: GitHub Pages

GitHub can host your [project website](https://help.github.com/categories/github-pages-basics/) in each repo. You can go from :weary: to :sunglasses: in no time.

## Resources

- [ArcGIS API for JavaScript](https://js.arcgis.com)

- [ArcGIS Geodev Hackerlabs](https://github.com/Esri/geodev-hackerlabs)

- [LeafletJS](http://leafletjs.com/) (and optionally the [Esri-Leaflet plugin](http://esri.github.io/esri-leaflet/))

- ["JavaScript: The Good Parts", Douglas Crockford (2008)](http://lib.slu.edu/)
  - A must-read which will go by quickly! It is available at SLU Libraries...you don't really have a good excuse to avoid this book.

- [JavaScript for Cats](http://jsforcats.com/) :cat2: :cat2: :cat2:

- [Mozilla Developer Network: JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

- [DevDocs.io](https://devdocs.io/)
