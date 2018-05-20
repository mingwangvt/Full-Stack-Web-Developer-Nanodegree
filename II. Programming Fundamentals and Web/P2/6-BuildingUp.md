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

####breakpoint
