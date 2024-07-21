__all__ = (
    "PublisherInterface",
    "AsyncPublisherInterface",
    "EventsManagerInterface",
    "AsyncEventsManagerInterface",
)

import typing as t

if t.TYPE_CHECKING:
    ...


EventContextTypeVar = t.TypeVar("EventContextTypeVar")


class PublisherInterface(t.Generic[EventContextTypeVar]):

    def add_subscribers(self, *args: "t.Callable[[EventContextTypeVar], None]"):
        raise NotImplementedError

    def remove_subscribers(self, *args: "t.Callable[[EventContextTypeVar], None]"):
        raise NotImplementedError

    def notify_subscribers(self, context: EventContextTypeVar):
        raise NotImplementedError


class AsyncPublisherInterface(t.Generic[EventContextTypeVar]):

    def add_subscribers(
        self,
        *args: "t.Callable[[EventContextTypeVar], t.Coroutine[t.Any, t.Any, None]]",
    ):
        raise NotImplementedError

    def remove_subscribers(
        self,
        *args: "t.Callable[[EventContextTypeVar], t.Coroutine[t.Any, t.Any, None]]",
    ):
        raise NotImplementedError

    async def notify_subscribers(self, context: EventContextTypeVar):
        raise NotImplementedError


EventTypeVar = t.TypeVar("EventTypeVar")


class EventsManagerInterface:

    def add_subscriber(
        self,
        event_cls: type[EventTypeVar],
        subscriber: t.Callable[[EventTypeVar], None],
    ):
        raise NotImplementedError

    def remove_subscriber(
        self,
        event_cls: type[EventTypeVar],
        subscriber: t.Callable[[EventTypeVar], None],
    ):
        raise NotImplementedError

    def notify_subscribers(self, event: EventTypeVar):
        raise NotImplementedError


class AsyncEventsManagerInterface:

    def add_subscriber(
        self,
        event_cls: type[EventTypeVar],
        subscriber: t.Callable[[EventTypeVar], t.Coroutine[t.Any, t.Any, None]],
    ):
        raise NotImplementedError

    def remove_subscriber(
        self,
        event_cls: type[EventTypeVar],
        subscriber: t.Callable[[EventTypeVar], t.Coroutine[t.Any, t.Any, None]],
    ):
        raise NotImplementedError

    async def notify_subscribers(self, event: EventTypeVar):
        raise NotImplementedError
