import clr
from Autodesk.Revit.DB import FilteredElementCollector as FEC, \
    WallType, \
    FloorType, \
    RoofType, \
    ElementCategoryFilter, \
    BuiltInCategory, \
    ElementFilter, \
    LogicalOrFilter
from Autodesk.Revit.DB import ElementClassFilter
from System.Collections.Generic import List

clr.AddReference('RevitAPI')

filter_wall = ElementClassFilter(WallType)  # Fiter around class WallType
filter_floor = ElementClassFilter(FloorType)  # Fiter around class FloorType
filter_roof = ElementClassFilter(RoofType)  # Fiter around class RoofType
filter_room = ElementCategoryFilter(BuiltInCategory.OST_Rooms)  # Fiter around category OST_Rooms
filter_stair = ElementCategoryFilter(BuiltInCategory.OST_Stairs)  # Fiter around category OST_Stairs
filter_curtain = ElementCategoryFilter(
    BuiltInCategory.OST_CurtainWallMullions)  # Fiter around category OST_CurtainWallMullions

all_filters_typed = List[ElementFilter]([filter_wall,
                                         filter_floor,
                                         filter_roof,
                                         filter_room,
                                         filter_stair,
                                         filter_curtain])  # Grouping all filters with List[ElementFilter]()

elements = FEC(doc).WherePasses(LogicalOrFilter(all_filters_typed))  # All filtered elements

unic_id_filter = ['07ae6064-8e02-489e-896d-f7554545ebb2-0002d8b3',
                  '07ae6064-8e02-489e-896d-f7554545ebb2-0002d8b4',
                  '07ae6064-8e02-489e-896d-f7554545ebb2-0002d8b6',
                  '07ae6064-8e02-489e-896d-f7554545ebb2-0002d8b7',
                  '07ae6064-8e02-489e-896d-f7554545ebb2-0002d8b9',
                  '07ae6064-8e02-489e-896d-f7554545ebb2-0002d8ba',
                  '07ae6064-8e02-489e-896d-f7554545ebb2-0002d8bc',
                  '07ae6064-8e02-489e-896d-f7554545ebb2-0002d8bd',
                  '07ae6064-8e02-489e-896d-f7554545ebb2-0002d8bf', ]  # Filters UniqueId on

result = [element.Id.IntegerValue for element in elements if element.UniqueId not in unic_id_filter]  # Just result list

bprint(sum(result))