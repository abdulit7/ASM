
import flet as ft
from components.fields import CustomTextField
import pymysql.cursors

class Login(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        

        self.expand = True


        # Database configuration
        self.db_config = {
            'user': 'root',
            'password': 'Pak@123',
            'host': '127.0.0.1',
            'database': 'ASM',
            'cursorclass': pymysql.cursors.DictCursor
        }


        self.emp_id = ft.Container(
            content=CustomTextField(label="EMP ID"), border=ft.border.all(width=1, color=ft.Colors.BLUE_400)
        )

        self.password = ft.Container(
            content=CustomTextField(label="Password", password=True, can_reveal_password=True),border=ft.border.all(width=1, color=ft.Colors.BLUE_400)
        )

        self.login_button = ft.Container(
            content=ft.Text("Login"),
            alignment=ft.alignment.center,
            bgcolor=ft.Colors.BLUE_400,
            height=40,
            on_click=self.auth_user,
        )

        self.content = ft.Row(
            controls=[
                ft.Container(
                    expand= 2,
                    padding=ft.padding.all(20),
                    content=ft.Column(
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Text("Welcome Back", color=ft.Colors.BLUE_400, size=40, weight=ft.FontWeight.BOLD),
                            ft.Container(height=20),
                            self.emp_id,
                            self.password,
                            self.login_button,
                            ft.Container(height=200),
                      

                        ]
                        
                    )
                ),
                ft.Container(
                    expand= 3,
                    image=ft.DecorationImage(
                        src="images/banner.jpg",
                        fit="cover",

                    ),
                  
                   
                    padding=ft.padding.all(20),
                    content=ft.Column(
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Icon(name=ft.Icons.LOCK_PERSON_ROUNDED, size=200, color=ft.Colors.YELLOW_400),
                            ft.Text("Login Section", color="white", size=20, weight=ft.FontWeight.NORMAL)
                      

                        ]
                    )
                )
            ]
        )
        
    def auth_user(self, e):
        emp_id = self.emp_id.content.value
        password = self.password.content.value

        connection = pymysql.connect(**self.db_config)
        with connection.cursor() as cursor:
            sql = "SELECT * FROM users WHERE can_login = 1 AND emp_id = %s AND password = %s"
            cursor.execute(sql, (emp_id, password))
            user = cursor.fetchone()
            if user:
                self.page.go("/dashboard")
            else:
                print("Invalid credentials")
