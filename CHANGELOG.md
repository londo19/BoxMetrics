# Change Log

### [Version 0.0.0.686]()

### Feature added

> - restructure and sorting Panel features depending its relation
> - **props**: transform orientation selectbox
> - **props**: transform pivot point selectbox
> - **props**: viewport shading selectbox
> - **operator**: object origin selectbox
> - **props**: object snap to selectbox
> - added more content to the README

### Bug fixes

> * hidden objects have been took into account on double click
> * alter loc/rot/scale/dim of the selected object did not affect Blender's state
> * scale factor calculation was not carried out on the new dimensions
> * selectboxes were expanded by default

---

### [Version 0.0.0.659]()

### Feature added

> - added License Information
> - Object Information Panel Structure and placeholder
> - **panel**: if object is "unselectable" and you try to double click it<br>
  an ask-panel will show up to ask whether you want to activate the object or not.
> - **info**: vert/edge/face count for selected object
> - **props**: object location slider
> - **props**: object rotation slider
> - **props**: object scale slider
> - **props**: object dimension slider

### Bug fixes

> - **autosmooth**: switch of state did not correspond to Blender's state
> - **hide**: object hide(hotkey:H) feature called a wrong operator
> - **collection** list: the list have not been updated after an object was moved to an other collection
> - **material list**: list only stated materials assigned to the active object 

---

### [Version 0.0.0.423]()

### Initialize Tool

* __new Pie-Menu__
>  - **Primitives** Sub-Menu to choose a primitive you want to add
>  - **workspace** Sub-Menu to switch among your workspaces.<br>
>  <sub style="font-size:13px">
_*it relates on the Blender's activated Top-Header-Tabs*_
</sub>
>  - **views** Sub-Menu to switch among all possible viewports at any workspace<br>and regardless the depth of separated viewports
>  - **Double-Click** event for the 3D-Viewport that gets activated only under limited conditions.
</div>