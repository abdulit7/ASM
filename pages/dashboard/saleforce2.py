import flet as ft
from nav.menubar import Menubar
from nav.sidebar import Sidebar

class SaleForce2(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()

        self.expand = True
        page.window.title = "Asset Management System"
        page.bgcolor = ft.Colors.BLUE_GREY_50

        add_component_button = ft.ElevatedButton(
            icon=ft.Icons.ADD, 
            text="ADD Component", 
            on_click=lambda e: page.go("/componentform")
        )

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
                        ft.DataCell(ft.Text("Bio-Metric")),
                        ft.DataCell(ft.Text("ZKTeco")),
                        ft.DataCell(ft.Text("UA860")),
                        ft.DataCell(ft.Text("123456789")),
                        ft.DataCell(ft.Text("2023-01-15")),
                        ft.DataCell(ft.Text("1 Years")),
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
            ],
        )

        # Tabs for Deployable and Deployed
        tabs = ft.Tabs(
            selected_index=0,
            tabs=[
                ft.Tab(
                    text="Deployable",
                    content=deployable_table
                ),
                ft.Tab(
                    text="Deployed",
                    content=deployable_table
                ),
            ],
            expand=True,
        )

        # Layout
        self.content = ft.Column(
            expand=True,
            scroll="auto",
            controls=[
                ft.ResponsiveRow(
                    controls=[
                        # Sidebar
                        ft.Container(
                            col={"sm": 12, "md": 3, "lg": 2},
                            bgcolor=ft.Colors.INDIGO_900,
                            padding=ft.Padding(10, 20, 10, 20),
                            border_radius=ft.border_radius.all(15),
                            content=ft.Column(
                                controls=[
                                    Menubar(page),
                                    ft.Text("Menu", size=20, weight=ft.FontWeight.W_600, color=ft.Colors.WHITE),
                                    Sidebar(page),
                                ],
                                spacing=10
                            )
                        ),
                        # Main Content Area
                        ft.Container(
                            expand=True,
                            col={"sm": 12, "md": 9, "lg": 10},
                            padding=ft.Padding(10, 20, 10, 20),
                            content=ft.Container(
                                bgcolor=ft.Colors.WHITE,
                                border_radius=ft.border_radius.all(15),
                                padding=ft.Padding(20, 30, 20, 30),
                                shadow=ft.BoxShadow(
                                    blur_radius=15, 
                                    spread_radius=1, 
                                    color=ft.Colors.GREY_400
                                ),
                                content=ft.Column(
                                    controls=[
                                        ft.Row(
                                            controls=[
                                                ft.Text("Components", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900),
                                                ft.Container(),
                                                add_component_button
                                            ],
                                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                                        ),
                                        tabs,
                                    ],
                                    spacing=20
                                )
                            )
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER, 
                    vertical_alignment=ft.CrossAxisAlignment.START
                )
            ]
        )

def SaleForcePage2(page):
    return SaleForce2(page)
