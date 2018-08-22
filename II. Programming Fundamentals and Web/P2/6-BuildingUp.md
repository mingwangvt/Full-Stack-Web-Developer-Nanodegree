###Building Up
####Adding a Basic Media Query
`<link rel="stylesheet" href="style.css">`
`<link rel="stylesheet" media="screen and (min-width: 500px)" href="over500.css>"`
second style only applys when the screen is over than 500px.

Another way to add media query:
`@media screen and (min-width: 500px) {
  body {background: red;}
}`
`@media screen and (min-width: 400px) and (max-width: 600px) {
  body {background: green;}
}`

* Compare two ways:
  * linked CSS: many small files, but many HTTP requests.
  * @media: fewer requests, but files tend to be bigger.

#### 12 complex media queries
```
@media screen and (min-width: 500px) and (max-width: 600px) {
  .yes {
    Opacity: 1;
  }
  .no {
    Opacity: 0;
  }
}
```
#### 13 what style are applied
```
@media screen and (max-width: 400px) {}
@media screen and (min-width: 301px) and (max-width: 600px) {}
@media screen and (min-width: 601px) {}
@media screen and (min-width: 961px) {}
```

#### 16 flexbox container
```
// css style, div with class “container” will shrink with window.
.container {
  Display: flex;
}
 
// css style, div with class “container” will wrap with window, and only shrink when really needs to.
.container {
  Display: flex;
  Flex-wrap: wrap;
}
```


#### 17 flex item
```
	// .dark_blue, .light_blue…the class name of div with different colors.
	@ media screen and (min-width: 700px) {
		.dark_blue {order: 4;}
		.light_blue {order: 5;}
		.green {order: 2;} …
	}
```

#### 18 deconstructing a flexbox layout
```
	<style>
	.container {
		Display: flex;
		Flex-wrap: wrap;
	}
	.dark_blue { width: 100%; order: 1;}
	.light_blue {width: 50%; order: 2;}…
	</style>
	 
	<body>
		<div class=“container”>
			<div class=”box dark_blue”></div>
			<div class=”box light_blue”></div>…
		</div>
	</body>
```

#### 19 deconstructing a flexbox layout
Width: 100; order: 0;
Width: 33; order: 1; width: 33; order: 2; width: 33; order: 3;
Width: 50; order: 4; width: 50; order: 5
Width: 100; order: 6;
** order do not need to be consistant.

#### 15 common responsive pattern
- 1 intro to patterns
![intro to patterns](/assets/intro_to_patterns.png)
- 2 pattern-column drop
![pattern-column drop](/assets/pattern_column_drop.png)
![pattern-column drop code](/assets/pattern_column_drop_code.png)
- 3 Pattern-mostly fluid
![mostly fluid](/assets/mostly_fluid.png)

####breakpoint
