"""
    This file is part of BoxMetrics.

    BoxMetrics is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    BoxMetrics is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with BoxMetrics.  If not, see <https://www.gnu.org/licenses/>.        
"""

import bpy
from bpy.props import EnumProperty
from bpy.types import AddonPreferences

from .backbone.bm_config import BM_ConfigManager

from .backbone.bm_helper import package_name, preferences, rebuildTuple, updateProp
from .backbone.bm_general_prefs import BM_GeneralPrefs
from .backbone.bm_pie_prefs import BM_PiePrefs


class BM_Properties(AddonPreferences, BM_PiePrefs, BM_GeneralPrefs):
    """BoxMetric Preferences to be add to Blender->Properties->Addon list

    Args:
        AddonPreferences (AddonPreferences): Blender Addon Preferences declaration
        BM_PropsVisible (PropertyGroup): BoxMetric's definition of visible Properties
        BM_PropsHidden (PropertyGroup): BoxMetric's definition of hidden Properties

    Returns:
        UILayout: Property Panel modifiable Properties
    """

    bl_idname = package_name(__file__)
    
    # retrieve all necessary data from the config file
    cm = BM_ConfigManager()
    _bm_prefs = preferences(bpy.context, __file__)
    #bm_prop_tabs = rebuildTuple(cm.config['GLOBAL']['ds_PropertyTabs'])
    #bm_pie_items = rebuildTuple(cm.config['GLOBAL']['ds_PieItems'])

    bm_prop_tabs = [
        ("GENERAL", "General", "", "",1),
        ("SCENE", "Scene", "","",2),
        ("OBJECT", "Object", "","",3),
        ("PIE", "Pie-Menu", "","",4)
    ]
    bm_pie_items = [
        ("vp", "bm_viewport", "show/hide Dropdown in Pie-Menu", "", 1),
        ("ws", "bm_workspaces", "show/hide Dropdown in Pie-Menu", "", 2)
    ]

    BM_PropTabsEnum:EnumProperty(
        items=bm_prop_tabs
    )
    BM_PieItems: EnumProperty(
        items=bm_pie_items,
    )

    def draw(self, context):
        """Method to display certian Information in a formatted manner.

        Args:
            context (any): (read-only)properties of the area that called the method.
        """


        
        # define the layout
        layout = self.layout
        row = layout.row()
        row.prop_tabs_enum(self, "BM_PropTabsEnum")
        row = layout.row()

        # draw certain Information depending on the active Tab
        if self.BM_PropTabsEnum == 'GENERAL':
            boxG = row.box()
            boxG.label(text="General Properties:")

            self.__fillGeneralPanel(boxG)

        elif self.BM_PropTabsEnum == 'SCENE':
            boxS = row.box()
            boxS.label(text="Scene Properties:")

            self.__fillScenePanel(boxS)

        elif self.BM_PropTabsEnum == 'OBJECT':
            boxO = row.box()
            boxO.label(text="Object Properties")

            self.__fillObjPanel(boxO)

        else:
            boxP = row.box()
            boxP.label(text="Pie-Menu Properties")

            self.__fillPiePanel(boxP)


    def __fillGeneralPanel(self, parent):
        """adding 'GENERAL' Information to the Panel

        Args:
            parent (UILayout): the layout on which to bind the Elements
        """
        parent.prop(self, "bm_ui_mode", expand=False)
        rowG = parent.row()

        col1 = rowG.column(align=False)
        col1.label(text="Ray Distance")
        col1.label(text="Transform Orientation")

        col2 = rowG.column(align=True)
        col2.prop(self, "bm_blength", text="General")
        col2.prop(self, "bm_autoOrientation", text="auto Orientation")


    def __fillScenePanel(self, parent):
        """adding 'SCENE' Information to the Panel

        Args:
            parent (UILayout): the layout on which to bind the Elements
        """
        row1 = parent.row()
        self.__fillProps(row1, "bm_ui_mode", **{'param':'expand', 'value':False})
        self.__fillProps(row1, "bm_blength", **{'param':'text', 'value':'Irgendwas'})


    def __fillObjPanel(self, parent):
        """adding 'OBJECT' Information to the Panel

        Args:
            parent (UILayout): the layout on which to bind the Elements
        """
        row1 = parent.row()

        self.__fillProps(row1, "bm_ui_mode", **{'param':'expand', 'value':False})
        self.__fillProps(row1, "bm_blength", **{'param':'text', 'value':'Irgendwas'})
        

    def __fillPiePanel(self, parent):
        """adding 'PIE-MENU' Information to the Panel

        Args:
            parent (UILayout): the layout on which to bind the Elements
        """
        row1 = parent.row()

        self.__fillProps(row1, "bm_viewports")
        self.__fillProps(row1, "bm_workspaces")



    def __fillProps(self, item, props, param=None, value=None):
        """Helper method to draw properties with a different set of parameter

        Args:
            item (SubLayout): Element to bind the property to
            props (string): Identifier of the property.
            param (string, optional): parameter definition. Defaults to None.
            value (any, optional): parameter related value. Defaults to None.

        Returns:
            [type]: [description]
        """
        if param == None:
            return item.prop(self, props)
        elif param == "text":
            return item.prop(self, props, text=value)
        elif param == "expand":
            return item.prop(self, props, expand=value)
        else:
            return None