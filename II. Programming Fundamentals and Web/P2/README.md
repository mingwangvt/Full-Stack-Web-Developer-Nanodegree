# Programming Fundamentals -- Frontend Notes

**Personal Notes for "Full Stack Web Developer Nanodegree" on Udacity [Part 2]**

### a.HTML Syntax

#### Environment
  - rich text(formatted)
  - plain text(ASCII chars)
  - IDE(Integrated Development Environment) Xcode/visual studio
  - Text Editors([**Visual Studio Code**](https://code.visualstudio.com)/ Atom Editor/ Emacs/ Vi/Vim
  - ctr+R(win)/command+R(mac) refresh browser


#### [HTML element reference](https://developer.mozilla.org/en-US/docs/Web/HTML/Element)

#### Paths

##### _Absolute Path_

Absolute path is written in relation to the computer's root directory. `/Users/cameron/Documents/file.txt`.

- Local Paths (local files)
  - "/Users/cameron/Documents/file.txt". `Users` is inside the root directory, represented by first `/`. rest directories are separated by `/`
  - Local Path can only work for your computer. If you want other people to access, then you need external path
- External Paths (External files)
  - The computer responsible for giving you a website's files is called a **server**
  - Every website is just a server with an external address, called **URL**.**clients**
  - **Protocols** for serving files: HTTP, HTTPS, etc. [Networking for Web Developers](https://www.udacity.com/course/networking-for-web-developers--ud256)
##### _Relative Paths_

How to find a path to a file from a directory that is not the root directory

```
http://labs.udacity.com/science/sciences.html
http://labs.udacity.com/science/physics/relativity.html
```

Relative path from `sciences.html` to `relativity.html`:

`<a href="physics/relativity.html">Einstein's Special Relativity</a>`

#### Constructing Links

```
<a href="https://www.udacity.com">Udacity</a>
```
- format:
  - a space between `a` and `href`
  - no space around `=`
  - no space between `href` and `>`

#### image element

```
<img src="http://udacity.github.io/fend/images/udacity.png" alt="Udacity logo">
```

display in the same line as the rest of the text

#### figure and caption

Add caption for figure

```
  <!--solution 1-->
  <img src="redwoods_state_park.jpg" alt="redwoods_state_park.jpg">
  <p>
  	Stout Memorial Grove in Jedediah Smith Redwoods State Park in 2011 by Chmee2 (Own work) GFDL or CC BY-SA 3.0, via Wikimedia Commons - <a href="https://commons.wikimedia.org/wiki/File%3AStout_Memorial_Grove_in_Jedediah_Smith_Redwoods_State_Park_in_2011_(22).JPG">Source</a>
  </p>

  <!--solution 2-->
  <figure>
  	<img src="redwoods_state_park.jpg" alt="redwoods_state_park.jpg">
  	<figcaption>
  		Stout Memorial Grove in Jedediah Smith Redwoods State Park in 2011 by Chmee2 (Own work) GFDL or CC BY-SA 3.0, via Wikimedia Commons - <a href="https://commons.wikimedia.org/wiki/File%3AStout_Memorial_Grove_in_Jedediah_Smith_Redwoods_State_Park_in_2011_(22).JPG">Source</a>
  		<!--no p tag made figure and caption close to each other; adding p tag gave more space around caption-->
  	</figcaption>
  </figure>
```

#### forms

`<form action="" method="">` tag -- parent element; `action` and `method` tell the form where and how to send the form data.

`<input>` tag:

- `<input type="text">`
- `<input type="textarea">` can use it to create a multi-line text input box
- `<input type="checkbox">`
- `<input type="radio">`
- `<input type="date">`

`<label for="name">What is your name?</lable> <input type="text" id="name">` tag -- `for` and `id` are both "name"

`<button></button>`

- `<button>I am just a button</button>`
- `<button type="submit">I am a submit button</button>`
- `<button type="reset">I am a reset button</button>`
- `<button type="button">I am a button with an image<img src="" alt=""></button>`

#### HTML structure

```
<!DOCTYPE html>      --- rending mode
<html>
  <head>             --- general information and metadata about the page  <meta> <link>
    Meta information goes here!
  </head>
  <body>
    content goes here
  </body>
</html>
```

`<head>` :
- title `<title></title>`
- css file  `<link rel="stylesheet" type="text/css" href="style.css">`
- js file `<script src="a.js"></script>`
- charset/test's encoding `<meta charset="utf-8">`
- keyword,author,description `<meta name="description" content="...">`
- "..."

---
### b.CSS Syntax

#### Comments
* CSS comments: /* CSS comments */
* HTML comments: <!--HTML comments-->

#### Attributes and Selector
can only have one **id**, but multiple **class** Fundamentals
CSS reference:
* https://css-tricks.com/almanac/
* https://developer.mozilla.org/en-US/docs/Web/CSS/Reference

#### Developer Tools
Chrome DevTools: https://developers.google.com/web/tools/chrome-devtools/

#### CSS Units
absolute vs. relative

#### CSS Color
* RGB 0-255 for R,G,B;
* Hexadecimal 00-FF for R,G,B. (00=0; FF=255)
open "inspect" in chrome, click on color square to display color picker

#### Border
![boder](/assets/boder.jpg)

#### CSS stylesheet

```CSS
<link href="path-to-stylesheet/stylesheet.css" rel="stylesheet">
```
type inside the `<head>` of HTML
`href` specifies the **path** to the linked resource, `rel` names the **relationship** between resource and your document.

### c. Sizing
#### box model
![box model](/assets/box%20model.jpg)
* box-sizing : content-box;
size = width + padding + boder
* box-sizing : border-box;
width = content-width + padding + boder
margin is outside.

#### Inline Boxes
<p>inline element cannot set height and width. It is content-based.

margin and padding can only work on horizontally, not vertically.</p>

#### Semantic Elements
```
<header></header>
<nav></nav>
<section></section>
<article></article>
```
[semantic tags reference](https://developer.mozilla.org/en-US/docs/Web/HTML/Element)

### d. Position
#### box model
------
**12 HTML syntax - 23**
