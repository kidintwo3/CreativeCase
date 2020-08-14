import maya.api.OpenMaya as om

def addDebugPoints(locatorShape=str,points=om.MPointArray()):

    sel = om.MSelectionList()
    sel.add(locatorShape)
    path = sel.getDagPath(0)
    
    fnDepLocShape = om.MFnDependencyNode(path.node())
    p_pointAPlug = fnDepLocShape.findPlug("debugInputPoints", True)
    
    # Load point data
    pAD_points = om.MFnPointArrayData()
    o_pA = pAD_points.create(points)
    p_pointAPlug.setMObject(o_pA)


# Add points here
locatorShape = "baseLocShape1"
points = om.MPointArray()

points.append(om.MPoint(0.0, 0.1, 0.0))
points.append(om.MPoint(1.0, 0.1, 0.0))
points.append(om.MPoint(1.0, 1.0, 0.0))

points.append(om.MPoint(2.0, 1.0, 0.0))
points.append(om.MPoint(3.0, 2.5, 0.5))
#points.append(om.MPoint(-1.0, 2.0, 0.5))

addDebugPoints(locatorShape, points)