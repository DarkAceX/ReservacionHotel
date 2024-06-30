import flet as ft
from views.main_menu import menu

def main(page: ft.Page):
    BG='#FFCD00'
    BLACK='#000000'
    FG='#00D513'
    WHITE='#FFFFFF'
    
    page.title = 'HOTEL ORO VERDE'
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = BG
    
    def navigate_page(e):
        page.views.clear()
        menu(page)
    
    container = ft.Container(
        content=ft.Column(
            controls=[
                ft.Container(
                    ft.Text(
                        'HOTEL ORO VERDE',
                        color=FG,
                        font_family='Arial',
                        weight='bold',
                        size=25,
                        text_align=ft.TextAlign.CENTER
                    ),
                    bgcolor=BLACK,
                    border_radius=10,
                    width=270,
                    margin=20
                ),
                ft.Container(
                    ft.Text(
                        'BIENVENIDO'
                        '\nA'
                        '\nTU HOTEL DE CONFIANZA',
                        color=BLACK,
                        font_family='Arial',
                        weight='bold',
                        size=20,
                        text_align=ft.TextAlign.CENTER,
                    )
                ),
                ft.Container(
                    ft.Text(
                        'Disfrute de una estancia inolvidable con nosotros. Reserve ahora y experimente el lujo y la comodidad que se merece.',
                        color=BLACK,
                        font_family='Arial',
                        size=16,
                        weight='bold',
                        text_align=ft.TextAlign.CENTER
                    )
                ),
                ft.IconButton(
                    icon='ARROW_CIRCLE_RIGHT',
                    icon_size=70,
                    icon_color=BLACK,
                    alignment=ft.alignment.bottom_center,
                    on_click=navigate_page,
                )
            ],
            spacing=100,
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,   
        )
    )
    
    page.add(container)
    page.update()

ft.app(main)
