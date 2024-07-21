import typing as t
from unittest import IsolatedAsyncioTestCase, TestCase
from unittest.mock import AsyncMock, Mock

from oo_patterns.behavioral.observer.publishers import AsyncPublisher, Publisher

if t.TYPE_CHECKING:
    ...


class PublisherInterfaceTestCase(TestCase):

    def test_main_flow(self):
        mock_subscriber_one = Mock()
        mock_subscriber_two = Mock(side_effect=Exception("Test"))

        tst_obj: "Publisher" = Publisher()
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


class AsyncPublisherInterfaceTestCase(IsolatedAsyncioTestCase):

    async def test_main_flow(self):
        mock_subscriber_one = AsyncMock()
        mock_subscriber_two = AsyncMock(side_effect=Exception("Test"))

        tst_obj: "AsyncPublisher" = AsyncPublisher()
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
