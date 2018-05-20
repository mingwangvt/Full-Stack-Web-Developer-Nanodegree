###Starting Small
####Pixels
* Hardware Pixels：显示设备（电脑、手机）的尺寸大小
* Device Independent Pixels (DIP): 网页开发时设计的网页大小, 类似 CSS px，DIP和CSS pixel之间的换算在viewport中定义.
* device pixel ratio (DPR): hardware pixels / DIP, on one dimension.
* The viewport (the area to display page) and device pixel ratio are likely to cause for the differences between devices.

`<meta name="viewport" content="width=device-width, initial-scale=1">`
* `name="viewport"`tell we know what we are doing
* `content="width=device-width` instructs the page to match the screen's width in device independent pixels. Allow the page to reflow content to match the screen sizes.
* `inital-scale`定义了DIP和CSS pixel之间的比例, without inital-scale=1, some browser will keep the page width when rotating to landscape mode(屏幕旋转). They scale the content rather than reflow.

####Max-width
fit the content within viewport to avoid horizontal scrolling.
```CSS
img, embed, object, video {
  max-width: 100%;
}
```

####Tap Target Sizes
48px x 48px
40px between two tap target.
`min-width: 48px;`
`min-height: 48px;`
simply use `width`,`height` is a little dangerous, because button cannot resize if the content inside of it is bigger than the container.

####Start small
* Good to know what are prioritize content, what are important on screen.
* focus on performance from the beginning.

> `padding: 1.5em inherit;`
1.5 times of text font size. inherit is the **left** and **right** padding, it's inheriting the padding from the item that is its container.
