"""

    Snaps the selected curves to a target mesh

"""

import maya.cmds as cmds
import maya.api.OpenMaya as om


def snap_curve_to_object(geo_name=None):
    """

    :param geo_name:
    :return:
    """

    if not geo_name or not cmds.objExists(geo_name):
        cmds.warning("Invalid target geo given...")
        return

    # Construct mFn mesh
    sel_list = om.MSelectionList()
    sel_list.add(geo_name)

    dg_path = sel_list.getDagPath(0)

    mFn = om.MFnMesh(dg_path)

    # Iterate trough curves
    sel_obj = cmds.ls(sl=True, l=True)

    if sel_obj:

        child_curves = cmds.listRelatives(sel_obj, ad=True, typ="nurbsCurve", f=True)

        if child_curves:

            for i in child_curves:
                cv_p = cmds.xform(i + ".cv[0]", query=True, t=True)
                p = om.MPoint(cv_p[0], cv_p[1], cv_p[2])

                c_p = mFn.getClosestPoint(p)

                cmds.xform(i + ".cv[0]", t=(c_p[0].x, c_p[0].y, c_p[0].z))

        else:
            cmds.warning("No curves selected...")

    else:
        cmds.warning("Nothing selected...")


snap_curve_to_object(geo_name='example_geo')
