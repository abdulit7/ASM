import flet as ft

import flet as ft

class Menubar(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
     
     
        self.appbar = ft.AppBar(
            leading=ft.Icon(ft.Icons.COMPUTER),
            leading_width=40,
            title=ft.Text("", size=20, weight=ft.FontWeight.BOLD),
            center_title=False,
            bgcolor=ft.Colors.GREEN_400,
        )
        
        page.appbar = self.appbar
       