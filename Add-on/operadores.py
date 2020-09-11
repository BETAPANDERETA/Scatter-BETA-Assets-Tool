#-----------------------------------------------------------------------
# AUTOR: BETAPANDERETA                                                  |
# CONTACT: lbetancurd@unal.edu.co                                       |
# LICENCE: MIT                                                          |
#-----------------------------------------------------------------------

import bpy
import os

#--------------------------------------------------------------------
#|                       Funciones de los operadores                  |
#--------------------------------------------------------------------

def append_assets(file,model,nom_coll):

    assets = os.path.join(os.path.dirname(__file__), "assets//"+file+"\Collection")
    bpy.ops.wm.append(filename=model,directory=assets) # Traigo el objeto del .blend file de "assets"
    esc = bpy.context.view_layer.active_layer_collection  # Obtengo la colección activa en el outliner 

    # Miro si existe alguna colección con el nombre de model, sino existe la creo 

    try : 
        nueva_col = esc.collection.children[nom_coll]
    except KeyError:
        nueva_col = bpy.data.collections.new(nom_coll)
        esc.collection.children.link(nueva_col) # La colección nueva se añade a la colección activa

    # Colección a remover

    coll_from = bpy.data.collections[model] # Colección importada de BETA_Assets.blend
    name = coll_from.name                   # Nombre de la colleción para que el operador Scatter sepa con que hacer el Scatter

    # Traslando la colección a nueva_col

    for col in bpy.data.collections:

        if col == coll_from:
            new_col = coll_from.copy()
            new_col.name = name
            nueva_col.children.link(new_col)
    
    bpy.data.collections.remove(coll_from) # Quito la collección 
    
def scatterTool(particula):

    # Info. de objetos  seleccionados

    objName = bpy.context.object.name
    obj = bpy.data.objects[objName]
    vert_g = obj.vertex_groups.new(name = "Grupo "+objName) #Creo un vertex group
    esc = bpy.context.scene                                 # Obteniendo la escena ("Scene")

    vert_grup =  obj.vertex_groups.keys() # Lista de los vertex group creados
    vert = ""                             # Donde se almacenan los nombres vertex group

    for v in vert_grup:                   
        vert = v

    bpy.ops.object.particle_system_add()  

    values_list = obj.particle_systems.values() # Lista de particles agregadas
    id_part_list = list(bpy.data.particles)
                    
    for val in   values_list:
        
        val.vertex_group_density = vert
                     
    for part in id_part_list:

        #print(part)
        #part.name +="_"+str(objName)
        part.type = 'HAIR'
        part.render_type = 'COLLECTION'
        
        #Valores predefinidos
        try:
            part.instance_collection = bpy.data.collections[particula]  #Objetos de particulas
        except KeyError:
            print("No existe instancia")
        part.size_random = .5                    # Variacion de escala
        part.particle_size =.5                   # Tamaño de particula
        part.count = 10                          # Cantidad de particulas inicial
        part.use_advanced_hair = True            # Opciones avanzadas de rotación
        part.use_rotations = True                # Orientación de objetos activada
        part.rotation_mode = 'GLOB_Z'            # Orientación en Z
        
    bpy.ops.paint.weight_paint_toggle()
    esc.tool_settings.unified_paint_settings.weight = 0.5

#--------------------------------------------------------------------
#|                              Operadores                           |
#--------------------------------------------------------------------

class ExportarAssets(bpy.types.Operator):

    bl_idname = "view3d.link_assets"
    bl_label = "Link assets"
    bl_description = "Connect the assets with the current blend file"

    model: bpy.props.StringProperty(default=" ") #Prop que recoje el nombre del modelo que se instancia
    colec: bpy.props.StringProperty(default=" ") #Prop que recoje el nombre de la colección donde se guardan las instancias

    def execute(self, context):
        
        append_assets("BETA_assets.blend",self.model,self.colec)
        print("Model imported: "+self.model)

        return {'FINISHED'}

class ScatterOperator(bpy.types.Operator):

    bl_idname = "view3d.scatter_operator"
    bl_label = "Scatter Tool"
    bl_description = "Activate the Scattering mode"

    model: bpy.props.StringProperty(default=" ") #Prop que recoje el nombre del modelo que se instancia
    
    @classmethod
    def poll(cls, context):
      return context.active_object is not None and  context.object.select_get()==True  and context.object.type == 'MESH'

    def execute(self, context):
        
        scatterTool(self.model)

        return {'FINISHED'}

class ScatterActivator(bpy.types.Operator):

    bl_idname = "view3d.scatter_activator"
    bl_label = "Scatter Tool"
    bl_description = "Apply the Scatter, once applied it'll not be able to reverse the action"

    @classmethod
    def poll(cls, context):
      return context.active_object is not None and  context.object.select_get()==True  and context.object.type == 'MESH'

    def execute(self, context):

        try: 
            bpy.ops.object.duplicates_make_real()
            bpy.ops.object.particle_system_remove()
        except RuntimeError:
             
            print("To apply the Scatter, go to OBJECT MODE")
            self.report({'WARNING'},"To apply the Scatter, go to OBJECT MODE")
            return {'CANCELLED'}
        
        return {'FINISHED'}