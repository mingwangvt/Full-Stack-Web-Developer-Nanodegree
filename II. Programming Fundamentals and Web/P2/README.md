# Programming Fundamentals -- Frontend Notes

**Personal Notes for "Full Stack Web Developer Nanodegree" on Udacity [Part 2]**

### a.HTML Syntax
  
- environment
  - rich text(formatted)
  - plain text(ASCII chars)
  - IDE(Integrated Development Environment) Xcode/visual studio
  - Text Editors([**Visual Studio Code**](https://code.visualstudio.com)/ Atom Editor/ Emacs/ Vi/Vim
  - ctr+R(win)/command+R(mac) refresh browser


- [HTML element reference](https://developer.mozilla.org/en-US/docs/Web/HTML/Element)

- Paths

  - Absolute Path

Absolute path is written in relation to the computer's root directory. `/Users/cameron/Documents/file.txt`

    - Local Paths (local files)
      - "/Users/cameron/Documents/file.txt". `Users` is inside the root directory, represented by first `/`. rest directories are separated by `//`
      - Local Path can only work for your computer. If you want other people to access, then you need external path
    - External Paths (External files)
      - The computer responsible for giving you a website's files is called a **server**
      - Every website is just a server with an external address, called **URL**.**clients**
      - **Protocols** for serving files: HTTP, HTTPS, etc. [Networking for Web Developers](https://www.udacity.com/course/networking-for-web-developers--ud256)
  - Relative Paths

How to find a path to a file from a directory that is not the root directory

''' 
http://labs.udacity.com/science/sciences.html
http://labs.udacity.com/science/physics/relativity.html

'''
Relative path from `sciences.html` to `relativity.html`:

'<a href="physics/relativity.html">Einstein's Special Relativity</a>'