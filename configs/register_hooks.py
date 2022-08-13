from typing import List

from eve import Eve
from hooks.base_hooks_table import BaseHooksTable


def register_hooks(app: Eve, hooks_tables: List[BaseHooksTable]) -> None:
    for hook_table in hooks_tables:
        hook_table.register_hooks(app)
