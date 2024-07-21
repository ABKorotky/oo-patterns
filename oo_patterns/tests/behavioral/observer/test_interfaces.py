import typing as t
from unittest import IsolatedAsyncioTestCase, TestCase
from unittest.mock import Mock

from oo_patterns.behavioral.observer.interfaces import (
    AsyncEventsManagerInterface,
    AsyncPublisherInterface,
    EventsManagerInterface,
    PublisherInterface,
)

if t.TYPE_CHECKING:
    ...


class PublisherInterfaceTestCase(TestCase):

    def test_add_subscribers(self):
        tst_obj: "PublisherInterface" = PublisherInterface()

        with self.assertRaises(NotImplementedError):
            tst_obj.add_subscribers(Mock(), Mock())

    def test_remove_subscribers(self):
        tst_obj: "PublisherInterface" = PublisherInterface()

        with self.assertRaises(NotImplementedError):
            tst_obj.remove_subscribers(Mock(), Mock())

    def test_notify_subscribers(self):
        tst_obj: "PublisherInterface" = PublisherInterface()

        with self.assertRaises(NotImplementedError):
            tst_obj.notify_subscribers(context=Mock())


class AsyncPublisherInterfaceTestCase(IsolatedAsyncioTestCase):

    def test_add_subscribers(self):
        tst_obj: "AsyncPublisherInterface" = AsyncPublisherInterface()

        with self.assertRaises(NotImplementedError):
            tst_obj.add_subscribers(Mock(), Mock())

    def test_remove_subscribers(self):
        tst_obj: "AsyncPublisherInterface" = AsyncPublisherInterface()

        with self.assertRaises(NotImplementedError):
            tst_obj.remove_subscribers(Mock(), Mock())

    async def test_notify_subscribers(self):
        tst_obj: "AsyncPublisherInterface" = AsyncPublisherInterface()

        with self.assertRaises(NotImplementedError):
            await tst_obj.notify_subscribers(context=Mock())


class EventsManagerInterfaceTestCase(TestCase):

    def test_add_subscribers(self):
        tst_obj: "EventsManagerInterface" = EventsManagerInterface()

        with self.assertRaises(NotImplementedError):
            tst_obj.add_subscriber(event_cls=Mock, subscriber=Mock())

    def test_remove_subscribers(self):
        tst_obj: "EventsManagerInterface" = EventsManagerInterface()

        with self.assertRaises(NotImplementedError):
            tst_obj.remove_subscriber(event_cls=Mock, subscriber=Mock())

    def test_notify_subscribers(self):
        tst_obj: "EventsManagerInterface" = EventsManagerInterface()

        with self.assertRaises(NotImplementedError):
            tst_obj.notify_subscribers(event=Mock())


class AsyncEventsManagerInterfaceTestCase(IsolatedAsyncioTestCase):

    def test_add_subscribers(self):
        tst_obj: "AsyncEventsManagerInterface" = AsyncEventsManagerInterface()

        with self.assertRaises(NotImplementedError):
            tst_obj.add_subscriber(event_cls=Mock, subscriber=Mock())

    def test_remove_subscribers(self):
        tst_obj: "AsyncEventsManagerInterface" = AsyncEventsManagerInterface()

        with self.assertRaises(NotImplementedError):
            tst_obj.remove_subscriber(event_cls=Mock, subscriber=Mock())

    async def test_notify_subscribers(self):
        tst_obj: "AsyncEventsManagerInterface" = AsyncEventsManagerInterface()

        with self.assertRaises(NotImplementedError):
            await tst_obj.notify_subscribers(event=Mock())
