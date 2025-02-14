import flet as ft
import pymysql.cursors
from nav.sidebar import Sidebar
from nav.menubar import Menubar

class Users(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()

        self.expand = True
        page.window.title = "Asset Management System"
    

        self.db_config = {
            'user': 'root',
            'password': 'Pak@123',
            'host': '127.0.0.1',
            'database': 'ASM',
            'cursorclass': pymysql.cursors.DictCursor
        }

        # Fetch users from the database
        users = self.fetch_users()

        # Separate users into admins and regular users
        admins = [user for user in users if user['can_login'] == 1]
        regular_users = [user for user in users if user['can_login'] != 1]

        # Create DataTable rows from the fetched users
        admin_rows = self.create_data_rows(admins)
        user_rows = self.create_data_rows(regular_users)

        self.add_user_button = ft.ElevatedButton("Add User", on_click=lambda e: page.go("/userform"))

        # Admin DataTable
        admin_table = ft.DataTable(
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
                ft.DataColumn(ft.Text("Name", weight=ft.FontWeight.W_600)),
                ft.DataColumn(ft.Text("EMP ID", weight=ft.FontWeight.W_600)),
                ft.DataColumn(ft.Text("Branch", weight=ft.FontWeight.W_600)),
                ft.DataColumn(ft.Text("Department", weight=ft.FontWeight.W_600)),
                ft.DataColumn(ft.Text("Can Login", weight=ft.FontWeight.W_600)),
                ft.DataColumn(ft.Text("Action", weight=ft.FontWeight.W_600)),
            ],
            rows=admin_rows
        )

        # User DataTable
        user_table = ft.DataTable(
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
                ft.DataColumn(ft.Text("Name", weight=ft.FontWeight.W_600)),
                ft.DataColumn(ft.Text("EMP ID", weight=ft.FontWeight.W_600)),
                ft.DataColumn(ft.Text("Branch", weight=ft.FontWeight.W_600)),
                ft.DataColumn(ft.Text("Department", weight=ft.FontWeight.W_600)),
                ft.DataColumn(ft.Text("Can Login", weight=ft.FontWeight.W_600)),
                ft.DataColumn(ft.Text("Action", weight=ft.FontWeight.W_600)),
            ],
            rows=user_rows
        )

        # Tabs
        tabs = ft.Tabs(
            selected_index=0,
            tabs=[
                ft.Tab(
                    text="Admins",
                    content=admin_table
                ),
                ft.Tab(
                    text="Users",
                    content=user_table
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
                                ft.Row([ft.Text("Users", size=28, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900), ft.Container(), self.add_user_button]),
                                tabs,
                            ],
                            spacing=30,
                        )
                    )
                )
            ],
            spacing=20
        )

    def fetch_users(self):
        """Fetch users from the database."""
        try:
            connection = pymysql.connect(**self.db_config)
            with connection:
                with connection.cursor() as cursor:
                    cursor.execute("SELECT name, emp_id, branch, department, can_login FROM users ORDER BY name")
                    return cursor.fetchall()
        except pymysql.MySQLError as err:
            print(f"Error: {err}")
            return []

    def create_data_rows(self, users):
        """Create DataRow instances from the fetched users."""
        data_rows = []
        for user in users:
            data_rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(user['name'])),
                        ft.DataCell(ft.Text(user['emp_id'])),
                        ft.DataCell(ft.Text(user['branch'])),
                        ft.DataCell(ft.Text(user['department'])),
                        ft.DataCell(ft.Text("Yes" if user['can_login'] else "No")),
                        ft.DataCell(
                            ft.Row(
                                controls=[
                                    ft.ElevatedButton("Edit", bgcolor=ft.Colors.LIGHT_GREEN_500, color=ft.Colors.WHITE),
                                    ft.ElevatedButton("Delete", bgcolor=ft.Colors.RED_500, color=ft.Colors.WHITE),
                                ],
                                spacing=5,
                                alignment=ft.MainAxisAlignment.CENTER,
                            )
                        ),
                    ]
                )
            )
        return data_rows

