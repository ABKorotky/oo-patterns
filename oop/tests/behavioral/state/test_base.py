from unittest import TestCase

from oop.behavioral.state import BaseState, BaseStateContext


class BaseTestState(BaseState["TestStateContext"]):

    def transition_to_first(self):
        raise NotImplementedError

    def transition_to_second(self):
        raise NotImplementedError


class FirstTestState(BaseTestState):
    def transition_to_second(self):
        self.context.set_state(state=SecondTestState())


class SecondTestState(BaseTestState):

    def transition_to_first(self):
        self.context.set_state(state=FirstTestState())


class TestStateContext(BaseStateContext["BaseTestState"]):
    def __init__(self):
        self.set_state(state=FirstTestState())

    def transition_to_first(self):
        self.state.transition_to_first()

    def transition_to_second(self):
        self.state.transition_to_second()


class StateTestCase(TestCase):

    def test_state(self):
        tst_ctx = TestStateContext()
        assert isinstance(tst_ctx.state, FirstTestState)

        tst_ctx.transition_to_second()
        assert isinstance(tst_ctx.state, SecondTestState)

        with self.assertRaises(NotImplementedError):
            tst_ctx.transition_to_second()

        tst_ctx.transition_to_first()
        assert isinstance(tst_ctx.state, FirstTestState)

        with self.assertRaises(NotImplementedError):
            tst_ctx.transition_to_first()
