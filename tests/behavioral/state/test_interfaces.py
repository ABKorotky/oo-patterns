import typing as t
from unittest import TestCase

from oo_patterns.behavioral.state.interfaces import (
    StateContextInterface,
    StateInterface,
)

if t.TYPE_CHECKING:
    ...


class StateInterfaceTestCase(TestCase):

    def test_set_context(self):
        tst_obj: "StateInterface" = StateInterface()

        with self.assertRaises(NotImplementedError):
            tst_obj.set_context(context=StateContextInterface())


class StateContextInterfaceTestCase(TestCase):

    def test_set_state(self):
        tst_obj: "StateContextInterface" = StateContextInterface()

        with self.assertRaises(NotImplementedError):
            tst_obj.set_state(state=StateInterface())
