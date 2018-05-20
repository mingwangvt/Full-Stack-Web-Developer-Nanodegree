### e. Floats
Floats are not a position value, they are a different flow on the page created by a new property, `float`.
> * Normal flow line boxes respect the boundaries of floated elements, but normal flow block elements ignore floats. (`<p>` respect floated boundaries, `<div>` ingore boundaries.)
> * Floats ingore block elements, but respect the boundaries of other float elements
#### Clearing
> Float children are not involved in the box-size calculation of normal flow parent.

There are few ways to force elements in the normal flow to respect the boundaries of floats:（不与float重合）

1. block formatting may not overlap floats. Turn the parent into a block formatting context with an `overflow` property other than `visible`.
2. Clearing: clear means they move out of the way for floats. You can control how siblings interact with floats with `clear`.
`clear:left` indicates that the top of the element must be below any left floated elements that appear before this one in the documents. 左侧不能有float
`clear: right` same as left. 右侧不能有float
`clear: none` means no restriction, default value.
`clear:both` the element must be below any bloated elements that appear earlier in the documents. 两侧都不能有floats
3. Clearfix:
> Pseudo-elements:
DOM is nutable(changeable). CSS can also mutate the DOM using something called a **pseudo-element**. A pseudo-element is an element that is actually created with CSS and then rendered like a normal element.

![pseudo elements](/assets/pseudo%20elements.jpg)

`.child:after {content: 'Pseudo-element';}`

<p>The pseudo-element is created with `:after` inside the CSS on the element that I want to mutate. Another option would be `before`.`:after` is rendered as a child of `.child` because it shares the background color of `.child` and is rendered inside the child's border. `:after` is inside the child. Without `content`, pseudo-element disappears.</p>
```html
<style>
    * {
      box-sizing: border-box;
      font-family: 'Source Sans Pro', sans-serif;
      font-weight: bold;
      font-size: 14pt;
    }
    .bordered {
      border: 2px solid #2e3d49;
    }
    /*technique 1*/
    .clearfix:after {
      content: '';    /*pseudo-element*/
      clear: both;    /*clear both sides floats*/
      display: table;  /*block formatting context*/
    }
    /*technique 2
    .clearfix {
      overflow: auto;   *block formatting context
    }
    */
    .left {
      float: left;
    }
    .parent {
      background-color: #89D0E5;
    }
    .child {
      background-color: #15A222;
    }
    .sibling {
      background-color: #D16906;
    }
  </style>
</head>
<body>
  <div class="bordered parent clearfix">
    <div class="bordered child left">Child</div>
    <div class="bordered child left">Child</div>
  </div>
  <div class="bordered sibling">Sibling to the parent</div>
</body>
```

> overflow
overflow property:`overflow`, `overflow-x`, `overflow-y`. These property determine what happens to content if its box model is larger than its parent's box model.
`visible`: default. the content is always rendered and may extend outside of its parent.
`hidden`: clips off any content that extends outside the parent's box model.
`scroll`: add scroll bars to the parent.
`auto`: depend on the browser.
