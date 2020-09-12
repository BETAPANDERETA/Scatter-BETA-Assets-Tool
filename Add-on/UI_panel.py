#-----------------------------------------------------------------------
# AUTOR: BETAPANDERETA                                                  |
# CONTACT: betaleonardo2017@gmail.com                                   |
# LICENCE: MIT                                                          |
#-----------------------------------------------------------------------

import os
import bpy

def destructorDeCol(col,pcol,prop):

    from bpy.types import WindowManager

    del WindowManager.prop

    for pcol in col.values():
        bpy.utils.previews.remove(pcol)
    col.clear()

#--------------------------------------------------------------------
#| Creando las previews para generar tupla compatible con EnumProperty|
#--------------------------------------------------------------------

def creadorDePreviews(dir,col,lista,prop):
    
    # Se recibe la información de los Props para generar las miniaturas
    # Se asegura de que la carpeta exista

      if dir and os.path.exists(dir):
        
        #Recoje las imágenes del directorio

        image_paths = []
        for fn in os.listdir(dir):
            if fn.lower().endswith(".png"):
                image_paths.append(fn)

        #Se arma la tupla que necesitan los props con EnumProperty

        for i, name in enumerate(image_paths):
            
            filepath = os.path.join(dir, name)
            icon = col.get(name)
            if not icon:
                thumb = col.load(name, filepath, 'IMAGE')
            else:
                thumb = col[name]
            lista.append((name, name, "", thumb.icon_id, i))

        col.prop = lista
        col.dir = dir
        return col.prop 

#--------------------------------------------------------------------
#| Funciones donde se recoje la información de los props de register()|
#--------------------------------------------------------------------

def generador_previews_cascos(self, context):
   
    enum_items = []

    if context is None:
        return enum_items

    wm = context.window_manager
    directorio = wm.my_previews_dir

    #Tomando la colección alojada en register()
    hcoll = preview_collections_cascos["main"]

    if directorio == hcoll.my_previews_dir:
        return hcoll.previews_cascos
    
    return creadorDePreviews(directorio,hcoll,enum_items,hcoll.previews_cascos)

def generador_previews_trees(self, context):
   
    enum_items_2 = []

    if context is None:
        return enum_items_2

    wm = context.window_manager
    directorio_2 = wm.my_previews_dir_trees

    #Tomando la colección alojada en register()
    tcoll = previews_collections_trees["main"]

    if directorio_2 == tcoll.my_previews_dir_trees:
        return tcoll.my_previews_trees

    #print("Escaneando directorio: %s" % directorio_2)
    
    return creadorDePreviews(directorio_2,tcoll,enum_items_2,tcoll.my_previews_trees) 

def generador_previews_terr(self, context):
   
    enum_items_3 = []

    if context is None:
        return enum_items_3

    wm = context.window_manager
    directorio_3 = wm.my_previews_dir_terr

    #Tomando la colección alojada en register()
    t_coll = previews_collections_terr["main"]

    if directorio_3 == t_coll.my_previews_dir_terr:
        return t_coll.my_previews_terr

    #print("Escaneando directorio: %s" % directorio_2)
    
    return creadorDePreviews(directorio_3,t_coll,enum_items_3,t_coll.my_previews_terr)

    # Llamado de operadores 

#--------------------------------------------------------------------
#|          Funciones donde se controlan los operadores             |
#--------------------------------------------------------------------

def controlOp(
            pvw,    # Previews generadas
            img,    # Nombre de la imagen del preview seleccionado
            column, # objeto tipo col de la función draw()
            model,  # Modelo a buscar en los assets
            coll    # Nombre de la colección nueva donde los assets se generan
    ):

        if pvw == img:
            prop = column.operator('view3d.link_assets',text = "IMPORT: "+model,icon='APPEND_BLEND')
            prop.model = model
            prop.colec = coll
    
def controlScat(
        pvw,    # Previews generadas
        img,    # Nombre de la imagen del preview seleccionado
        column, # objeto tipo col de la función draw()
        model,  # Modelo a buscar en los assets
    ):
        if pvw == img:
            prop = column.operator('view3d.scatter_operator',text="SCATTER", icon='EVENT_S')
            prop.model = model

#--------------------------------------------------------------------
#|                         UI PANELES                                |                
#--------------------------------------------------------------------

class PanelAddon(bpy.types.Panel):
    
    bl_label = "Scatter BETA-Assets Tool"
    bl_idname = "VIEW3D_PT_PanelAddon"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "SB-ATool"

    def draw(self, context):

        layout = self.layout
        wm = context.window_manager
        
        col = layout.column(align=True)
        col.label(text="Author: BETAPANDERETA",icon='COMMUNITY')
        col.label(text="Blender version: 2.9",icon='BLENDER')
        col.label(text="Version: 0.7.7",icon='FILE_SCRIPT')

