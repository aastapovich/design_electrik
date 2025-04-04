from tkinter import ttk
from data import DataManager

my_date = DataManager()
saved_data = my_date.get_default_settings()
table_data = my_date.get_default_table()

class TableManager:
    _instance = None

    def __new__(cls, treeview=None):
        if not cls._instance:
            if treeview:
                cls._instance = super().__new__(cls)
                cls._instance.treeview = treeview
        return cls._instance

    def __init__(self, treeview=None):
        if treeview:
            self.treeview = treeview  # Инициализируем только если еще не инициализировано


    def sync_table(self, saved_data):
        for item in self.treeview.get_children():
            name = self.treeview.item(item, "values")[0]
            if name in saved_data.keys():
                self.treeview.item(item, values=(saved_data[name]))


    def default_apply_table(self, table_data, saved_data):
        table_data = my_date.get_default_table()
        if self.treeview.get_children():
            self.treeview.delete(*self.treeview.get_children())
        for row in table_data:
            val = saved_data[row]
            self.treeview.insert("", "end", values=val)

    def fill_table(self, table_data, saved_data):
        if self.treeview.get_children():
            self.treeview.delete(*self.treeview.get_children())
        for row in table_data:
            val = saved_data[row]
            self.treeview.insert("", "end", values=val)

    def on_row_clicks(self, event, table_data, saved_data):
        selected_item = self.treeview.selection()
        selected_row = self.treeview.index(selected_item)
        if not selected_item:
            return
        item_id = selected_item[0]
        item_text = self.treeview.item(item_id, "values")[0]
        if item_text in table_data:
            table_data.remove(item_text)
            self.treeview.item(item_id, tags=("disabled",))
        else:
            table_data.insert(selected_row, saved_data[item_text][0])
            self.treeview.item(item_id, tags=("default",))

    def update_saved_check(self, name, var):
        value = not var.get()
        saved_data[name] = saved_data[name] = saved_data[name][0], value, saved_data[name][2]
        self.sync_table(saved_data)

    def update_saved_data(self, name, widget):
        if isinstance(widget, ttk.Radiobutton):
            value = widget.cget('text')
            saved_data[name] = saved_data[name][0], value, saved_data[name][2]
        elif isinstance(widget, ttk.Checkbutton):
            return # Переменные Checkbutton обрабатываются в update_saved_check
        else:
            value = widget.get()
            saved_data[name] = saved_data[name][0], value, saved_data[name][2]
        # Синхронизируем таблицу
        self.sync_table(saved_data)
        return(saved_data)
