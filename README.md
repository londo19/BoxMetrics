# BoxMetric
<sub id="top"></sub>

### Table of Context
+ Information and Description of the Addon itself and its features
+ <a href="#require">Requirements</a>
+ <a href="#install">Installation</a>
+ <a href="#use">Usage</a>
+ <a href="#faq">FAQ's</a>
+ <a href="#issues">known Issues</a>

_*a Blender Toolkit*_


> The simpliest to explain is the first one `add Primitive`.<br>
> It simply adds some of the Primitives that Blender provides to the active viewport,<br>
> except that these primitives already has a Bevel modifier added<br>
> and it set to `shade smooth` and `autosmooth 30°`.
>
> `switch viewport`: This tab contains all available views to change the active viewport to.<br>
> Blender provides the feature to split of the viewports to any depth.<br>
> But the newly created viewport inherits the view it was created from.<br>
> The BoxMetric > switch Viewport let you switch the viewport to your liking at any depth.<br>
> It also works in full screen mode _`ctrl + alt + space`_.<br>
> In which you do not even have the ability to access the default switch button.<br>
> You would have to exit the full screen mode first and look out for the  

---

<sub id="require"></sub> 
### Requirements
<a href="#top">to top</a>

+ A copy of [Blender](https://www.blender.org/download/) v2.80 or higher

<sub id="install"></sub>
### Installation
<a href="#top">to top</a>

+ download [boxmetric.zip]() and push it into Blender's default Addon path<br>or any other folder of your choice.
+ open up your Blender Solution and navigate to the preferences<br>_Menu > Edit > Preferences_
+ in the opened Panel navigate to the **Add-ons** tab on the left hand site.
+ in the upper right corner a button **Install** shows up. click on that.
+ in the upcoming folder dialog, navigate to the folder you have stored [boxmetric]() in<br> select _boxmetric.zip_ and finally click on **Install Add-on**.
+ boxmetric is goint to be installed right away.
+ after the installation the addon list will be filtered by boxmetric
+ you will see a tiny checkbox to the left of the addon's name, tick it to activate the addon.
+ a click on the arrow right beside the checkbox will expand the addon-panel<br> to give access to the addon-settings. Here you can customize the addon to your liking.

<sub id="use"></sub>
### Usage
<a href="#top">to top</a>

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
The Panel gets disabled only if one of the following triggers:

| Condition | closing state |
| --- | --- |
| `right mouse`- click | _(correctly closed)_ |
| `ESC` pushed | _(correctly closed)_ |
| `hide` button activated | _(correctly closed)_ |
| `selectable` button activated | _(correctly closed)_ |
| `cursor` leaves Panel bounds | _(aborted)_ |
| `malfunction` | _(faulty terminated)_ |


<sub id="faq"></sub>
### FAQ
<a href="#top">to top</a>

**to Do**

<sub id="issues"></sub>
### Known Issues
<a href="#top">to top</a>

* abnormal loadtime on nested objects with unapplied bevel/subdiv modifier
* in certain situation the raycast goes through the object and hits the object behind
* Scale/ Dimension slider values only gets updated when releasing the mouse button