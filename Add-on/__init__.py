#-----------------------------------------------------------------------
# AUTOR: BETAPANDERETA                                                  |
# CONTACT: lbetancurd@unal.edu.co                                       |
# LICENCE: (POR DEFINIR)                                                |
#-----------------------------------------------------------------------

bl_info = {
    "name" : "Scatter BETA-Assets Tool",
    "author" : "BETAPANDERETA <lbetancurd@unal.edu.co>",
    "description" : "Este Add-on sirve para generar ambientes con assets de mi autoria",
    "blender" : (2, 82, 0),
    "version" : (0, 7, 5),
    "location" : "VIEW_3D > UI",
    "warning" : "Este Add-on está en cosntrucción, puede tener algunos bugs",
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
