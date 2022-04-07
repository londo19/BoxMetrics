# BoxMetric
<sub id="top"></sub>

>## Table of Context
>+ Features
>+ <a href="#require">Requirements</a>
>+ <a href="#install">Installation</a>
>+ <a href="#use">Usage</a>
>+ <a href="#faq">FAQ's</a>
>+ <a href="#issues">Known Issues</a>
>+ <a href="#contact">Get in touch</a>
>+ <a href="#screenshots">Screenshots</a>

#

<br />

>## Features

<br />

* runs on a native Blender version.
* automatically switch between different behavior of the Transformation axes by turning on _**auto Orientation**_.
    - In any Mode other than _**Edit-Mode**_ the _"global"_ axis is being used.
    - switch automatically to _"local"_ as _**Edit-Mode**_ is being entered.
* split the active viewport _horizontally_ or _vertically_ at a factor of 50/50 using the **Pie-Menu**
* change the content of the active Viewport to any of the awailable Viewports using the **Pie-Menu**
* switch to any of the activated Workspaces from **Pie-Menu**
* In **Object-Mode** and at least one **Mesh-Object** has been created. You can _"double-click"_ this object.
    - a Panel going to be drawn in the Viewport that contains all kind of useful Information and Properties.
    - also many general properties can be changed in this Panel.
    - _see the [manual](docs/manual.md) for further Information._

#

>## Requirements <sub style="font-size:8px"><a href="#top">to top</a></sub>
<sub id="require"></sub>
<br />

+ A copy of [Blender](https://www.blender.org/download/) v2.80 or higher
+ no other Addons required
+ no third-party software required

#

>## Installation <sub style="font-size:8px"><a href="#top">to top</a></sub>
<sub id="install"></sub>
<br />

+ download [boxmetric.zip]() or clone this repository
+ open up your Blender Solution and navigate to the preferences
<br />
___Menu > Edit > Preferences___
+ in the Preference Panel navigate to the **Addons** tab on the left hand site.
+ in the upper right corner, click on the button **"install"**
+ in the upcoming dialog, navigate to the folder where you have stored [boxmetric]() in
+ select either the _boxmetric.zip_ or the _"\_\_init\_\_.py"_ and click on **Install Add-on**.
+ boxmetric is goint to be installed right away.
+ check the Status Message to verify the installation. __green msg = success | red msg = error__ 
+ after the installation succeeded the addon list will be updated and BoxMetrics is on focus
+ to activate the Addon tick the mark on the left hand side of the Addon's name
+ to open the Addon's preferences simply expand the Panel with a click on the arrow right next to the checkbox

#

>## Usage <sub style="font-size:8px"><a href="#top">to top</a></sub>
<sub id="use"></sub>

+ `Pie-Menu` <span style="font-size:10px">(default: `Ctrl+Y`)</span> : use the bound shortcut in any Viewport to open BoxMetrix's **Pie-Menu**<br />Choose from any of the contained Elements: <span style="font-size:12px">`(auto Orientation, switch Workspace, switch Viewport)`</span>
+ `Object-Panel`: In the 3D-Viewport _double-click_ on any `Mesh-Object` to open its Property-Panel.
+ `General-Panel`: is contained in the `Object-Panel`. <span style="color:yellow;">**Attention:**</span> _Access method will change in a future Update_
+ _see the [manual](docs/manual.md) for further Information._

#

>## FAQ <sub style="font-size:8px"><a href="#top">to top</a></sub>
<sub id="faq"></sub>

#

`Can I use the Addon with any of the provided objects?`
- No, the Panel will only show up on a selected object of type of `MESH`.<br /> i.e. _Cubes, Spheres, Cylinder, Planes etc.

`Will the Addon affect Blender's performance in any way?`
- No.

#

>## Known Issues <sub style="font-size:8px"><a href="#top">to top</a></sub>
<sub id="issues"></sub>

* abnormal loadtime on nested objects with unapplied bevel/subdiv modifier
* in certain situation the raycast goes through the object and hits the object behind

#

>## Contact <sub style="font-size:8px"><a href="#top">to top</a></sub>
<sub id="contact"></sub>

|  |  |
| --- | -------|
| Email | - |
| Discord | - |
| Homepage | - |

#

>## Screenshot <sub style="font-size:8px"><a href="#top">to top</a></sub>
<sub id="screenshot"></sub>
| | |
| - | - |
| Preferences View | auto Transform Orientation activated |
| <img src="/images/early_stage/active_prefs.png" width="150px" height="150"> | <img src="images/early_stage/autoOrient.png" width="150px" height="150">|
| auto Transform Orientation deactivated | Panel after double click |
| <img src="images/early_stage/no_autoOrient.png" width="150px" height="150"> | <img src="images/early_stage/panel_active.png" width="150px" height="150"> |
| some altered Properties | Blender Properties altered in Panel |
| <img src="images/early_stage/panel_changings.png" width="150px" height="150"> | <img src="images/early_stage/prop_tuning.png" width="150px" height="150"> |
| a couple viewports drawn and its content changed from Pie-Menu only | switched workspaces from Pie-Menu only |
| <img src="images/early_stage/viewport_madness.png" width="150px" height="150"> | <img src="images/early_stage/workspaces.png" width="150px" height="150"> |
