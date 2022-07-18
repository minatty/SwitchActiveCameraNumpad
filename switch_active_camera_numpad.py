from re import S
import bpy
from bpy.types import Operator

from bpy.props import (PointerProperty)
from bpy.types import (Operator)

bl_info = {
    "name": "SwitchActiveCameraNumpad",
    "author": "minatty",
    "version": (0, 1),
    "blender": (2, 80, 0),
    "location": "View3D > View",
    "description": "Switches active camera in a scene",
    "warning": "",
    "doc_url": "",
    "category": "Scene camera",
}

def camera_poll(self, object):
    return object.type == 'CAMERA'

class InputComponent(bpy.types.PropertyGroup):
    isSwitchCameraView: bpy.props.BoolProperty(
        name="Switch camera view",
        default=False
    )

class UI_PT_Panel(bpy.types.Panel):
    bl_label = "Switch Active Camera Numpad"
    bl_category = "View"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout

        # 操作時カメラビューに切り替えるチェック
        layout.prop(context.scene.imput_component, 'isSwitchCameraView')

        # カメラ選択フォーム
        row1 = layout.row()
        # row1.alignment = 'LEFT'
        row1.label(text="Num7")
        row1.label(text="Num8")
        row1.label(text="Num9")
        row2 = layout.row(align=True)
        row2.prop_search(context.scene, 'camera_obj_Num7', context.scene, 'objects', text="")
        row2.prop_search(context.scene, 'camera_obj_Num8', context.scene, 'objects', text="")
        row2.prop_search(context.scene, 'camera_obj_Num9', context.scene, 'objects', text="")
        row3 = layout.row(align=True)
        # row3.alignment = 'LEFT'
        row3.label(text="Num4")
        row3.label(text="Num5")
        row3.label(text="Num6")
        row4 = layout.row(align=True)
        row4.prop_search(context.scene, 'camera_obj_Num4', context.scene, 'objects', text="")
        row4.prop_search(context.scene, 'camera_obj_Num5', context.scene, 'objects', text="")
        row4.prop_search(context.scene, 'camera_obj_Num6', context.scene, 'objects', text="")
        row5 = layout.row(align=True)
        # row5.alignment = 'LEFT'
        row5.label(text="Num1")
        row5.label(text="Num2")
        row5.label(text="Num3")
        row6 = layout.row(align=True)
        row6.prop_search(context.scene, 'camera_obj_Num1', context.scene, 'objects', text="")
        row6.prop_search(context.scene, 'camera_obj_Num2', context.scene, 'objects', text="")
        row6.prop_search(context.scene, 'camera_obj_Num3', context.scene, 'objects', text="")
        row7 = layout.row(align=True)
        # row7.alignment = 'LEFT'
        row7.label(text="Num0")
        row8 = layout.row(align=True)
        row8.prop_search(context.scene, 'camera_obj_Num0', context.scene, 'objects', text="")

class SwitchSceneCamera0(bpy.types.Operator):
    """シーンカメラを切り替える(Num0)"""

    bl_idname = "switch_camera.num0"
    bl_label = "switch camera (Alt + Num0)"
    bl_description = "Switch active camera (Num0)"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        switch_camera(self, 0)
        return {"FINISHED"}

class SwitchSceneCamera1(bpy.types.Operator):
    """シーンカメラを切り替える(Num1)"""

    bl_idname = "switch_camera.num1"
    bl_label = "switch camera (Alt + Num1)"
    bl_description = "Switch active camera (Num1)"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        switch_camera(self, 1)
        return {"FINISHED"}

class SwitchSceneCamera2(bpy.types.Operator):
    """シーンカメラを切り替える(Num2)"""

    bl_idname = "switch_camera.num2"
    bl_label = "switch camera (Alt + Num2)"
    bl_description = "Switch active camera (Num2)"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        switch_camera(self, 2)
        return {"FINISHED"}

class SwitchSceneCamera3(bpy.types.Operator):
    """シーンカメラを切り替える(Num3)"""

    bl_idname = "switch_camera.num3"
    bl_label = "switch camera (Alt + Num3)"
    bl_description = "Switch active camera (Num3)"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        switch_camera(self, 3)
        return {"FINISHED"}

class SwitchSceneCamera4(bpy.types.Operator):
    """シーンカメラを切り替える(Num4)"""

    bl_idname = "switch_camera.num4"
    bl_label = "switch camera (Alt + Num4)"
    bl_description = "Switch active camera (Num4)"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        switch_camera(self, 4)
        return {"FINISHED"}

