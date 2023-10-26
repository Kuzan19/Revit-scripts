import clr
from Autodesk.Revit.DB import FilteredElementCollector as FEC, FamilyInstance
from Autodesk.Revit.DB import ElementClassFilter


clr.AddReference('RevitAPI')

filters = ElementClassFilter(FamilyInstance)
elements = FEC(doc).WherePasses(filters).WhereElementIsViewIndependent()


def selector(elements):
    list_elements = []
    for element in elements:
        filters = ['Двери', 'Окна', 'Обобщенные модели']
        if element.Category.Name not in filters:
            list_elements.append(element)
    return list_elements


print counter(elements)
