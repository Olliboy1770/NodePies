bl_info = {
    "name": "NodePies",
    "author": "Olliboy",
    "version": (0, 3),
    "blender": (2, 80, 0),
    "location": "Shader Editor > W",
    "description": "Adds pie menus for adding nodes more quickly.",
    "warning": "",
    "doc_url": "",
    "category": "Node",
}


import bpy
from bpy.types import Menu, Operator
import time

time.sleep(3)



# node types --------------------------------------------------------------------

class addAO(bpy.types.Operator):
    """Add An Ambient Occlusion Node"""
    bl_idname = "ext.add_ao"
    bl_label = "Ambient Occlusion"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        bpy.ops.node.add_node(type="ShaderNodeAmbientOcclusion")
        return bpy.ops.node.translate_attach_remove_on_cancel('INVOKE_DEFAULT')
    
class addMath(bpy.types.Operator):
    """Add A Math Node"""
    bl_idname = "ext.add_math"
    bl_label = "Math"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        bpy.ops.node.add_node(type="ShaderNodeMath")
        return bpy.ops.node.translate_attach_remove_on_cancel('INVOKE_DEFAULT')
    
class addVMath(bpy.types.Operator):
    """Add A Vector Math Node"""
    bl_idname = "ext.add_v_math"
    bl_label = "Vector Math"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        bpy.ops.node.add_node(type="ShaderNodeVectorMath")
        return bpy.ops.node.translate_attach_remove_on_cancel('INVOKE_DEFAULT')

class addColorRamp(bpy.types.Operator):
    """Add A ColorRamp Node"""
    bl_idname = "ext.add_cr"
    bl_label = "ColorRamp"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        bpy.ops.node.add_node(type="ShaderNodeValToRGB")
        return bpy.ops.node.translate_attach_remove_on_cancel('INVOKE_DEFAULT')

class addGradient(bpy.types.Operator):
    """Add A Gradient Texture Node"""
    bl_idname = "ext.add_gradient"
    bl_label = "Gradient Texture"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        bpy.ops.node.add_node(type="ShaderNodeTexGradient")
        return bpy.ops.node.translate_attach_remove_on_cancel('INVOKE_DEFAULT')
    
class addNoiseTex(bpy.types.Operator):
    """Add A Noise Texture Node"""
    bl_idname = "ext.add_noise_tex"
    bl_label = "Noise Texture"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        bpy.ops.node.add_node(type="ShaderNodeTexNoise")
        return bpy.ops.node.translate_attach_remove_on_cancel('INVOKE_DEFAULT')
    
class addImgTex(bpy.types.Operator):
    """Add An Image Texture Node"""
    bl_idname = "ext.add_img_tex"
    bl_label = "Image Texture"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        bpy.ops.node.add_node(type="ShaderNodeTexImage")
        return bpy.ops.node.translate_attach_remove_on_cancel('INVOKE_DEFAULT')
    
class addPrinBSDF(bpy.types.Operator):
    """Add A Principled BSDF Node"""
    bl_idname = "ext.add_prin_bsdf"
    bl_label = "Principled BSDF"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        bpy.ops.node.add_node(type="ShaderNodeBsdfPrincipled")
        return bpy.ops.node.translate_attach_remove_on_cancel('INVOKE_DEFAULT')
    
class addSepXYZ(bpy.types.Operator):
    """Add A Separate XYZ Node"""
    bl_idname = "ext.add_sep_xyz"
    bl_label = "Separate XYZ"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        bpy.ops.node.add_node(type="ShaderNodeSeparateXYZ")
        return bpy.ops.node.translate_attach_remove_on_cancel('INVOKE_DEFAULT')
    
class addSepRGB(bpy.types.Operator):
    """Add A Separate RGB Node"""
    bl_idname = "ext.add_sep_rgb"
    bl_label = "Separate RGB"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        bpy.ops.node.add_node(type="ShaderNodeSeparateRGB")
        return bpy.ops.node.translate_attach_remove_on_cancel('INVOKE_DEFAULT')
    
class addObjInfo(bpy.types.Operator):
    """Add An Object Info Node"""
    bl_idname = "ext.add_obj_info"
    bl_label = "Object Info"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        bpy.ops.node.add_node(type="ShaderNodeObjectInfo")
        return bpy.ops.node.translate_attach_remove_on_cancel('INVOKE_DEFAULT')  
    
class addHueSat(bpy.types.Operator):
    """Add A Hue/Saturation Node"""
    bl_idname = "ext.add_hue_sat"
    bl_label = "Hue Saturation Value"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        bpy.ops.node.add_node(type="ShaderNodeHueSaturation")
        return bpy.ops.node.translate_attach_remove_on_cancel('INVOKE_DEFAULT')   

