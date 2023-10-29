import flet as ft


def main(page: ft.Page):
    # page.add(ft.SafeArea(ft.Text("Hello, Flet!")))

    

    page.add(
        ft.Row(
            [
                ft.Icon(ft.icons.REMOVE),
                ft.Text('0'),
                ft.Icon(ft.icons.ADD)
            ]
        )
    )

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

ft.app(main)
