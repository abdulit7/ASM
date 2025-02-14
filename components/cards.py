import flet as ft

class MainCards(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()

        self.expand = True


        self.content = ft.ResponsiveRow(
            controls=[
                ft.Container(
                    content=self.main_cards(
                        ft.Icons.COMPUTER,
                        "TOTAL ASSETS",
                        "50",
                        "View",
                        ft.Colors.BLUE_100,
                        ft.Colors.YELLOW_400,
                        ft.Colors.RED_200
                    ),
                    col={"xs": 12, "sm": 6, "md": 4, "xl": 3},
                ),
                ft.Container(
                    content=self.main_cards(
                        ft.Icons.PERSON,
                        "TOTAL USERS",
                        "50",
                        "View",
                        ft.Colors.BLUE_100,
                        ft.Colors.YELLOW_400,
                        ft.Colors.RED_200
                    ),
                    col={"xs": 12, "sm": 6, "md": 4, "xl": 3},
                ),
                ft.Container(
                    content=self.main_cards(
                        ft.Icons.DASHBOARD,
                        "TOTAL DEPARTMENTS",
                        "50",
                        "View",
                        ft.Colors.BLUE_100,
                        ft.Colors.YELLOW_400,
                        ft.Colors.RED_200
                    ),
                    col={"xs": 12, "sm": 6, "md": 4, "xl": 3},
                ),
                ft.Container(
                    content=self.main_cards(
                        ft.Icons.CATEGORY,
                        "TOTAL CATEGORIES",
                        "50",
                        "View",
                        ft.Colors.BLUE_100,
                        ft.Colors.YELLOW_400,
                        ft.Colors.RED_200
                    ),
                    col={"xs": 12, "sm": 6, "md": 4, "xl": 3},
                ),
            ],
            alignment=ft.MainAxisAlignment.START,
            vertical_alignment=ft.CrossAxisAlignment.START,
        )

    def main_cards(self, leading, title, subtitle, button1, card_bgcolor, listtile_bgcolor, icon_bgcolor):
        return ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.Container(
                            bgcolor=listtile_bgcolor,
                            padding=10,
                            border_radius=8,
                            content=ft.Row(
                                controls=[
                                    ft.Container(
                                        content=ft.Icon(leading, color=ft.Colors.WHITE),
                                        bgcolor=icon_bgcolor,
                                        width=40,
                                        height=40,
                                        alignment=ft.alignment.center,
                                        border_radius=20
                                    ),
                                    ft.Column(
                                        controls=[
                                            ft.Text(title, size=18, weight=ft.FontWeight.BOLD),
                                            ft.Text(subtitle),
                                        ],
                                        spacing=5
                                    )
                                ],
                                spacing=10
                            ),
                        ),
                        ft.Row(
                            [ft.TextButton(button1)],
                            alignment=ft.MainAxisAlignment.END,
                        ),
                    ]
                ),
                padding=10,
                bgcolor=card_bgcolor,
                border_radius=12
            )
        )
