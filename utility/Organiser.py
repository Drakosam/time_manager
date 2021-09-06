from typing import List

from utility.FileManager import read_from_file, write_to_file


class Organiser:
    def __init__(self):
        self.categories = read_from_file()
        self.now_category = ''
        self.now_item = ''

    def add_category(self, name):
        if not (name in self.categories):
            self.categories.setdefault(name, {})
            write_to_file(self.categories)

    def get_category_names(self) -> List[str]:
        return list(self.categories.keys())

    def rename_category(self, old_name, new_name):
        if not (new_name in self.categories) and new_name:
            if old_name in self.categories:
                self.categories[new_name] = self.categories.pop(old_name)

    def select_category(self, name: str):
        if name in self.categories:
            self.now_category = name

    def add_item_to_category(self, name):
        if self.now_category and self.now_category in self.categories:
            if name not in self.categories[self.now_category]:
                self.categories[self.now_category].setdefault(name, {'text': ''})
                write_to_file(self.categories)

    def get_items_name_in_category(self) -> List[str]:
        if self.now_category and self.now_category in self.categories:
            return list(self.categories[self.now_category].keys())
        return []

    def update_item_name_in_category(self, old_name, new_name):
        if self.now_category and self.now_category in self.categories:
            if old_name in self.categories[self.now_category]:
                if new_name not in self.categories[self.now_category]:
                    self.categories[self.now_category][new_name] = self.categories[self.now_category].pop(old_name)

    def select_item(self, name):
        if self.now_category and self.now_category in self.categories:
            if name in self.categories[self.now_category]:
                self.now_item = name

    def get_item_details(self):
        if self.now_category and self.now_category in self.categories:
            if self.now_item and self.now_item in self.categories[self.now_category]:
                return self.categories[self.now_category][self.now_item]['text']
        return ''

    def set_item_details(self, new_text):
        if self.now_category and self.now_category in self.categories:
            if self.now_item and self.now_item in self.categories[self.now_category]:
                self.categories[self.now_category][self.now_item]['text'] = new_text
                write_to_file(self.categories)
