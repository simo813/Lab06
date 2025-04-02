import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.dropdownAnno = None
        self.dropdownAnnoValue = None
        self.dropdownBrand = None
        self.dropdownBrandValue = None
        self.dropdownRetailer = None
        self.dropdownRetailerValue = None
        self.btnTopV = None
        self.btnAnalizzaV = None
        self.txt_result = None
        # Add resize listener

        self._page.on_resize = self.update_dropdown_widths

    def load_interface(self):
        # title
        self._title = ft.Text("Analizza vendite", color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW with some controls
        # dropdown options
        self.dropdownAnno = ft.Dropdown(
            width=self._page.width / 3, label="Anno", options=[ft.dropdown.Option (key=None, text="Nessun valore")],
            on_change = self._controller.dropdownAnnoChanged

        )
        self._controller.handleDropdownAnno()

        self.dropdownBrand = ft.Dropdown(
            width=self._page.width / 3, label="Brand", options=[ft.dropdown.Option (key=None, text="Nessun valore")],
            on_change = self._controller.dropdownBrandChanged

        )
        self._controller.handleDropdownBrand()

        self.dropdownRetailer = ft.Dropdown(
            width=self._page.width / 2, label="Retailer", options=[ft.dropdown.Option (key=None, text="Nessun valore")],
            on_change = self._controller.dropdownRetailerChanged

        )
        self._controller.handleDropdownRetailer()

        # buttons
        self.btnTopV = ft.ElevatedButton(text="Top vendite")
        self.btnAnalizzaV = ft.ElevatedButton(text="Analizza vendite")

        #Append rows to page
        row1 = ft.Row([self.dropdownAnno, self.dropdownBrand, self.dropdownRetailer], alignment=ft.MainAxisAlignment.CENTER)
        row2 = ft.Row([self.btnTopV, self.btnAnalizzaV], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)
        self._page.controls.append(row2)

        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_dropdown_widths(self, e):
        self.dropdownAnno.width = self._page.width / 4
        self.dropdownBrand.width = self._page.width / 4
        self.dropdownRetailer.width = self._page.width / 2
        self._page.update()

    def update_page(self):
        self._page.update()
