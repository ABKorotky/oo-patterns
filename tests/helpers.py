__all__ = ("TestingMixin",)

import typing as t

if t.TYPE_CHECKING:
    ...


TestedClassTypeVar = t.TypeVar("TestedClassTypeVar")


class TestingMixin(t.Generic[TestedClassTypeVar]):

    tst_cls: type[TestedClassTypeVar]

    def build_tst_obj(self) -> TestedClassTypeVar:
        params = self.get_tst_obj_creating_params()
        if params:
            return self.tst_cls(**params)

        return self.tst_cls()

    def get_tst_obj_creating_params(self) -> dict:
        return {}
