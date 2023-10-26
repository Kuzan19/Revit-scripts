import clr
from Autodesk.Revit.DB import FilteredElementCollector as FEC, \
    BuiltInCategory, \
    ElementCategoryFilter, \
    ElementFilter, \
    LogicalOrFilter
from System.Collections.Generic import List
clr.AddReference('RevitAPI')

filter_door = ElementCategoryFilter(BuiltInCategory.OST_DoorTags)  # Fiter around category OST_DoorTags
filter_room = ElementCategoryFilter(BuiltInCategory.OST_RoomTags)  # Fiter around category OST_RoomTags
filter_window = ElementCategoryFilter(BuiltInCategory.OST_WindowTags)  # Fiter around category OST_WindowTags
filter_wall = ElementCategoryFilter(BuiltInCategory.OST_WallTags)  # Fiter around category OST_WallTags
filter_view_id = ElementCategoryFilter(BuiltInCategory.OST_Views)  # Fiter around category OST_Views

all_filters_typed = List[ElementFilter]([filter_door,
                                         filter_room,
                                         filter_window,
                                         filter_wall,
                                         ])  # Grouping all filters with List[ElementFilter]()

views = FEC(doc).WherePasses(filter_view_id)


def search_elements(views, id):
    result = []
    for view in views:
        if view.Id.IntegerValue == id:
            elements = FEC(doc, view.Id).WherePasses(LogicalOrFilter(all_filters_typed))
            for element in elements:
                result.append(element.Id.IntegerValue)
    return sum(result)


bprint(search_elements(views, 695) + search_elements(views, 136343))