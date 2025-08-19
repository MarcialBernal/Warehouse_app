import flet as ft

class SideBar(ft.NavigationRail):
    def __init__(self):
        super().__init__(
            selected_index=0,
            label_type=ft.NavigationRailLabelType.ALL,
            min_width=100,
            min_extended_width=400,
            leading=ft.FloatingActionButton(
                icon=ft.Icons.CREATE, text="Add Item to Warehouse", on_click=self.fab_clicked
            ),
            group_alignment=-0.9,
            destinations=[
                ft.NavigationRailDestination(
                    icon=ft.Icons.FAVORITE_BORDER,
                    selected_icon=ft.Icons.FAVORITE,
                    label="First",
                ),
                ft.NavigationRailDestination(
                    icon=ft.Icons.BOOKMARK_BORDER,
                    selected_icon=ft.Icons.BOOKMARK,
                    label="Second",
                ),
                ft.NavigationRailDestination(
                    icon=ft.Icons.SETTINGS_OUTLINED,
                    selected_icon=ft.Icons.SETTINGS,
                    label_content=ft.Text("Settings"),
                ),
            ],
            on_change=self.on_destination_change,
        )

    def fab_clicked(self, e):
        pass
        #print("FAB clicked!")

    def on_destination_change(self, e):
        pass
        #print("Selected destination:", e.control.selected_index)