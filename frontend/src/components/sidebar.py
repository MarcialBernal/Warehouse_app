import flet as ft

class SideBar(ft.NavigationRail):
    def __init__(self):
        super().__init__() 
        self.selected_index = 0
        self.label_type = ft.NavigationRailLabelType.ALL
        self.min_width = 100
        self.min_extended_width = 400
        self.group_alignment = -0.9

        
        self.destinations = [
            ft.NavigationRailDestination(
                icon=ft.Icons.CREATE_ROUNDED,
                selected_icon=ft.Icons.CREATE,
                label="Add Item to Warehouse",
            ),
            ft.NavigationRailDestination(
                icon=ft.Icons.FAVORITE_BORDER,
                selected_icon=ft.Icons.FAVORITE,
                label="Inventario",
            ),
            ft.NavigationRailDestination(
                icon=ft.Icons.BOOKMARK_BORDER,
                selected_icon=ft.Icons.BOOKMARK,
                label="Requisiciones",
            ),
            ft.NavigationRailDestination(
                icon=ft.Icons.SETTINGS_OUTLINED,
                selected_icon=ft.Icons.SETTINGS,
                label_content=ft.Text("Settings"),
            ),
        ]
        self.on_change = self.on_destination_change

    def fab_clicked(self, e):
        pass
        

    def on_destination_change(self, e):
        pass
        
