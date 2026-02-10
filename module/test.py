import flet as ft

def visual(page: ft.Page):

    page.title = 'Flet app' #Имя окна
    page.theme_mode = 'light' #Тема окна
    page.vertical_alignment = ft.MainAxisAlignment.START #Расположение элементов в окне

    user_label = ft.Text('Info')
    user_text = ft.TextField(value = '0', width = 150, text_align = ft.TextAlign.LEFT)

    def get_info(e):
        user_label.value = user_text.value
        page.update( )

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.Icons.HOME, on_click = get_info),
                ft.Icon(ft.Icons.BACK_HAND),
                # ft.ElevatedButton('Click me', on_click = get_info),
                # ft.OutlinedButton('Sorry', on_click = get_info),
                # ft.Checkbox(label = 'Yes', value = True, on_change = None)
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),

        ft.Row(
            [
                user_label,
                user_text
            ],
            alignment=ft.MainAxisAlignment.CENTER
    )

    )

ft.app(target=visual)

