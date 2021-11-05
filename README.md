# BoxMetric
<sub id="top"></sub>

>## Table of Context
+ Features
+ <a href="#require">Requirements</a>
+ <a href="#install">Installation</a>
+ <a href="#use">Usage</a>
+ <a href="#faq">FAQ's</a>
+ <a href="#issues">known Issues</a>
+ <a href="#contact">get in touch</a>
+ <a href="#screenshots">Screenshots</a>

#



<br />

>## Features

<br />

* runs on native Blender
* let Blender decide how to calculate pivot axes by toggle on _**auto Orientation**_. <br />Blender will switch **transform Orientation** to _local_, everytime **Edit-Mode** has entered
* split the viewport and switch to any of the awailable Viewports using the **Pie-Menu**
* switch to any Workspace from **Pie-Menu**
* When in **OBJECT-Mode** and _double-click_ on any **MESH-Object** <br />you will get a Panel being drawn within the Viewport that contains all kind of useful Properties <br />which are related to the given Obejct. _see the [manual](docs\manual.md) for further Information._



#

>## Requirements <a href="#top" style="font-size:12px">to top</a>
<sub id="require"></sub>
<br />

+ A copy of [Blender](https://www.blender.org/download/) v2.80 or higher
+ no other Addons required
+ no third-party software required

#

>## Installation <a href="#top" style="font-size:12px">to top</a>
<sub id="install"></sub>
<br />

+ download [boxmetric.zip]() or clone this repository
+ open up your Blender Solution and navigate to the preferences
<br>
___Menu > Edit > Preferences___
+ in the opened Panel navigate to the **Addons** tab on the left hand site.
+ in the upper right corner, click on the button **"install"**
+ in the upcoming folder dialog, navigate to the folder where you have stored [boxmetric]() in
+ select either the _boxmetric.zip_ or the _"\_\_init\_\_.py"_ and click on **Install Add-on**.
+ boxmetric is goint to be installed right away.
+ check the Status Message to verify the installation. __green msg = success | red msg = error__ 
+ after the installation the addon list will be filtered by boxmetric
+ you will see a tiny checkbox to the left of the addon's name, tick it to activate the addon.
+ a click on the arrow right beside the checkbox will expand the addon-panel<br> to give access to the addon-settings. Here you can customize the addon to your liking.


#

>## Usage <a href="#top" style="font-size:12px">to top</a>
<sub id="use"></sub>


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

#

>## FAQ <a href="#top" style="font-size:12px">to top</a>
<sub id="faq"></sub>
<br />

#

>## Known Issues <a href="#top" style="font-size:12px;">to top</a>
<sub id="issues"></sub>

* abnormal loadtime on nested objects with unapplied bevel/subdiv modifier
* in certain situation the raycast goes through the object and hits the object behind

#

>## Contact <a href="#top" width="12px">to top</a>
<sub id="contact"></sub>

|  |  |
| --- | -------|
| Email | - |
| Discord | - |
| Homepage | - |

#

>## Screenshot <a href="#top" width="12px">to top</a>
<sub id="screenshot"></sub>
| | |
| - | - |
| <img src="images/eary_stage/active_prefs.png" width="150px" height="150"> | Preferences View |
| <img src="images/eary_stage/autoOrient.png" width="150px" height="150"> | auto Transform Orientation activated |
| <img src="images/eary_stage/no_autoOrient.png" width="150px" height="150"> | auto Transform Orientation deactivated |
| <img src="images/eary_stage/panel_active.png" width="150px" height="150"> | Panel after double click |
| <img src="images/eary_stage/panel_changings.png" width="150px" height="150"> | some altered Properties |
| <img src="images/eary_stage/prop_tuning.png" width="150px" height="150"> | Blender Properties altered in Panel |
| <img src="images/eary_stage/viewport_madness.png" width="150px" height="150"> | a couple viewports drawn and its content changed from Pie-Menu only |
| <img src="images/eary_stage/workspaces.png" width="150px" height="150"> | switched workspaces from Pie-Menu only |
