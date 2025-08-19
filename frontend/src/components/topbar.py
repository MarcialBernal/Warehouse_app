import flet as ft

class TopBar(ft.AppBar):
    def __init__(self):
        # Llamamos al constructor de AppBar con los atributos oficiales
        super().__init__(
            leading=ft.Icon(ft.Icons.PALETTE),
            leading_width=40,
            title=ft.Text("AppBar Example"),
            center_title=False,
            bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
            actions=[
                ft.IconButton(ft.Icons.WB_SUNNY_OUTLINED),
                ft.IconButton(ft.Icons.FILTER_3),
                ft.PopupMenuButton(
                    items=[
                        ft.PopupMenuItem(text="Item 1"),
                        ft.PopupMenuItem(),  # divider
                        ft.PopupMenuItem(
                            text="Checked item", checked=False, on_click=self.check_item_clicked
                        ),
                    ]
                ),
            ],
        )

    # Método para manejar clicks en el PopupMenu
    def check_item_clicked(self, e):
        e.control.checked = not e.control.checked
        e.page.update()