class addCombXYZ(bpy.types.Operator):
    """Add A Combine XYZ Node"""
    bl_idname = "ext.add_comb_xyz"
    bl_label = "Combine XYZ"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        bpy.ops.node.add_node(type="ShaderNodeCombineXYZ")
        return bpy.ops.node.translate_attach_remove_on_cancel('INVOKE_DEFAULT')   

class addBump(bpy.types.Operator):
    """Add A Bump Node"""
    bl_idname = "ext.add_bump"
    bl_label = "Bump"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        bpy.ops.node.add_node(type="ShaderNodeBump")
        return bpy.ops.node.translate_attach_remove_on_cancel('INVOKE_DEFAULT')  

class addNMap(bpy.types.Operator):
    """Add A Normal Map Node"""
    bl_idname = "ext.add_n_map"
    bl_label = "Normal Map"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        bpy.ops.node.add_node(type="ShaderNodeNormalMap")
        return bpy.ops.node.translate_attach_remove_on_cancel('INVOKE_DEFAULT')
    
class addMapRange(bpy.types.Operator):
    """Add A Map Range Node"""
    bl_idname = "ext.add_map_range"
    bl_label = "Map Range"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        bpy.ops.node.add_node(type="ShaderNodeMapRange")
        return bpy.ops.node.translate_attach_remove_on_cancel('INVOKE_DEFAULT')
    
class addDisplacement(bpy.types.Operator):
    """Add A Displacement Node"""
    bl_idname = "ext.add_dis"
    bl_label = "Displacement"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        bpy.ops.node.add_node(type="ShaderNodeDisplacement")
        return bpy.ops.node.translate_attach_remove_on_cancel('INVOKE_DEFAULT')
    
#------------------------------------------------------------------------------
    
   
class open_node_Pie1(bpy.types.Operator):
    """Open The NodePie Menu"""
    bl_idname = "ext.open_pie1"
    bl_label = "Open Menu"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        bpy.ops.wm.call_menu_pie(name="OBJECT_MT_node_Pie")
        print(1353412)
        return {'FINISHED'}   
   
   
    
    
class open_node_Pie2(bpy.types.Operator):
    """Open The Secondary NodePie Menu"""
    bl_idname = "ext.open_pie2"
    bl_label = "Open Secondary Menu"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        bpy.ops.wm.call_menu_pie(name="OBJECT_MT_node_Pie2")
        print(135341)
        return {'FINISHED'}


    
       







class node_Pie(Menu):
    bl_idname = "OBJECT_MT_node_Pie"
    bl_label = "Add Node"

    def draw(self, context):
        layout = self.layout

        pie = layout.menu_pie()
        # operator_enum will just spread all available options
        # for the type enum of the operator on the pie
        pie.operator("ext.add_math")
        pie.operator("ext.add_v_math")
        
        pie.operator("ext.open_pie2")
        
        pie.operator("ext.add_cr")
        pie.operator("ext.add_gradient")  
        pie.operator("ext.add_noise_tex")
        pie.operator("ext.add_sep_rgb")
        pie.operator("ext.add_sep_xyz")
        

class node_Pie2(Menu):
    bl_idname = "OBJECT_MT_node_Pie2"
    bl_label = "Add Node"

    def draw(self, context):
        layout = self.layout

        pie = layout.menu_pie()

        #pie.operator("ext.add_ao")
        pie.operator("ext.add_n_map")        
        pie.operator("ext.add_img_tex")            
        pie.operator("ext.add_obj_info")
        pie.operator("ext.add_hue_sat")
        pie.operator("ext.add_comb_xyz")
        pie.operator("ext.add_map_range")
        pie.operator("ext.add_dis")
        pie.operator("ext.add_bump")
        

from bpy.utils import register_class, unregister_class

classes = [
node_Pie,
node_Pie2,
open_node_Pie1,
open_node_Pie2,


addAO,
addMath,
addVMath,
addColorRamp,
addGradient,
addNoiseTex,
addImgTex,
addPrinBSDF,
addSepXYZ,
addSepRGB,
addObjInfo,
addHueSat,
addCombXYZ,
addBump,
addNMap,
addMapRange,
addDisplacement
]

addon_keymaps = []

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
        
  
    
    # Add the hotkey
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        km = wm.keyconfigs.addon.keymaps.new(name='Node Editor', space_type='NODE_EDITOR')
        kmi = km.keymap_items.new(open_node_Pie1.bl_idname, type='W', value='PRESS')
        addon_keymaps.append((km, kmi))




def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
        
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()


if __name__ == "__main__":
    register()

    #bpy.ops.wm.call_menu_pie(name="node_Pie")

