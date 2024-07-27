__all__ = (
    "PublisherTestCase",
    "AsyncPublisherTestCase",
)

import typing as t
from unittest import IsolatedAsyncioTestCase, TestCase
from unittest.mock import AsyncMock, Mock

from oo_patterns.behavioral.observer.publishers import AsyncPublisher, Publisher
from oo_patterns.tests.helpers import TestingMixin

if t.TYPE_CHECKING:
    ...


PublisherTypeVar = t.TypeVar("PublisherTypeVar", bound=Publisher)


class PublisherTestCase(
    TestingMixin[PublisherTypeVar], TestCase, t.Generic[PublisherTypeVar]
):
    tst_cls = Publisher

    def test_main_flow(self):
        mock_subscriber_one = Mock()
        mock_subscriber_two = Mock(side_effect=Exception("Test"))

        tst_obj = self.build_tst_obj()
        tst_obj.add_subscribers(mock_subscriber_one, mock_subscriber_two)
        tst_obj.add_subscribers(mock_subscriber_one)

        mock_event_context_one = Mock()

        tst_obj.notify_subscribers(context=mock_event_context_one)
        mock_subscriber_one.assert_called_once_with(mock_event_context_one)
        mock_subscriber_two.assert_called_once_with(mock_event_context_one)
        mock_subscriber_one.reset_mock()
        mock_subscriber_two.reset_mock()

        mock_event_context_two = Mock()
        tst_obj.notify_subscribers(context=mock_event_context_two)
        mock_subscriber_one.assert_called_once_with(mock_event_context_two)
        mock_subscriber_two.assert_called_once_with(mock_event_context_two)
        mock_subscriber_one.reset_mock()
        mock_subscriber_two.reset_mock()

        tst_obj.remove_subscribers(mock_subscriber_one, mock_subscriber_two)

        mock_subscriber_not_registered = Mock()
        tst_obj.remove_subscribers(mock_subscriber_not_registered)

        tst_obj.notify_subscribers(context=Mock())
        mock_subscriber_one.assert_not_called()
        mock_subscriber_two.assert_not_called()

        tst_obj.remove_all_subscribers()


AsyncPublisherTypeVar = t.TypeVar("AsyncPublisherTypeVar", bound=AsyncPublisher)


class AsyncPublisherTestCase(
    TestingMixin[AsyncPublisherTypeVar],
    IsolatedAsyncioTestCase,
    t.Generic[AsyncPublisherTypeVar],
):
    tst_cls = AsyncPublisher

    async def test_main_flow(self):
        mock_subscriber_one = AsyncMock()
        mock_subscriber_two = AsyncMock(side_effect=Exception("Test"))

        tst_obj = self.build_tst_obj()
        tst_obj.add_subscribers(mock_subscriber_one, mock_subscriber_two)
        tst_obj.add_subscribers(mock_subscriber_one)

        mock_event_context_one = Mock()

        await tst_obj.notify_subscribers(context=mock_event_context_one)
        mock_subscriber_one.assert_awaited_once_with(mock_event_context_one)
        mock_subscriber_two.assert_awaited_once_with(mock_event_context_one)
        mock_subscriber_one.reset_mock()
        mock_subscriber_two.reset_mock()

        mock_event_context_two = Mock()
        await tst_obj.notify_subscribers(context=mock_event_context_two)
        mock_subscriber_one.assert_awaited_once_with(mock_event_context_two)
        mock_subscriber_two.assert_awaited_once_with(mock_event_context_two)
        mock_subscriber_one.reset_mock()
        mock_subscriber_two.reset_mock()

        tst_obj.remove_subscribers(mock_subscriber_one, mock_subscriber_two)

        mock_subscriber_not_registered = AsyncMock()
        tst_obj.remove_subscribers(mock_subscriber_not_registered)

        await tst_obj.notify_subscribers(context=Mock())
        mock_subscriber_one.assert_not_awaited()
        mock_subscriber_two.assert_not_awaited()

        tst_obj.remove_all_subscribers()
