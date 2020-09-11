#-----------------------------------------------------------------------
# AUTOR: BETAPANDERETA                                                  |
# CONTACT: lbetancurd@unal.edu.co                                       |
# LICENCE: MIT                                                          |
#-----------------------------------------------------------------------

bl_info = {
    "name" : "Scatter BETA-Assets Tool",
    "author" : "BETAPANDERETA <betaleonardo2017@gmail.com>",
    "description" : "This add-on incorporates +21 assets made by me, also includes a Scatter tool",
    "blender" : (2, 90, 0),
    "version" : (0, 7, 7),
    "location" : "VIEW 3D > UI",
    "warning" : "If you find any bug let me know please",
    "category" : "Scattering-Assets-Manager"
}

import bpy
from . UI_panel import *
from . operadores import ExportarAssets
from . operadores import ScatterOperator
from . operadores import ScatterActivator

def register():

    UI_panel.register()
    bpy.utils.register_class(ExportarAssets)
    bpy.utils.register_class(ScatterOperator)
    bpy.utils.register_class(ScatterActivator)
    bpy.utils.register_class(PanelArboles)
    bpy.utils.register_class(PanelTerreno)
    bpy.utils.register_class(PanelVar)
    bpy.utils.register_class(PanelOpcionesScatter)

def unregister():

    UI_panel.unregister()
    bpy.utils.unregister_class(ExportarAssets)
    bpy.utils.unregister_class(ScatterOperator)
    bpy.utils.unregister_class(ScatterActivator)
    bpy.utils.unregister_class(PanelArboles)
    bpy.utils.unregister_class(PanelTerreno)
    bpy.utils.unregister_class(PanelVar)
    bpy.utils.unregister_class(PanelOpcionesScatter)

if __name__ == "__main__":
    register()
