import flet as ft
import pymysql.cursors
from nav.menubar import Menubar
from nav.sidebar import Sidebar

class Asset(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()

        self.expand = True
        page.window.title = "Asset Management System"
        page.bgcolor = ft.Colors.BLUE_GREY_50  # Light background for contrast
     

        add_asset_button = ft.ElevatedButton(icon=ft.Icons.ADD, text="ADD Asset", on_click=lambda e: page.go("/assetform"))

        # Deployable DataTable
        deployable_table = ft.DataTable(
            bgcolor=ft.Colors.WHITE,
            border=ft.border.all(1, ft.Colors.GREY_300),
            border_radius=10,
            vertical_lines=ft.BorderSide(1, ft.Colors.GREY_200),
            horizontal_lines=ft.BorderSide(1, ft.Colors.GREY_200),
            heading_row_color=ft.Colors.INDIGO_100,
            heading_text_style=ft.TextStyle(
                color=ft.Colors.INDIGO_900,
                weight=ft.FontWeight.BOLD,
                size=16
            ),
            data_row_color={
                ft.ControlState.HOVERED: ft.Colors.LIGHT_BLUE_50,
            },
            data_row_min_height=50,
            data_text_style=ft.TextStyle(
                color=ft.Colors.GREY_800,
                size=14,
            ),
            show_checkbox_column=False,
            column_spacing=30,
            columns=[
                ft.DataColumn(ft.Text("Category", weight=ft.FontWeight.W_600)),
                ft.DataColumn(ft.Text("Company", weight=ft.FontWeight.W_600)),
                ft.DataColumn(ft.Text("Model", weight=ft.FontWeight.W_600)),
                ft.DataColumn(ft.Text("Serial No", weight=ft.FontWeight.W_600)),
                ft.DataColumn(ft.Text("Purchase Date", weight=ft.FontWeight.W_600)),
                ft.DataColumn(ft.Text("Warranty", weight=ft.FontWeight.W_600)),
                ft.DataColumn(ft.Text("Price", weight=ft.FontWeight.W_600)),
                ft.DataColumn(ft.Text("Status", weight=ft.FontWeight.W_600)),
                ft.DataColumn(ft.Text("Action", weight=ft.FontWeight.W_600)),
            ],
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Laptop")),
                        ft.DataCell(ft.Text("Dell")),
                        ft.DataCell(ft.Text("XPS 15")),
                        ft.DataCell(ft.Text("123456789")),
                        ft.DataCell(ft.Text("2023-01-15")),
                        ft.DataCell(ft.Text("2 Years")),
                        ft.DataCell(ft.Text("$1500")),
                        ft.DataCell(ft.Text("Active")),
                        ft.DataCell(
                            ft.Row(
                                controls=[
                                    ft.ElevatedButton("Edit", bgcolor=ft.Colors.LIGHT_GREEN_500, color=ft.Colors.WHITE),
                                    ft.ElevatedButton("Delete", bgcolor=ft.Colors.RED_500, color=ft.Colors.WHITE)
                                ],
                                spacing=10
                            )
                        ),
                    ],
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Mouse")),
                        ft.DataCell(ft.Text("Logitech")),
                        ft.DataCell(ft.Text("MX Master 3")),
                        ft.DataCell(ft.Text("987654321")),
                        ft.DataCell(ft.Text("2023-06-01")),
                        ft.DataCell(ft.Text("1 Year")),
                        ft.DataCell(ft.Text("$100")),
                        ft.DataCell(ft.Text("Active")),
                        ft.DataCell(
                            ft.Row(
                                controls=[
                                    ft.ElevatedButton("Edit", bgcolor=ft.Colors.LIGHT_GREEN_500, color=ft.Colors.WHITE),
                                    ft.ElevatedButton("Delete", bgcolor=ft.Colors.RED_500, color=ft.Colors.WHITE)
                                ],
                                spacing=10
                            )
                        ),
                    ],
                ),
            ],
        )

        # Deployed DataTable
        deployed_table = ft.DataTable(
            bgcolor=ft.Colors.WHITE,
            border=ft.border.all(1, ft.Colors.GREY_300),
            border_radius=10,
            vertical_lines=ft.BorderSide(1, ft.Colors.GREY_200),
            horizontal_lines=ft.BorderSide(1, ft.Colors.GREY_200),
            heading_row_color=ft.Colors.INDIGO_100,
            heading_text_style=ft.TextStyle(
                color=ft.Colors.INDIGO_900,
                weight=ft.FontWeight.BOLD,
                size=16
            ),
            data_row_color={
                ft.ControlState.HOVERED: ft.Colors.LIGHT_BLUE_50,
            },
            data_row_min_height=50,
            data_text_style=ft.TextStyle(
                color=ft.Colors.GREY_800,
                size=14,
            ),
            show_checkbox_column=False,
            column_spacing=30,
            columns=[
                ft.DataColumn(ft.Text("Category", weight=ft.FontWeight.W_600)),
                ft.DataColumn(ft.Text("Company", weight=ft.FontWeight.W_600)),
                ft.DataColumn(ft.Text("Model", weight=ft.FontWeight.W_600)),
                ft.DataColumn(ft.Text("Serial No", weight=ft.FontWeight.W_600)),
                ft.DataColumn(ft.Text("Purchase Date", weight=ft.FontWeight.W_600)),
                ft.DataColumn(ft.Text("Warranty", weight=ft.FontWeight.W_600)),
                ft.DataColumn(ft.Text("Price", weight=ft.FontWeight.W_600)),
                ft.DataColumn(ft.Text("Status", weight=ft.FontWeight.W_600)),
                ft.DataColumn(ft.Text("Action", weight=ft.FontWeight.W_600)),
            ],
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Monitor")),
                        ft.DataCell(ft.Text("Samsung")),
                        ft.DataCell(ft.Text("Odyssey G9")),
                        ft.DataCell(ft.Text("1122334455")),
                        ft.DataCell(ft.Text("2022-12-01")),
                        ft.DataCell(ft.Text("3 Years")),
                        ft.DataCell(ft.Text("$1200")),
                        ft.DataCell(ft.Text("Deployed")),
                        ft.DataCell(
                            ft.Row(
                                controls=[
                                    ft.ElevatedButton("Edit", bgcolor=ft.Colors.LIGHT_GREEN_500, color=ft.Colors.WHITE),
                                    ft.ElevatedButton("Delete", bgcolor=ft.Colors.RED_500, color=ft.Colors.WHITE)
                                ],
                                spacing=10
                            )
                        ),
                    ],
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Keyboard")),
                        ft.DataCell(ft.Text("Corsair")),
                        ft.DataCell(ft.Text("K95 RGB")),
                        ft.DataCell(ft.Text("9988776655")),
                        ft.DataCell(ft.Text("2023-03-01")),
                        ft.DataCell(ft.Text("2 Years")),
                        ft.DataCell(ft.Text("$200")),
                        ft.DataCell(ft.Text("Deployed")),
                        ft.DataCell(
                            ft.Row(
                                controls=[
                                    ft.ElevatedButton("Edit", bgcolor=ft.Colors.LIGHT_GREEN_500, color=ft.Colors.WHITE),
                                    ft.ElevatedButton("Delete", bgcolor=ft.Colors.RED_500, color=ft.Colors.WHITE)
                                ],
                                spacing=10
                            )
                        ),
                    ],
                ),
            ],
        )

        # Tabs
        tabs = ft.Tabs(
            selected_index=0,
            tabs=[
                ft.Tab(
                    text="Deployable",
                    content=deployable_table
                ),
                ft.Tab(
                    text="Deployed",
                    content=deployed_table
                ),
            ],
            expand=True,
        )

        # Layout
        self.content = ft.ResponsiveRow(
            controls=[
                # Sidebar
                ft.Container(
                    width=250,
                    col={"sm": 12, "md": 3},
                    bgcolor=ft.Colors.INDIGO_900,
                    padding=20,
                    border_radius=ft.border_radius.all(15),
                    content=ft.Column(
                        controls=[
                            Menubar(page),
                            ft.Text("Menu", size=20, weight=ft.FontWeight.W_600, color=ft.Colors.WHITE),
                            Sidebar(page),
                        ],
                        spacing=20
                    )
                ),
                # Main Content Area
                ft.Container(
                    expand=True,
                    col={"sm": 12, "md": 9},
                    padding=30,
                    content=ft.Container(
                        bgcolor=ft.Colors.WHITE,
                        border_radius=ft.border_radius.all(15),
                        padding=30,
                        shadow=ft.BoxShadow(
                            blur_radius=15, 
                            spread_radius=1, 
                            color=ft.Colors.GREY_400
                        ),
                        content=ft.Column(
                            controls=[
                                ft.Row([ft.Text("Assets", size=28, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900), ft.Container(), add_asset_button]),
                                tabs,
                            ],
                            spacing=30,
                        )
                    )
                )
            ],
            spacing=20
        )


def AssetPage(page):
    return Asset(page)