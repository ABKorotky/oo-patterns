__all__ = (
    "StateInterface",
    "StateContextInterface",
)

import typing as t

if t.TYPE_CHECKING:
    ...


StateTypeVar = t.TypeVar("StateTypeVar", bound="StateInterface")
StateContextTypeVar = t.TypeVar("StateContextTypeVar", bound="StateContextInterface")


class StateInterface(t.Generic[StateContextTypeVar]):
    context: StateContextTypeVar

    def set_context(self, context: StateContextTypeVar):
        raise NotImplementedError


class StateContextInterface(t.Generic[StateTypeVar]):

    def set_state(self, state: StateTypeVar):
        raise NotImplementedError
