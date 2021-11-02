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

from bpy.types import Operator

from .backbone.bm_helper import preferences


class BM_OT_Properties(Operator):
    """to draw Information to a specific Output.

    Args:
        Operator (Operator): extends

    Returns:
        Operator: reference to the Operator.
    """

    bl_idname = "object.ot_properties"
    bl_label = "BoxMetric: Properties Panel"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        """method to execute given code when the Operator by the related Panel.

        Args:
            context (any): (read-only)properties of the area that called the method.

        Returns:
            enum: returns the result of the modal-operator
        """

        prefs = preferences(context, __file__)

        info = (f"Path: {prefs.filepath}, Number: {prefs.number}, Boolean {prefs.boolean}")

        self.report({'INFO'}, info)
        print(info)

        return {'FINISHED'}
