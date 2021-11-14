# Change Log

##### [Version 0.0.756]()

>## `Feature added`

  - added auto Orientation to Pie-Menu and as settable property
  - added Tabs to the Panel to group related properties tab-wise
  - added groups of properties that mirrors built-in property Panels.
  - added split functionality to the Pie-Menu.<br />Ability to split the Viewport from Pie-Menu, horizontally and vertically by the factor of _0.5_.
  - added a new Tab structure to the `Object-Panel`
    + all properties with a direct relation to the _selected object_ are grouped under a single Tab.
    + start to transfer each section of the Property-Panel into the Tab system

>## `Bug fixes`

- none

>## `Removed`
  - Submenu from Pie-Menu that created default Primitives to the Scene
  - additional Information Panel from the function tree
  - removed `Tabs_Menu` from the Object-Panel that was responsible to group properties


#

##### [Version 0.0.686]()

>## `Feature added`

- restructure and sorting Panel features depending its relation
- **props**: transform orientation selectbox
- **props**: transform pivot point selectbox
- **props**: viewport shading selectbox
- **operator**: object origin selectbox
- **props**: object snap to selectbox
- added more content to the README

>## `Bug fixes`

* hidden objects have been took into account on double click
* alter loc/rot/scale/dim of the selected object did not affect Blender's state
* scale factor calculation was not carried out on the new dimensions
* selectboxes were expanded by default

#

##### [Version 0.0.659]()

>## `Feature added`

- added License Information
- Object Information Panel Structure and placeholder
- **panel**: if object is "unselectable" and you try to double click it<br />
  you will be questioned whether to activate the object or not.
- **info**: vert/edge/face count for selected object
- **props**: object location slider
- **props**: object rotation slider
- **props**: object scale slider
- **props**: object dimension slider

>## `Bug fixes`

- **autosmooth**: switch of state did not correspond to Blender's state
- **hide**: object hide(hotkey:H) feature called a wrong operator
- **collection** list: the list have not been updated after an object was moved to an other collection
- **material list**: list only stated materials assigned to the active object 

#

##### [Version 0.0.423]()
>## `Initialize Tool`

* __new Pie-Menu__
- **Primitives** Sub-Menu to choose a primitive you want to add
- **workspace** Sub-Menu to switch among your workspaces.<br>
<sub style="font-size:13px">
_*it relates on the Blender's activated Top-Header-Tabs*_
</sub>
- **views** Sub-Menu to switch among all possible viewports at any workspace<br>and regardless the depth of separated viewports
- **Double-Click** event for the 3D-Viewport that gets activated only under limited conditions.
