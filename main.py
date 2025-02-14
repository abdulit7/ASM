import flet as ft
from pages.authencations.login import Login
from pages.dashboard.home import Home
from pages.dashboard.users import Users
from components.userform import UserForm
from pages.dashboard.assets import AssetPage
from components.assetform import AssetFormPage  # Change here
from pages.dashboard.components import Components
from pages.dashboard.saleforce import SaleForcePage
from pages.dashboard.saleforce2 import SaleForcePage2

def main(page: ft.Page):
    page.title = "Asset Management System"
    page.expand = True
    page.scroll = "adaptive"  # Enable scrolling on the page

    # Function to handle route changes
    def change_route(route):
        page.views.clear()
        if page.route == "/login":
            page.views.append(
                ft.View(
                    "/login",
                    controls=[Login(page)]
                )
            )
        elif page.route == "/dashboard":
            page.views.append(
                ft.View(
                    "/dashboard",
                    controls=[Home(page)]
                )
            )
        elif page.route == "/user":
            page.views.append(
                ft.View(
                    "/user",
                    controls=[Users(page)]
                )
            )
        elif page.route == "/userform":
            page.views.append(
                ft.View(
                    "/userform",
                    controls=[UserForm(page)]
                )
            )
        elif page.route == "/asset":
            page.views.append(
                ft.View(
                    "/asset",
                    controls=[AssetPage(page)]
                )
            )
        elif page.route == "/assetform":
            page.views.append(
                ft.View(
                    "/assetform",
                    controls=[AssetFormPage(page)]  # Change here
                )
            )
        elif page.route == "/component":
            page.views.append(
                ft.View(
                    "/component",
                    controls=[Components(page)]
                )
            )
        elif page.route == "/saleforce":
            page.views.append(
                ft.View(
                    "/saleforce",
                    controls=[SaleForcePage(page)]
                )
            )

        elif page.route == "/saleforce2":
            page.views.append(
                ft.View(
                    "/saleforce2",
                    controls=[SaleForcePage2(page)]
                )
            )
        page.update()

    # Handle back navigation
    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)
    
    # Assign the route change and view pop events
    page.on_route_change = change_route
    page.on_view_pop = view_pop
    
    # Start the app at the login page
    page.go("/saleforce")

ft.app(target=main, assets_dir="assets", view=ft.AppView.WEB_BROWSER)