#--------------------------------------------------------------------
#|                      Panel de previews ARBOLES                   |
#--------------------------------------------------------------------

class PanelArboles(bpy.types.Panel):
    
    bl_label = "- TREES -"
    bl_idname = "VIEW3D_PT_PanelArboles"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "SB-ATool"
    bl_parent_id = "VIEW3D_PT_PanelAddon"

    def draw(self, context):

        layout = self.layout
        wm = context.window_manager

        nom_trees_coll = "Trees"
        col = layout.column(align=True)
        col.template_icon_view(wm, "my_previews_trees",show_labels=True)

        # Opciones por imagen (Buscar manera de optimizar)

        controlOp(wm.my_previews_trees,"tree_orange.png",col,"Tree_orange",nom_trees_coll)
        controlScat(wm.my_previews_trees,"tree_orange.png",col,"Tree_orange")

        controlOp(wm.my_previews_trees,"tree_green.png",col,"Tree_green",nom_trees_coll)
        controlScat(wm.my_previews_trees,"tree_green.png",col,"Tree_green")

        controlOp(wm.my_previews_trees,"tree_pink.png",col,"Tree_pink",nom_trees_coll)
        controlScat(wm.my_previews_trees,"tree_pink.png",col,"Tree_pink")

        controlOp(wm.my_previews_trees,"tree_white.png",col,"Tree_white",nom_trees_coll)
        controlScat(wm.my_previews_trees,"tree_white.png",col,"Tree_white")

        controlOp(wm.my_previews_trees,"tree_nr.png",col,"Tree_nr",nom_trees_coll)
        controlScat(wm.my_previews_trees,"tree_nr.png",col,"Tree_nr")

#--------------------------------------------------------------------
#|                      Panel de previews TERRENO                    |
#--------------------------------------------------------------------

class PanelTerreno(bpy.types.Panel):
    
    bl_label = "- TERRAIN - LANDS -"
    bl_idname = "VIEW3D_PT_PanelTerreno"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "SB-ATool"
    bl_parent_id = "VIEW3D_PT_PanelAddon"

    def draw(self, context):

        layout = self.layout
        wm = context.window_manager
        
        nom_terr_coll = "Terrain"
        col = layout.column(align=True)

        # Opciones por imagen (Buscar manera de optimizar)

        col.template_icon_view(wm, "my_previews_terr",show_labels=True)

        controlOp(wm.my_previews_terr,"Rocks_1.png",col,"Rock_1",nom_terr_coll)
        controlScat(wm.my_previews_terr,"Rocks_1.png",col,"Rock_1")

        controlOp(wm.my_previews_terr,"Rocks_2.png",col,"Rock_2",nom_terr_coll)
        controlScat(wm.my_previews_terr,"Rocks_2.png",col,"Rock_2")

        controlOp(wm.my_previews_terr,"Rocks_pack.png",col,"Rock_pack",nom_terr_coll)
        controlScat(wm.my_previews_terr,"Rocks_pack.png",col,"Rock_pack")

        controlOp(wm.my_previews_terr,"Grass.png",col,"Grass",nom_terr_coll)
        controlScat(wm.my_previews_terr,"Grass.png",col,"Grass")

        controlOp(wm.my_previews_terr,"Terrain_1.png",col,"Terrain_1",nom_terr_coll)
        controlOp(wm.my_previews_terr,"Terrain_2.png",col,"Terrain_2",nom_terr_coll)
        controlOp(wm.my_previews_terr,"Terrain_3.png",col,"Terrain_3",nom_terr_coll)
        controlOp(wm.my_previews_terr,"Terrain_4.png",col,"Terrain_4",nom_terr_coll)

#--------------------------------------------------------------------
#|                      Panel - BONUS -                              |
#--------------------------------------------------------------------

class PanelVar(bpy.types.Panel):
    
    bl_label = "- BETA MODELS (GIFT) -"
    bl_idname = "VIEW3D_PT_PanelVar"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "SB-ATool"
    bl_parent_id = "VIEW3D_PT_PanelAddon"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):

        layout = self.layout
        wm = context.window_manager

        col = layout.column(align=True)
        col.label(
            text="- MODELS AUTHOR: BETA -",
            icon='BLENDER'
        )
        col.label(
            text="- This models are free - ",
            icon='ERROR'
        )
        col.label(
            text="- They can't be sold -",
            icon='CANCEL'
        )
        col.label(
            text="- They will not be used for commercial purposes -",
            icon='CANCEL'
        )

        nom_var_coll = "Varios" #Nombre de la colección donde se alojan los modelos obsequio
        col = layout.column(align=True)
        col.template_icon_view(wm, "previews_cascos",show_labels=True)
        controlOp(wm.previews_cascos,"emile.png",col,"Emile",nom_var_coll)
        controlOp(wm.previews_cascos,"noble.png",col,"Noble_6",nom_var_coll)

        col.label(
            text="Don't forget give me credits!",
            icon='FAKE_USER_ON'
        )

