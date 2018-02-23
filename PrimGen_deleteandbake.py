import maya.cmds as cmds

sel_obj = cmds.ls(sl=True, l=True)

cmds.undoInfo(ock=True)

if sel_obj:

    output_o = []

    for i in sel_obj:
        if cmds.nodeType(i) == 'transform':
            shape_obj = cmds.listRelatives(i, s=True)
            if shape_obj:
                for s in shape_obj:
                    conn_obj = cmds.listConnections(s, sh=True, d=True, s=False)
                    for c in conn_obj:
                        if cmds.nodeType(c) == 'primitiveGenerator':
                            conn_mesh_obj = cmds.listConnections(c, d=True, s=False)

                            cmds.setAttr(c + '.baseMeshDisplayOverride', False)

                            for co in conn_mesh_obj:
                                output_o.append(co)

                        cmds.delete(c)

            cmds.select(output_o, r=True)

cmds.undoInfo(cck=True)
