# Web Mapping Development Intro

25 April 2017

Jacob Wasilkowski, Esri

[https://jwasilgeo.github.io](https://jwasilgeo.github.io)

## Intro to HTML, CSS, and JavaScript

- What's the purpose of each and how do they work together?

- Devs are lazy (_supposedly_), here's a link: [https://developer.mozilla.org/en-US/docs/Web](https://developer.mozilla.org/en-US/docs/Web)

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

- **Important**: start thinking in terms of user interaction **"events"**, instead of _just_ top-to-bottom script execution.

- Obligatory JS meme pic:

  ![](https://pbs.twimg.com/media/B-SjB7XIcAAoOzU.jpg)

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
     .bigger-sans-serif-text {
       font-size: 15pt;
       font-family: sans-serif;
     }
    </style>
  </head>

  <body>
    <!-- this is an HTML comment -->

    <h1>Hello, World!</h1>

    <h2>Hello, World!</h2>

    <div>This is "div".</div>

    <div class="green bigger-sans-serif-text">This is "div" with several CSS classes".</div>

    <a href="http://www.slu.edu/peoplefinder/index.php?query=brunner#FacStaff" target="_blank">This is a link that will open in another window.</a>

    <script>
      // this is a JS comment
    </script>
  </body>
  </html>
  ```

## Let's get mappy in the browser

- Intro to [ArcGIS API for JavaScript](https://js.arcgis.com)

- Walk through code in ["Get started with MapView - Create a 2D map"](https://developers.arcgis.com/javascript/latest/sample-code/get-started-mapview/index.html)

- **Hands on:** getting started with [JS Bin](https://jsbin.com)
  - Why? Your browser will block functionality if browsing files directly from hard drive. You must use a web server. JS Bin is interactive and easy to experiment with, just like Python Notebooks.

- **Challenge:**
  - change web map to be centered on and zoomed in to St. Louis
  - change the basemap

- **Hands on:** work with HTML layout elements and CSS to create a floating "title" and a "side panel"

- **Hands on:** add a "feature layer" to the web map

- **Challenge:** make it 3D! Super easy with [`SceneView`](https://developers.arcgis.com/javascript/latest/api-reference/esri-views-SceneView.html).

## Finale :octocat:

- Did you know? GitHub can host your [project website](https://help.github.com/articles/user-organization-and-project-pages/#project-pages) in each repo. You can go from :weary: to :sunglasses: in no time.

## Resources

- [ArcGIS API for JavaScript](https://js.arcgis.com)

- [ArcGIS Geodev Hackerlabs](https://github.com/Esri/geodev-hackerlabs)

- ["JavaScript: The Good Parts"](http://ezp.slu.edu/login?url=http://search.ebscohost.com/login.aspx?direct=true&db=cat00825a&AN=slu.b3608207&site=eds-live), Douglas Crockford (2008).
  - A must-read which will go by quickly! It is available at SLU Libraries...you don't really have a good excuse to avoid this book.

- [JavaScript for Cats](http://jsforcats.com/) :cat2: :cat2: :cat2:

- [Mozilla Developer Network: JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

- [DevDocs.io](http://devdocs.io/)
