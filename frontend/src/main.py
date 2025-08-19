import flet as ft
from components.topbar import TopBar
from components.sidebar import SideBar


def main(page: ft.Page):
    page.title = "AppBar Example"

    # Creamos la instancia de nuestra TopBar personalizada
    page.appbar = TopBar()
    
    rail = SideBar()

    page.add(
        ft.Row(
            [
                rail,
                ft.VerticalDivider(width=1),
                ft.Column(
                    [ft.Text("Body!")],
                    alignment=ft.MainAxisAlignment.START,
                    expand=True,
                ),
            ],
            expand=True,
        )
    )


ft.app(main)