class SwitchSceneCamera5(bpy.types.Operator):
    """シーンカメラを切り替える(Num5)"""

    bl_idname = "switch_camera.num5"
    bl_label = "switch camera (Alt + Num5)"
    bl_description = "Switch active camera (Num5)"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        switch_camera(self, 5)
        return {"FINISHED"}

class SwitchSceneCamera6(bpy.types.Operator):
    """シーンカメラを切り替える(Num6)"""

    bl_idname = "switch_camera.num6"
    bl_label = "switch camera (Alt + Num6)"
    bl_description = "Switch active camera (Num6)"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        switch_camera(self, 6)
        return {"FINISHED"}

class SwitchSceneCamera7(bpy.types.Operator):
    """シーンカメラを切り替える(Num7)"""

    bl_idname = "switch_camera.num7"
    bl_label = "switch camera (Alt + Num7)"
    bl_description = "Switch active camera (Num7)"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        switch_camera(self, 7)
        return {"FINISHED"}

class SwitchSceneCamera8(bpy.types.Operator):
    """シーンカメラを切り替える(Num8)"""

    bl_idname = "switch_camera.num8"
    bl_label = "switch camera (Alt + Num8)"
    bl_description = "Switch active camera (Num8)"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        switch_camera(self, 8)
        return {"FINISHED"}

class SwitchSceneCamera9(bpy.types.Operator):
    """シーンカメラを切り替える(Num9)"""

    bl_idname = "switch_camera.num9"
    bl_label = "switch camera (Alt + Num9)"
    bl_description = "Switch active camera (Num9)"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        switch_camera(self, 9)
        return {"FINISHED"}

def switch_camera(self, camera_num):
    camera_obj = getattr(bpy.context.scene, 'camera_obj_Num' + str(camera_num))
    if camera_obj is None:
        return
    bpy.context.scene.camera = camera_obj
    
    if bpy.context.scene.imput_component.isSwitchCameraView:
        bpy.context.space_data.region_3d.view_perspective = 'CAMERA'

classes = (
    SwitchSceneCamera0,
    SwitchSceneCamera1,
    SwitchSceneCamera2,
    SwitchSceneCamera3,
    SwitchSceneCamera4,
    SwitchSceneCamera5,
    SwitchSceneCamera6,
    SwitchSceneCamera7,
    SwitchSceneCamera8,
    SwitchSceneCamera9,
    InputComponent,
    UI_PT_Panel,
)

addon_keymaps = []

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    key_assign_list = [
        (SwitchSceneCamera0.bl_idname, "NUMPAD_0", "PRESS", False, True, False),
        (SwitchSceneCamera1.bl_idname, "NUMPAD_1", "PRESS", False, True, False),
        (SwitchSceneCamera2.bl_idname, "NUMPAD_2", "PRESS", False, True, False),
        (SwitchSceneCamera3.bl_idname, "NUMPAD_3", "PRESS", False, True, False),
        (SwitchSceneCamera4.bl_idname, "NUMPAD_4", "PRESS", False, True, False),
        (SwitchSceneCamera5.bl_idname, "NUMPAD_5", "PRESS", False, True, False),
        (SwitchSceneCamera6.bl_idname, "NUMPAD_6", "PRESS", False, True, False),
        (SwitchSceneCamera7.bl_idname, "NUMPAD_7", "PRESS", False, True, False),
        (SwitchSceneCamera8.bl_idname, "NUMPAD_8", "PRESS", False, True, False),
        (SwitchSceneCamera9.bl_idname, "NUMPAD_9", "PRESS", False, True, False),
    ]
    if kc:
        km = kc.keymaps.new(name="3D View", space_type="VIEW_3D")
        for (idname, key, event, ctrl, alt, shift) in key_assign_list:
            kmi = km.keymap_items.new(
                idname, key, event, ctrl=ctrl, alt=alt, shift=shift
            )
            addon_keymaps.append((km, kmi))
    for num in range(10):
        setattr(bpy.types.Scene, 'camera_obj_Num' + str(num), PointerProperty(type=bpy.types.Object, poll=camera_poll))
    bpy.types.Scene.imput_component = bpy.props.PointerProperty(type=InputComponent)
    print("SwitchActiveCamera is registered.")

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()
    for num in range(10):
        camera_obj_Num = getattr(bpy.types.Scene, 'camera_obj_Num' + str(num))
        del camera_obj_Num
    del bpy.types.Scene.imput_component
    print("SwitchActiveCamera is unregistered.")

if __name__ == "__main__":
    register()