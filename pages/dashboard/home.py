import flet as ft
from nav.sidebar import Sidebar
from nav.menubar import Menubar
from components.cards import MainCards

class Home(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()

        self.expand = True
     
    
        page.window.title = "Asset Management System"

        self.content = ft.Row(
            controls=[
                ft.Container(
                    width=250,  # Fixed width for the sidebar
                    content=ft.Column(
                        controls=[
                            Menubar(page),
                            ft.Text("Menu", size=20, weight=ft.FontWeight.BOLD),
                            Sidebar(page),
                        ],
                        spacing=10,
                    ),
                ),
                ft.Container(
                    expand=True,
                    content=ft.Column(
                        controls=[
                            MainCards(page),
                        ],
                        spacing=10,
                    ),
                    bgcolor=ft.Colors.GREY_200,
                    padding=20,
                ),
            ],
        )
