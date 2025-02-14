import flet as ft

class Sidebar(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()

        self.expand = False  # Sidebar should not expand to fill available space

        self.content = ft.Container(
            bgcolor="#37474F",  # HEX for BLUE_GREY_900
            padding=ft.padding.symmetric(vertical=20, horizontal=10),
            border_radius=12,
            width=250,  # Fixed width for the sidebar
            content=ft.Column(
                controls=[
                    self.create_menu_button("Dashboard", ft.Icons.DASHBOARD, lambda e: page.go("/dashboard")),
                    self.create_menu_button("Assets", ft.Icons.REPORT, lambda e: page.go("/asset")),
                    self.create_menu_button("Components", ft.Icons.PEOPLE, lambda e: page.go("/component")),
                    self.create_menu_button("Users", ft.Icons.PEOPLE, lambda e: page.go("/user")),
                    self.create_menu_button("Category", ft.Icons.SETTINGS, lambda e: page.go("/category")),
                    self.create_menu_button("Saleforce2", ft.Icons.SETTINGS, lambda e: page.go("/saleforce2")),
                    self.create_menu_button("Sale Force", ft.Icons.SETTINGS, lambda e: page.go("/saleforce")),
                    self.create_menu_button("Logout", ft.Icons.LOGOUT, lambda e: page.go("/logout")),
                ],
                spacing=15,
                scroll= "adaptive"
            )
        )

    def create_menu_button(self, text, icon, on_click):
        return ft.TextButton(
            content=ft.Row(
                controls=[
                    ft.Container(
                        content=ft.Icon(icon, color="#FFFFFF"),  # HEX for WHITE
                        width=40,
                        height=40,
                        alignment=ft.alignment.center,
                        bgcolor="#455A64",  # Solid background color
                        border_radius=20
                    ),
                    ft.Text(text, color="#FFFFFF", size=16, weight=ft.FontWeight.BOLD),
                ],
                alignment=ft.MainAxisAlignment.START,
                spacing=10,
            ),
            style=ft.ButtonStyle(
                color="#FFFFFF",
                overlay_color="rgba(69, 90, 100, 0.2)",  # RGBA color for transparency
                padding=ft.padding.all(10),  # Correct padding usage
                shape=ft.RoundedRectangleBorder(radius=8)
            ),
            on_click=on_click
        )
