import flet as ft

class TopBar(ft.AppBar):
    def __init__(self):
        super().__init__() 
        self.leading = ft.Icon(ft.Icons.WAREHOUSE)
        self.leading_width = 40
        self.title = ft.Text("WAREHOUSE")
        self.center_title = False
        self.bgcolor = ft.Colors.SURFACE_CONTAINER_HIGHEST

        self.actions = [
            ft.ElevatedButton(
                "ADMIN / Login",
                icon=ft.Icons.ADMIN_PANEL_SETTINGS,
                icon_color=ft.Colors.PINK_400,
            ),
        ]

    # Método para manejar clicks en el PopupMenu
    def check_item_clicked(self, e):
        e.control.checked = not e.control.checked
        e.page.update()