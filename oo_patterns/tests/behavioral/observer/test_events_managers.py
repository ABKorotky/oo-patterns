import typing as t
from dataclasses import dataclass
from unittest import IsolatedAsyncioTestCase, TestCase
from unittest.mock import AsyncMock, Mock

from oo_patterns.behavioral.observer import AsyncEventsManager, EventsManager

if t.TYPE_CHECKING:
    ...


@dataclass
class TestEventOne:
    f_int: int


@dataclass
class TestEventTwo:
    f_str: str


@dataclass
class TestEventNotRegistered:
    f_bool: bool


class EventsManagerTestCase(TestCase):

    def test_main_flow(self):
        mock_subscriber_one = Mock()
        mock_subscriber_two = Mock(side_effect=Exception("Test"))

        tst_obj: "EventsManager" = EventsManager()
        tst_obj.add_subscriber(event_cls=TestEventOne, subscriber=mock_subscriber_one)
        tst_obj.add_subscriber(event_cls=TestEventTwo, subscriber=mock_subscriber_two)

        test_event_one = TestEventOne(f_int=12)
        tst_obj.notify_subscribers(event=test_event_one)
        mock_subscriber_one.assert_called_once_with(test_event_one)
        mock_subscriber_two.assert_not_called()
        mock_subscriber_one.reset_mock()

        test_event_two = TestEventTwo(f_str="test")
        tst_obj.notify_subscribers(event=test_event_two)
        mock_subscriber_one.assert_not_called()
        mock_subscriber_two.assert_called_once_with(test_event_two)
        mock_subscriber_two.reset_mock()

        test_event_not_registered = TestEventNotRegistered(f_bool=True)
        tst_obj.notify_subscribers(event=test_event_not_registered)
        mock_subscriber_one.assert_not_called()
        mock_subscriber_two.assert_not_called()
        mock_subscriber_one.reset_mock()
        mock_subscriber_two.reset_mock()

        tst_obj.remove_subscriber(
            event_cls=TestEventOne, subscriber=mock_subscriber_one
        )
        tst_obj.remove_subscriber(
            event_cls=TestEventTwo, subscriber=mock_subscriber_two
        )

        mock_subscriber_not_registered = Mock()
        tst_obj.remove_subscriber(
            event_cls=TestEventNotRegistered, subscriber=mock_subscriber_not_registered
        )

        tst_obj.notify_subscribers(event=test_event_one)
        tst_obj.notify_subscribers(event=test_event_two)
        mock_subscriber_one.assert_not_called()
        mock_subscriber_two.assert_not_called()
        mock_subscriber_one.reset_mock()
        mock_subscriber_two.reset_mock()


class AsyncEventsManagerTestCase(IsolatedAsyncioTestCase):

    async def test_main_flow(self):
        mock_subscriber_one = AsyncMock()
        mock_subscriber_two = AsyncMock(side_effect=Exception("Test"))

        tst_obj: "AsyncEventsManager" = AsyncEventsManager()
        tst_obj.add_subscriber(event_cls=TestEventOne, subscriber=mock_subscriber_one)
        tst_obj.add_subscriber(event_cls=TestEventTwo, subscriber=mock_subscriber_two)

        test_event_one = TestEventOne(f_int=12)
        await tst_obj.notify_subscribers(event=test_event_one)
        mock_subscriber_one.assert_awaited_once_with(test_event_one)
        mock_subscriber_two.assert_not_awaited()
        mock_subscriber_one.reset_mock()

        test_event_two = TestEventTwo(f_str="test")
        await tst_obj.notify_subscribers(event=test_event_two)
        mock_subscriber_one.assert_not_awaited()
        mock_subscriber_two.assert_awaited_once_with(test_event_two)
        mock_subscriber_two.reset_mock()

        test_event_not_registered = TestEventNotRegistered(f_bool=True)
        await tst_obj.notify_subscribers(event=test_event_not_registered)
        mock_subscriber_one.assert_not_awaited()
        mock_subscriber_two.assert_not_awaited()
        mock_subscriber_one.reset_mock()
        mock_subscriber_two.reset_mock()

        tst_obj.remove_subscriber(
            event_cls=TestEventOne, subscriber=mock_subscriber_one
        )
        tst_obj.remove_subscriber(
            event_cls=TestEventTwo, subscriber=mock_subscriber_two
        )

        mock_subscriber_not_registered = Mock()
        tst_obj.remove_subscriber(
            event_cls=TestEventNotRegistered, subscriber=mock_subscriber_not_registered
        )

        await tst_obj.notify_subscribers(event=test_event_one)
        await tst_obj.notify_subscribers(event=test_event_two)
        mock_subscriber_one.assert_not_awaited()
        mock_subscriber_two.assert_not_awaited()
        mock_subscriber_one.reset_mock()
        mock_subscriber_two.reset_mock()
