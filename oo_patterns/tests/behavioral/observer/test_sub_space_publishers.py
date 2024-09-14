__all__ = (
    "PublisherTestCase",
    "AsyncPublisherTestCase",
)

import typing as t
from unittest import IsolatedAsyncioTestCase, TestCase
from unittest.mock import AsyncMock, Mock

from oo_patterns.behavioral.observer.sub_space_publishers import (
    BaseAsyncSubSpacePublisher,
    BaseSubSpacePublisher,
)
from oo_patterns.tests.helpers import TestingMixin

if t.TYPE_CHECKING:
    ...


TST_SUB_SPACE_ONE = "first"
TST_SUB_SPACE_TWO = "second"


EventContextTypeVar = t.TypeVar("EventContextTypeVar")


class TstSubSpacePublisher(BaseSubSpacePublisher):

    def get_event_context_sub_space(self, context: EventContextTypeVar) -> t.Any:
        return context.sub_space


class TstAsyncSubSpacePublisher(BaseAsyncSubSpacePublisher):

    def get_event_context_sub_space(self, context: EventContextTypeVar) -> t.Any:
        return context.sub_space


class PublisherTestCase(
    TestingMixin[TstSubSpacePublisher],
    TestCase,
):
    tst_cls = TstSubSpacePublisher

    def test_main_flow(self):
        mock_subscriber_one = Mock()
        tst_error = Exception("Test")
        mock_subscriber_two = Mock(side_effect=tst_error)

        tst_obj = self.build_tst_obj()
        tst_obj.add_subscribers(mock_subscriber_one, sub_space=TST_SUB_SPACE_ONE)
        tst_obj.add_subscribers(mock_subscriber_two, sub_space=TST_SUB_SPACE_TWO)

        mock_event_context_one = Mock(sub_space=TST_SUB_SPACE_ONE)

        tst_res = tst_obj.notify_subscribers(context=mock_event_context_one)
        assert tst_res == []
        mock_subscriber_one.assert_called_once_with(mock_event_context_one)
        mock_subscriber_two.assert_not_called()
        mock_subscriber_one.reset_mock()
        mock_subscriber_two.reset_mock()

        mock_event_context_two = Mock(sub_space=TST_SUB_SPACE_TWO)
        tst_res = tst_obj.notify_subscribers(context=mock_event_context_two)
        assert tst_res == [tst_error]
        mock_subscriber_one.assert_not_called()
        mock_subscriber_two.assert_called_once_with(mock_event_context_two)
        mock_subscriber_one.reset_mock()
        mock_subscriber_two.reset_mock()

        tst_obj.remove_subscribers(mock_subscriber_one, sub_space=TST_SUB_SPACE_ONE)
        tst_obj.remove_subscribers(mock_subscriber_two, sub_space=TST_SUB_SPACE_TWO)

        mock_subscriber_not_registered = Mock()
        tst_obj.remove_subscribers(mock_subscriber_not_registered, sub_space=Mock())

        tst_res = tst_obj.notify_subscribers(context=Mock(sub_space="missed"))
        assert tst_res == []
        mock_subscriber_one.assert_not_called()
        mock_subscriber_two.assert_not_called()

        tst_obj.remove_all_subscribers()


class AsyncPublisherTestCase(
    TestingMixin[TstAsyncSubSpacePublisher],
    IsolatedAsyncioTestCase,
):
    tst_cls = TstAsyncSubSpacePublisher

    async def test_main_flow(self):
        mock_subscriber_one = AsyncMock()
        tst_error = Exception("Test")
        mock_subscriber_two = AsyncMock(side_effect=tst_error)

        tst_obj = self.build_tst_obj()
        tst_obj.add_subscribers(mock_subscriber_one, sub_space=TST_SUB_SPACE_ONE)
        tst_obj.add_subscribers(mock_subscriber_two, sub_space=TST_SUB_SPACE_TWO)

        mock_event_context_one = Mock(sub_space=TST_SUB_SPACE_ONE)

        tst_res = await tst_obj.notify_subscribers(context=mock_event_context_one)
        assert tst_res == []
        mock_subscriber_one.assert_awaited_once_with(mock_event_context_one)
        mock_subscriber_two.assert_not_awaited()
        mock_subscriber_one.reset_mock()
        mock_subscriber_two.reset_mock()

        mock_event_context_two = Mock(sub_space=TST_SUB_SPACE_TWO)
        tst_res = await tst_obj.notify_subscribers(context=mock_event_context_two)
        assert tst_res == [tst_error]
        mock_subscriber_one.assert_not_awaited()
        mock_subscriber_two.assert_awaited_once_with(mock_event_context_two)
        mock_subscriber_one.reset_mock()
        mock_subscriber_two.reset_mock()

        tst_obj.remove_subscribers(mock_subscriber_one, sub_space=TST_SUB_SPACE_ONE)
        tst_obj.remove_subscribers(mock_subscriber_two, sub_space=TST_SUB_SPACE_TWO)

        mock_subscriber_not_registered = AsyncMock()
        tst_obj.remove_subscribers(mock_subscriber_not_registered, sub_space=Mock())

        tst_res = await tst_obj.notify_subscribers(context=Mock(sub_space="missed"))
        assert tst_res == []
        mock_subscriber_one.assert_not_awaited()
        mock_subscriber_two.assert_not_awaited()

        tst_obj.remove_all_subscribers()
