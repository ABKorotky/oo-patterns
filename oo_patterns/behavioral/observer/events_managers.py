__all__ = (
    "EventsManager",
    "AsyncEventsManager",
)

import logging
import typing as t
from collections import defaultdict

from .interfaces import AsyncEventsManagerInterface, EventsManagerInterface
from .publishers import AsyncPublisher, Publisher

if t.TYPE_CHECKING:
    ...


logger = logging.getLogger(__name__)

EventTypeVar = t.TypeVar("EventTypeVar")


class EventsManager(EventsManagerInterface):

    def __init__(self):
        self._events_publishers_map: dict[type, "Publisher"] = defaultdict(Publisher)

    def add_subscriber(
        self,
        event_cls: type[EventTypeVar],
        subscriber: t.Callable[[EventTypeVar], None],
    ):
        self._events_publishers_map[event_cls].add_subscribers(subscriber)

    def remove_subscriber(
        self,
        event_cls: type[EventTypeVar],
        subscriber: t.Callable[[EventTypeVar], None],
    ):
        if event_cls not in self._events_publishers_map:
            return

        self._events_publishers_map[event_cls].remove_subscribers(subscriber)

    def notify_subscribers(self, event: EventTypeVar) -> list[Exception]:
        if event.__class__ not in self._events_publishers_map:
            return []
        return self._events_publishers_map[event.__class__].notify_subscribers(
            context=event
        )

    def remove_all_subscribers(self):
        for publisher in self._events_publishers_map.values():
            publisher.remove_all_subscribers()
        self._events_publishers_map.clear()


class AsyncEventsManager(AsyncEventsManagerInterface):

    def __init__(self):
        self._events_publishers_map: dict[type, "AsyncPublisher"] = defaultdict(
            AsyncPublisher
        )

    def add_subscriber(
        self,
        event_cls: type[EventTypeVar],
        subscriber: t.Callable[[EventTypeVar], t.Coroutine[t.Any, t.Any, None]],
    ):
        self._events_publishers_map[event_cls].add_subscribers(subscriber)

    def remove_subscriber(
        self,
        event_cls: type[EventTypeVar],
        subscriber: t.Callable[[EventTypeVar], t.Coroutine[t.Any, t.Any, None]],
    ):
        if event_cls not in self._events_publishers_map:
            return

        self._events_publishers_map[event_cls].remove_subscribers(subscriber)

    async def notify_subscribers(self, event: EventTypeVar) -> list[Exception]:
        if event.__class__ not in self._events_publishers_map:
            return []
        return await self._events_publishers_map[event.__class__].notify_subscribers(
            context=event
        )

    def remove_all_subscribers(self):
        for publisher in self._events_publishers_map.values():
            publisher.remove_all_subscribers()
        self._events_publishers_map.clear()
