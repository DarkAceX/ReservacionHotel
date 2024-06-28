import flet as ft
def main(page: ft.Page):
    def show_new_interface():
        # Limpiar la página actual
        page.controls.clear()

        # Crear nueva interfaz
        new_content = ft.Column(
            controls=[
                ft.Text("Nueva Interfaz", size=30, weight="bold"),
                ft.Text("Este es el contenido de la nueva interfaz.")
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )

        page.add(new_content)
        page.update()

    # Cargar la imagen de fondo
    bg_image = ft.Container(
        content=ft.Image(
            src=f"/img/Background.jpg",
            fit=ft.ImageFit.COVER,
        ),
        width=page.window.width,
        height=page.window.height,
    )

    # Crear el texto y los elementos superpuestos
    header_text = ft.Container(
        ft.Text(
        "HOTEL ORO VERDE",
        color=ft.colors.LIGHT_GREEN_ACCENT_700,
        size=30,
        weight="bold",
        text_align=ft.TextAlign.CENTER,
        ),
        alignment=ft.alignment.top_center,
        bgcolor=ft.colors.GREY_900, 
        width=400,
        border_radius=ft.BorderRadius(5,5,10,10)
        
   )
    welcome_text = ft.Container(
        ft.Text(
            "BIENVENIDO\nA\nTU HOTEL DE CONFIANZA",
            color=ft.colors.AMBER_ACCENT_400,
            font_family="Arial_bold",
            size=20,
            weight="bold",
            text_align=ft.TextAlign.CENTER,   
        ),
    )

    description_text = ft.Text(
        "Disfrute de una estancia inolvidable con nosotros.\n"
        "Reserve ahora y experimente el lujo y la comodidad que se merece.",
        color=ft.colors.WHITE,
        font_family="Arial_bold",
        size=16,
        text_align=ft.TextAlign.CENTER
    )

    # Crear el botón
    button = ft.IconButton(
        icon=ft.icons.ARROW_FORWARD,
        icon_size=24,
        on_click=lambda _: show_new_interface()
    )

    # Crear el contenedor principal
    content = ft.Column(
        controls=[
            header_text,
            welcome_text,
            description_text,
            button,
        ],
        spacing=80,
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    # Añadir la imagen de fondo y el contenido al layout
    page.add(
        ft.Stack(
            controls=[
                bg_image,
                ft.Container(
                    content=content,
                    alignment=ft.alignment.center,
                    padding=20,
                    blur=5,
                    width=page.window.width, height=page.window.height
                )
            ]
        )
    )

ft.app(target=main)