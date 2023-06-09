
name = ""

# create node


# multiply divide
_mult_divide = cmds.createNode("multiplyDivide", n=name+"_mult_divide")
cmds.setAttr(_mult_divide+".operation", 2)
cmds.setAttr(_mult_divide+".input2X", 2)
cmds.connectAttr(control_+".Twist", _mult_divide+".input1X")
cmds.connectAttr(_mult_divide+".outputX", group_+".rotateX")

# create curve and connect to ribbon
crv_from_rbn_iso = cmds.createNode("curveFromSurfaceIso", n=name+"_curve_from_surface_iso")
cmds.connectAttr(ribbon[0] + "Shape.worldSpace[0]", crv_from_rbn_iso + ".inputSurface", force=1)
ribbon_crv = cmds.createNode("nurbsCurve", n=name+"_length_curve")
ribbon_crv_transform = cmds.listRelatives(ribbon_crv, p=1)
cmds.parent(ribbon_crv_transform, systems_grp)
cmds.connectAttr(crv_from_rbn_iso+".outputCurve", ribbon_crv+".create", force=1)
cmds.setAttr(crv_from_rbn_iso+".isoparmValue", 0.5)

# floatmath
ribbon_length_const_to_abs_pow2 = cmds.createNode("floatMath", n=name+"_length_to_abs_pow2")
cmds.setAttr(ribbon_length_const_to_abs_pow2+".operation", 6)
cmds.connectAttr(ribbon_length_const+".outFloat", ribbon_length_const_to_abs_pow2+".floatA")
cmds.setAttr(ribbon_length_const_to_abs_pow2+".floatB", 2)


# blendcolors
bl_colors_IK_FK_volume_switch = cmds.createNode("blendColors", n=name+"_IK_FK_blend_colors_volume_switch")
cmds.setAttr(bl_colors_IK_FK_volume_switch+".color2", 1, 0, 0, type="double3")
cmds.setAttr(bl_colors_IK_FK_volume_switch+".blender", 1)
cmds.connectAttr(mult_divide_scale+".outputX", bl_colors_IK_FK_volume_switch+".color1R", force=1)
cmds.connectAttr(bl_colors_IK_FK_volume_switch+".outputR", bl_colors_volume_switch+".color1R", force=1)

bl_colors_ribbon_length = cmds.createNode("blendColors", n=ribbon_length_dist_btw+"_blend_colors")
cmds.setAttr(bl_colors_ribbon_length+".blender", 0.4)
cmds.setAttr(bl_colors_ribbon_length+".color1", 1, 0, 0, type="double3")
cmds.setAttr(bl_colors_ribbon_length+".color2", 1, 0, 0, type="double3")
cmds.connectAttr(ribbon_length_mult_divide+".outputX", bl_colors_ribbon_length+".color2R")
cmds.connectAttr(bl_colors_ribbon_length+".outputR", tw_ctrl_mid_extra_grp+".scaleX")

# condition

