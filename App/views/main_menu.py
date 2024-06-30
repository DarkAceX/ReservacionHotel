# main_menu.py
import flet as ft
from views.reserved import reserved

def menu(page: ft.Page):
    
    BG='#FFCD00'
    BLACK='#000000'
    FG='#00D513'
    WHITE='#FFFFFF'
    
    def navigate_reserved(e):
        page.views.clear()
        reserved(page)
    
    page.views.append(
        ft.View(
            bgcolor=BG,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=100,
            controls=[
                ft.Container(
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
                            ft.ElevatedButton(
                                content=ft.Container(
                                    content=ft.Column(
                                        [
                                            ft.Text(
                                                'RESERVA YA!',
                                                color=BLACK,
                                                font_family='Arial',
                                                weight='bold',
                                                size=25,
                                                text_align=ft.TextAlign.CENTER
                                            )   
                                        ]
                                    )
                                ),
                                bgcolor=FG,
                                width=270,
                                on_click=navigate_reserved,
                            ),
                            ft.ElevatedButton(
                                content=ft.Container(
                                    content=ft.Column(
                                        [
                                            ft.Text(
                                                'HABITACIONES DISPONIBLES',
                                                color=BLACK,
                                                font_family='Arial',
                                                weight='bold',
                                                size=20,
                                                text_align=ft.TextAlign.CENTER
                                            )   
                                        ]
                                    )
                                ),
                                bgcolor=FG,
                                width=270
                            ),
                            ft.ElevatedButton(
                                content=ft.Container(
                                    content=ft.Column(
                                        [
                                            ft.Text(
                                                'ADMINISTRA TU RESERVACION',
                                                color=BLACK,
                                                font_family='Arial',
                                                weight='bold',
                                                size=20,
                                                text_align=ft.TextAlign.CENTER
                                            )   
                                        ]
                                    )
                                ),
                                bgcolor=FG,
                                width=270
                            ),
                            ft.TextButton(
                                'DERECHOS Y POLITICAS DEL HOTEL',
                                icon="ARROW_CIRCLE_RIGHT",
                                icon_color=BLACK,
                                style=ft.ButtonStyle(
                                    color=ft.colors.BLACK
                                )
                                
                            )                            
                        ],
                        alignment=ft.MainAxisAlignment.START,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=100
                    )
                )
            ] 
        )
    )
    page.update()
