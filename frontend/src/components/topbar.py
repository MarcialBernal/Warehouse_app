import flet as ft

class TopBar(ft.AppBar):
    def __init__(self):
        # Llamamos al constructor de AppBar con los atributos oficiales
        super().__init__(
            leading=ft.Icon(ft.Icons.WAREHOUSE),
            leading_width=40,
            title=ft.Text("WAREHOUSE"),
            center_title=False,
            bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
            actions=[
                ft.ElevatedButton("ADMIN / Login",
                                    icon=ft.Icons.ADMIN_PANEL_SETTINGS,
                                    icon_color=ft.Colors.PINK_400,),

            ],
        )

    # Método para manejar clicks en el PopupMenu
    def check_item_clicked(self, e):
        e.control.checked = not e.control.checked
        e.page.update()