import clr
from Autodesk.Revit.DB import FilteredElementCollector as FEC, WallType
from Autodesk.Revit.DB import ElementClassFilter, BuiltInParameter


clr.AddReference('RevitAPI')

filter_wall = ElementClassFilter(WallType)  # Fiter around class WallType

elements = FEC(doc).WherePasses(filter_wall)

result = 0

for element in elements:
    if element.Parameter[BuiltInParameter.ALL_MODEL_TYPE_MARK]:
        parameter = element.Parameter[BuiltInParameter.ALL_MODEL_TYPE_MARK]
        result += parameter.Id.IntegerValue
    else:
        print(element.Parameter[BuiltInParameter.ALL_MODEL_TYPE_MARK])
        print element.Category.Name

print result
