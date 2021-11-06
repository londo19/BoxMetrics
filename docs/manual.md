>|Table of Content | |
>|-|-|
>|I|some text will go here|
>|II||
>|III||
>|IV||
>|V||
>|VI||



BoxMetric uses a Pie-Menu what can be access via `ctrl + y` by default.<br>
The Pie-Menu works in any viewport and regardless of mode (object|edit).<br>
You can choose from 3 tabs to either
+ add Primitive
+ switch viewport
+ switch workspace

Simply move the mouse over the pill of your choice. The underlaying Sub-Menu will appear right away.<br>
Navigate to the item of your choice and after a last `left mouse` click on the item,<br>
the choosen feature is going to be executed in the viewport the Pie-Menu was called from.

To activate the Object Panel and all its Features you have to be in **OBJECT**- mode.<br>
Move the mouse cursor above any **MESH**- Object and double-click it with your `left mouse` button.<br>It doesn't matter if the choosen object is the current active or selected object.<br>The Object that calls the event becomes the active/ selected object anyhow.<br>
Only if the object is of a proper kind the Object-Panel will show up and you get access.<br>

You can left-click-hold on the Panel's background to drag it around.<br>
You can click, you can use slider/tabs/buttons etc. the Panel will stay active.<br>


    - alter the name
    - move to an other Collection
    - view vertex/edge/face counts of the selected object only

        _default cube with subdivision modifier level: 1_ 
        |count|physically|virtual|
        |-|-|-|
        |vertex|8|26|
        |edge|12|48|
        |face|6|24|


        | | |
        |-|-|
        |I Click|shoots a Ray from mouse position straight into the Viewport.<br />the first Object what gets hit by the Ray will be selected|
        |II Click|validates the selected Object and if it's a valid object<br />a Panel will be drawn onto the Viewport<br /> with the upper left corner originated at mouse position.