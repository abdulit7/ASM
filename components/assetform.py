import flet as ft
from nav.sidebar import Sidebar
from nav.menubar import Menubar
from components.fields import CustomTextField

class AssetForm(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()

        page.window.title = "Asset Management System"
        page.scroll = "adaptive"
        self.expand = True

        # Form Fields
        self.name_field = CustomTextField(label="Name")
        self.category_field = CustomTextField(label="Category")
        self.company_field = CustomTextField(label="Company")
        self.model_field = CustomTextField(label="Model")
        self.serial_no_field = CustomTextField(label="Serial No")
        self.purchase_date_field = ft.DatePicker()
        self.warranty_field = CustomTextField(label="Warranty")
        self.price_field = CustomTextField(label="Price")
        self.status_field = ft.Dropdown(
            label="Status",
            options=[
                ft.dropdown.Option("Active"),
                ft.dropdown.Option("Inactive"),
                ft.dropdown.Option("Deployed"),
            ]
        )

        # Form Layout
        self.content = ft.ResponsiveRow(
            controls=[
                # Sidebar
                ft.Container(
                    width=250,
                    col={"sm": 12, "md": 3},
                    content=ft.Column(
                        controls=[
                            Menubar(page),
                            ft.Text("Menu", size=18, weight=ft.FontWeight.W_600),
                            Sidebar(page),
                        ],
                        spacing=20
                    )
                ),
                # Main Form Area
                ft.Container(
                    expand=True,
                    col={"sm": 12, "md": 9},
                    bgcolor=ft.Colors.GREY_100,
                    padding=30,
                    content=ft.Container(
                        bgcolor=ft.Colors.WHITE,
                        border_radius=ft.border_radius.all(15),
                        padding=30,
                        shadow=ft.BoxShadow(blur_radius=10, spread_radius=1, color=ft.Colors.GREY_400),
                        content=ft.Column(
                            controls=[
                                ft.Text("Asset Register", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900),
                                self.build_form_row("Name", self.name_field),
                                self.build_form_row("Category", self.category_field),
                                self.build_form_row("Company", self.company_field),
                                self.build_form_row("Model", self.model_field),
                                self.build_form_row("Serial No", self.serial_no_field),
                                ft.Text("Purchase Date"),
                                ft.Container(content=self.purchase_date_field, width=300),
                                self.build_form_row("Warranty", self.warranty_field),
                                self.build_form_row("Price", self.price_field),
                                self.build_form_row("Status", self.status_field),
                                # Save and Cancel Buttons
                                ft.Row(
                                    controls=[
                                        ft.ElevatedButton("Save", 
                                            icon=ft.Icons.SAVE, 
                                            bgcolor=ft.Colors.GREEN_600, 
                                            color=ft.Colors.WHITE, 
                                            style=ft.ButtonStyle(
                                                shape=ft.RoundedRectangleBorder(radius=10)
                                            ),
                                        ),
                                        ft.ElevatedButton("Cancel", 
                                            icon=ft.Icons.CANCEL, 
                                            bgcolor=ft.Colors.RED_600, 
                                            color=ft.Colors.WHITE, 
                                            style=ft.ButtonStyle(
                                                shape=ft.RoundedRectangleBorder(radius=10)
                                            )
                                        ),
                                    ],
                                    alignment=ft.MainAxisAlignment.END,
                                    spacing=20,
                                )
                            ],
                            spacing=20,
                            scroll="adaptive"
                        )
                    )
                )
            ],
            spacing=20
        )

    def build_form_row(self, label_text, input_control):
        """Builds a single row for the form with a label and input field."""
        return ft.ResponsiveRow(
            controls=[
                ft.Container(
                    width=150,
                    col={"xs": 12, "md": 3},
                    content=ft.Text(label_text, size=18, weight=ft.FontWeight.W_500, color=ft.Colors.BLUE_GREY_700),
                ),
                ft.Container(
                    expand=True,
                    col={"xs": 12, "md": 9},
                    content=input_control,
                ),
            ],
            spacing=10,
        )
        
def AssetFormPage(page):
    return AssetForm(page)
