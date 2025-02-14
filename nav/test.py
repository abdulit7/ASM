import flet as ft
from components.fields import CustomTextField

class UserRegistrationForm(ft.UserControl):
    def __init__(self):
        super().__init__()

    def build(self):
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text("User Registration Form", style=ft.TextThemeStyle.HEADLINE_MEDIUM, weight=ft.FontWeight.BOLD),
                    
                    CustomTextField(label="Username", icon=ft.icons.PERSON),
                    CustomTextField(label="Email", icon=ft.icons.EMAIL),
                    CustomTextField(label="Phone Number", icon=ft.icons.PHONE),
                    CustomTextField(label="Password", icon=ft.icons.LOCK, password=True, can_reveal_password=True),
                    CustomTextField(label="Confirm Password", icon=ft.icons.LOCK, password=True, can_reveal_password=True),

                    ft.ElevatedButton(
                        text="Register",
                        icon=ft.icons.CHECK_CIRCLE_OUTLINE,
                        on_click=self.on_register_click,
                        style=ft.ButtonStyle(
                            bgcolor={ft.ControlState.DEFAULT: ft.Colors.BLUE_400},
                            shape=ft.RoundedRectangleBorder(radius=12),
                            color=ft.Colors.WHITE,
                        )
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=15,
                width=400,
            ),
            padding=20,
            alignment=ft.alignment.center,
            border_radius=16,
            bgcolor=ft.Colors.SURFACE_VARIANT,
            shadow=ft.BoxShadow(blur_radius=10, spread_radius=2, color=ft.Colors.GREY_500),
        )

    def on_register_click(self, e):
        print("Register button clicked!")

def main(page: ft.Page):
    page.title = "User Registration Form"
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.vertical_alignment = ft.CrossAxisAlignment.CENTER
    page.add(UserRegistrationForm())

ft.app(target=main)
