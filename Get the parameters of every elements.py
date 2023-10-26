import clr
from Autodesk.Revit.DB import FilteredElementCollector as FEC, BuiltInParameter, ElementClassFilter, ElementType, \
    BuiltInCategory

clr.AddReference('RevitAPI')

id_list = ['-1010103', '-1010109', '-1010108']

filter_all_elements = ElementClassFilter(ElementType)
elements = FEC(doc).WherePasses(filter_all_elements)

b_parameters = BuiltInParameter.GetValues(BuiltInParameter)  # list

r_parameters = [param for param in b_parameters if str(int(param)) in id_list]  # list

cost = 0

print r_parameters

for element in elements:
    for param in r_parameters:
        if element.Parameter[param]:
            cost += 1

print cost