**Personal Notes for "Full Stack Web Developer Nanodegree" on Udacity [Part 2-2]**
### d. Position
#### Normal Flow
position is static, which called normal flow. The `relative`, `absolute`, `fixed` flows are variations of normal flow.
* inline element cannot set height and width. It is content-based.Margin and padding can only work on horizontally, not vertically.

* inline-block: can be sized like block elements, but are laid out like inline elements.

#### Anonymous Box
tabs, space and newlines in HTML can actually become elements. The resulting elements are called "Anonymous boxes".
Eg: Two inline-block div with a with of 50% do not display on the same line.
```css
.child {
  display: inline-block;
  width: 50%
}
```
```HTML
<div class="container">
  <div class="child">Child 1</div>
  <div class="child">Child 2</div>
</div>
```
is rendered differently than this:
```HTML
<div class="container">
  <div class="child">Child 1</div><div class="child">Child 2</div>
</div>
```
because of the whitespace, newline and tab, between the `.child` elements is turned into an anonymous box.
Anonymous boxes aries in situation where there is a mix of block and inline elements inside a container. In the example, the whitespace is turned into an inline element between two `.child`s.

****************
|      | Relative           | Absolute           | Fixed              |
|:---- |:------------------ |:------------------ |:------------------ |
| When | After normal  flow | Before normal flow | Before normal flow |
| Positional relative to...       | Position in normal flow       | parent       | viewport       |

#### relative flow
The relative flow allows you to shift the position after they've been laid out in the normal flow.

> Trick for finding any element by its selector with developer tools.
>> 1.open console panel
>> 2.type `$('selector')` or `$('.className')` or `$('#idName')`.
>> 3.The elements should appear in the console, right-click and select _reveal in elements panel_.

#### 3D websites
`z-index` to control the stacking order of overlapping elements on differnt layers.
* **Document** is another name for entire DOM. The entire page.
* **window** is the visible portion of the DOM. **viewport**

#### fixed flow
Fixed Position
`position: fixed`, `top`, `bottom`, `left`, `right` indicate a position within the **viewport**. Eg: navigation menus move with scrolling the page. `top:0; left:0;`.

#### absolute flow
`position: absolute` is positioned relative to its parent **before** the rest of the normal flow occurs.(relative flow is **after** other normal flow)
> `position: absolute;` is the last choice. It is good to know, but it is rarely your best positioning option.
> `transform: translate` is a more advanced CSS property.

#### inline formating
font defines a _text-top_, _text-bottom_, _baseline_. These are used to calculate the height of the line boxes.
* `text-align` for horizontal alignment;
  - `direction: ltr`: left to right
  - `direction: rtl`: right to left; set for languages that are read from right to left.
  - justify` keep left and right edges nicely alighed (rarely used online).
  - `left`, `right`, `center`.
* `vertical-aligh` for vertical alignment.

------
15 Position - 15 Inline Formating
