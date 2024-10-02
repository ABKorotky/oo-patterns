__all__ = (
    "BaseState",
    "BaseStateContext",
)

import typing as t

from oo_patterns.behavioral.state.interfaces import (
    StateContextInterface,
    StateInterface,
)

StateTypeVar = t.TypeVar("StateTypeVar", bound="BaseState")
StateContextTypeVar = t.TypeVar("StateContextTypeVar", bound="BaseStateContext")


class BaseState(StateInterface[StateContextTypeVar], t.Generic[StateContextTypeVar]):
    _context: StateContextTypeVar

    @property
    def context(self) -> StateContextTypeVar:  # type: ignore
        return self._context

    def set_context(self, context: StateContextTypeVar):
        self._context = context


class BaseStateContext(StateContextInterface[StateTypeVar], t.Generic[StateTypeVar]):
    _state: StateTypeVar

    @property
    def state(self) -> StateTypeVar:
        return self._state

    def set_state(self, state: StateTypeVar):
        self._state = state
        state.set_context(context=self)
        state.init_state()
