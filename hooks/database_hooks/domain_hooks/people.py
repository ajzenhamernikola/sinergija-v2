import bcrypt
from eve import Eve
from hooks.base_hooks_table import BaseHooksTable


class PeopleHooksTable(BaseHooksTable):
    def on_insert_people(self, items):
        for item in items:
            item["password"] = bcrypt.hashpw(
                item["password"], bcrypt.gensalt())

    def on_update_people(self, updates, original):
        if "password" in updates:
            updates["password"] = bcrypt.hashpw(
                updates["password"], bcrypt.gensalt())

    def register_hooks(self, app: Eve) -> None:
        app.on_insert_people += self.on_insert_people
        app.on_update_people += self.on_update_people
