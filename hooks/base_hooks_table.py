from abc import abstractmethod

from eve import Eve


class BaseHooksTable:
    @abstractmethod
    def register_hooks(self, app: Eve) -> None:
        pass
