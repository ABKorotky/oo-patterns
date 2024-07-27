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
    tst_cls: type["PublisherInterface"] = PublisherInterface

    def test_add_subscribers(self):
        tst_obj = self.tst_cls()

        with self.assertRaises(NotImplementedError):
            tst_obj.add_subscribers(Mock(), Mock())

    def test_remove_subscribers(self):
        tst_obj = self.tst_cls()

        with self.assertRaises(NotImplementedError):
            tst_obj.remove_subscribers(Mock(), Mock())

    def test_notify_subscribers(self):
        tst_obj = self.tst_cls()

        with self.assertRaises(NotImplementedError):
            tst_obj.notify_subscribers(context=Mock())

    def test_remove_all_subscribers(self):
        tst_obj = self.tst_cls()

        with self.assertRaises(NotImplementedError):
            tst_obj.remove_all_subscribers()


class AsyncPublisherInterfaceTestCase(IsolatedAsyncioTestCase):
    tst_cls: type["AsyncPublisherInterface"] = AsyncPublisherInterface

    def test_add_subscribers(self):
        tst_obj = self.tst_cls()

        with self.assertRaises(NotImplementedError):
            tst_obj.add_subscribers(Mock(), Mock())

    def test_remove_subscribers(self):
        tst_obj = self.tst_cls()

        with self.assertRaises(NotImplementedError):
            tst_obj.remove_subscribers(Mock(), Mock())

    async def test_notify_subscribers(self):
        tst_obj = self.tst_cls()

        with self.assertRaises(NotImplementedError):
            await tst_obj.notify_subscribers(context=Mock())

    def test_remove_all_subscribers(self):
        tst_obj = self.tst_cls()

        with self.assertRaises(NotImplementedError):
            tst_obj.remove_all_subscribers()


class EventsManagerInterfaceTestCase(TestCase):
    tst_cls: type["EventsManagerInterface"] = EventsManagerInterface

    def test_add_subscriber(self):
        tst_obj = self.tst_cls()

        with self.assertRaises(NotImplementedError):
            tst_obj.add_subscriber(event_cls=Mock, subscriber=Mock())

    def test_remove_subscriber(self):
        tst_obj = self.tst_cls()

        with self.assertRaises(NotImplementedError):
            tst_obj.remove_subscriber(event_cls=Mock, subscriber=Mock())

    def test_notify_subscribers(self):
        tst_obj = self.tst_cls()

        with self.assertRaises(NotImplementedError):
            tst_obj.notify_subscribers(event=Mock())

    def test_remove_all_subscribers(self):
        tst_obj = self.tst_cls()

        with self.assertRaises(NotImplementedError):
            tst_obj.remove_all_subscribers()


class AsyncEventsManagerInterfaceTestCase(IsolatedAsyncioTestCase):
    tst_cls: type["AsyncEventsManagerInterface"] = AsyncEventsManagerInterface

    def test_add_subscribers(self):
        tst_obj = self.tst_cls()

        with self.assertRaises(NotImplementedError):
            tst_obj.add_subscriber(event_cls=Mock, subscriber=Mock())

    def test_remove_subscribers(self):
        tst_obj = self.tst_cls()

        with self.assertRaises(NotImplementedError):
            tst_obj.remove_subscriber(event_cls=Mock, subscriber=Mock())

    async def test_notify_subscribers(self):
        tst_obj = self.tst_cls()

        with self.assertRaises(NotImplementedError):
            await tst_obj.notify_subscribers(event=Mock())

    def test_remove_all_subscribers(self):
        tst_obj = self.tst_cls()

        with self.assertRaises(NotImplementedError):
            tst_obj.remove_all_subscribers()