#--------------------------------------------------------------------
#|                      Panel -OPCIONES SCATTER -                    |
#--------------------------------------------------------------------

class PanelOpcionesScatter(bpy.types.Panel):
    
    bl_label = "- SCATTER OPTIONS -"
    bl_idname = "VIEW3D_PT_PanelOpcionesScatter"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "SB-ATool"
    bl_parent_id = "VIEW3D_PT_PanelAddon"

    def draw(self, context):

        layout = self.layout

        msj = " - SCATTER TOOLS - "
        col = layout.column()
        col.label(text= msj, icon='EXPERIMENTAL')

        obj = context.active_object
        part = bpy.data.particles.keys()  #Particulas en el blend file
        
        # Opciones del scatter

        act_id = [] #Lista donde recojo el nombre de las particulas ej: ParticleSettings.001
        for ids in part:
            if ids != "":
                act_id.append(ids)

        # Propiedades del SCATTER - UI PANEL

        if obj is not None and  context.object.select_get()==True:
            col = layout.column(align=True)
            
            try:
                if obj.modifiers["ParticleSettings"] is not None:  

                    col.prop(bpy.data.particles[act_id[-1]],'count',text ="Number of objects")
                    col.prop(bpy.data.particles[act_id[-1]],'size_random',text ="Size random")
                    col.prop(bpy.data.particles[act_id[-1]],'particle_size',text ="Objects size")
                    col.prop(bpy.data.particles[act_id[-1]],'rotation_factor_random',text ="Random orientation")
                    col.prop(bpy.data.particles[act_id[-1]],'rotation_mode',text ="Rotation")
                
                    col = layout.column()
                    col.operator('view3d.scatter_activator',text = "APPLY SCATTER",icon='CHECKBOX_HLT')
                    col.label(text="Once applied the Scatter it'll not be able to reverse the action",icon= 'ERROR')
                    col.label(text="Exit of the'Weight paint mode' to apply the Scatter",icon= 'ERROR')
        
            except (KeyError,IndexError):
                    pass

        #print(act_id) -----> Visualizo las particulas existentes

#--------------------------------------------------------------------
#|        Colecciones donde se guarda la info de las miniaturas      |
#--------------------------------------------------------------------

preview_collections_cascos = {}
previews_collections_trees = {}
previews_collections_terr = {}

def register():

    from bpy.types import WindowManager
    from bpy.props import (
            StringProperty,
            EnumProperty,
        )

    #Props 1ra collecion de miniaturas CASCOS

    WindowManager.my_previews_dir = StringProperty(
        subtype='DIR_PATH',
        default=os.path.join(os.path.dirname(__file__), "misc//images_var")
    )

    WindowManager.previews_cascos = EnumProperty(
        items=generador_previews_cascos,
    )
    
    #Props 2da colleción de miniaturas ARBOLES

    WindowManager.my_previews_dir_trees = StringProperty(
        subtype='DIR_PATH',
        default=os.path.join(os.path.dirname(__file__), "misc//images_trees")
    )

    WindowManager.my_previews_trees = EnumProperty(
        items=generador_previews_trees,
    )
    
    #Props 3ra colleción de miniaturas TERRENO

    WindowManager.my_previews_dir_terr = StringProperty(
        subtype='DIR_PATH',
        default=os.path.join(os.path.dirname(__file__), "misc//images_terrain")
    )

    WindowManager.my_previews_terr = EnumProperty(
        items=generador_previews_terr,
    )

    import bpy.utils.previews

    #Collección de imágenes varios

    hcoll = bpy.utils.previews.new()
    hcoll.my_previews_dir = ""
    hcoll.previews_cascos = ()
    preview_collections_cascos["main"] = hcoll

    #Colleción de imágenes árboles

    tcoll = bpy.utils.previews.new()
    tcoll.my_previews_dir_trees = ""
    tcoll.my_previews_trees = ()
    previews_collections_trees["main"] = tcoll

    #Colleción de imágenes terrenos

    t_coll = bpy.utils.previews.new()
    t_coll.my_previews_dir_terr = ""
    t_coll.my_previews_terr = ()
    previews_collections_terr["main"] = t_coll

    bpy.utils.register_class(PanelAddon)

def unregister():

    try:
        destructorDeCol(preview_collections_cascos,hcoll,previews_cascos)
        destructorDeCol(previews_collections_trees,tcoll,my_previews_trees)
    except NameError: 
        pass 
    
    bpy.utils.unregister_class(PanelAddon)
