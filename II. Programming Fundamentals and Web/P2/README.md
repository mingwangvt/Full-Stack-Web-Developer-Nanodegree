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

**12 HTML syntax - 20**
