# main_menu.py
import flet as ft

def reserved(page: ft.Page):
    
    BG='#FFCD00'
    BLACK='#000000'
    FG='#00D513'
    WHITE='#FFFFFF'
    
    full_name = ft.Ref[ft.TextField]()
    
    def save_name(e):
        name = full_name.current.value
        print(f"Nombre completo: {name}")
    
    page.views.append(
        ft.View(
            bgcolor=BG,
            spacing=50,
            controls=[
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Container(
                                ft.Text(
                                    'RESERVACION',
                                    color=FG,
                                    font_family='Arial',
                                    weight='bold',
                                    size=25,
                                    text_align=ft.TextAlign.CENTER
                                ),
                                bgcolor=BLACK,
                                border_radius=10,
                                width=270,
                                margin=20,
                                alignment=ft.alignment.top_center,
                            )                                          
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER
                    ),
                    alignment=ft.alignment.top_center,
                ),
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Container(
                                ft.Text(
                                    'INGRESA TUS DATOS',
                                    color=BLACK,
                                    font_family='Arial',
                                    weight='bold',
                                    size=20,
                                    text_align=ft.TextAlign.CENTER
                                ),
                                bgcolor=FG,
                                width=270,
                                border_radius=10
                            ),
                            ft.Container(
                                ft.TextField(
                                    label='NOMBRE COMPLETO',
                                    ref=full_name,
                                    width=270,
                                    height=50,
                                    border_color=BLACK,
                                    color=BLACK,
                                    cursor_color=BLACK,
                                    label_style=ft.TextStyle(
                                        color=BLACK
                                    )
                                ),
                            ),
                            ft.Container(
                                ft.ElevatedButton(
                                    text="Guardar",
                                    on_click=save_name
                                ),
                                width=270,
                                margin=20,
                                alignment=ft.alignment.center
                            )
                        ]
                    )
                )
            ] 
        )
    )
    page.update()