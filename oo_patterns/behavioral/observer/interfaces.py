__all__ = (
    "PublisherInterface",
    "AsyncPublisherInterface",
    "SubSpacePublisherInterface",
    "AsyncSubSpacePublisherInterface",
    "EventsManagerInterface",
    "AsyncEventsManagerInterface",
)

import typing as t

if t.TYPE_CHECKING:
    ...


EventContextTypeVar = t.TypeVar("EventContextTypeVar")


class PublisherInterface(t.Generic[EventContextTypeVar]):

    def add_subscribers(self, *args: "t.Callable[[EventContextTypeVar], None]"):
        raise NotImplementedError(f"{self.__class__}.add_subscribers")

    def remove_subscribers(self, *args: "t.Callable[[EventContextTypeVar], None]"):
        raise NotImplementedError(f"{self.__class__}.remove_subscribers")

    def notify_subscribers(self, context: EventContextTypeVar) -> list[Exception]:
        raise NotImplementedError(f"{self.__class__}.notify_subscribers")

    def remove_all_subscribers(self):
        raise NotImplementedError(f"{self.__class__}.remove_all_subscribers")


class AsyncPublisherInterface(t.Generic[EventContextTypeVar]):

    def add_subscribers(
        self,
        *args: "t.Callable[[EventContextTypeVar], t.Coroutine[t.Any, t.Any, None]]",
    ):
        raise NotImplementedError(f"{self.__class__}.add_subscribers")

    def remove_subscribers(
        self,
        *args: "t.Callable[[EventContextTypeVar], t.Coroutine[t.Any, t.Any, None]]",
    ):
        raise NotImplementedError(f"{self.__class__}.remove_subscribers")

    async def notify_subscribers(self, context: EventContextTypeVar) -> list[Exception]:
        raise NotImplementedError(f"{self.__class__}.notify_subscribers")

    def remove_all_subscribers(self):
        raise NotImplementedError(f"{self.__class__}.remove_all_subscribers")


class SubSpacePublisherInterface(t.Generic[EventContextTypeVar]):

    def add_subscribers(
        self, *args: "t.Callable[[EventContextTypeVar], None]", sub_space: t.Any
    ):
        raise NotImplementedError(f"{self.__class__}.add_subscribers")

    def remove_subscribers(
        self, *args: "t.Callable[[EventContextTypeVar], None]", sub_space: t.Any
    ):
        raise NotImplementedError(f"{self.__class__}.remove_subscribers")

    def notify_subscribers(self, context: EventContextTypeVar) -> list[Exception]:
        raise NotImplementedError(f"{self.__class__}.notify_subscribers")

    def get_event_context_sub_space(self, context: EventContextTypeVar) -> t.Any:
        raise NotImplementedError(f"{self.__class__}.get_event_context_sub_space")

    def remove_all_subscribers(self):
        raise NotImplementedError(f"{self.__class__}.remove_all_subscribers")


class AsyncSubSpacePublisherInterface(t.Generic[EventContextTypeVar]):

    def add_subscribers(
        self,
        *args: "t.Callable[[EventContextTypeVar], t.Coroutine[t.Any, t.Any, None]]",
        sub_space: t.Any,
    ):
        raise NotImplementedError(f"{self.__class__}.add_subscribers")

    def remove_subscribers(
        self,
        *args: "t.Callable[[EventContextTypeVar], t.Coroutine[t.Any, t.Any, None]]",
        sub_space: t.Any,
    ):
        raise NotImplementedError(f"{self.__class__}.remove_subscribers")

    async def notify_subscribers(self, context: EventContextTypeVar) -> list[Exception]:
        raise NotImplementedError(f"{self.__class__}.notify_subscribers")

    def get_event_context_sub_space(self, context: EventContextTypeVar) -> t.Any:
        raise NotImplementedError(f"{self.__class__}.get_event_context_sub_space")

    def remove_all_subscribers(self):
        raise NotImplementedError(f"{self.__class__}.remove_all_subscribers")


EventTypeVar = t.TypeVar("EventTypeVar")


class EventsManagerInterface:

    def add_subscriber(
        self,
        event_cls: type[EventTypeVar],
        subscriber: t.Callable[[EventTypeVar], None],
    ):
        raise NotImplementedError(f"{self.__class__}.add_subscriber")

    def remove_subscriber(
        self,
        event_cls: type[EventTypeVar],
        subscriber: t.Callable[[EventTypeVar], None],
    ):
        raise NotImplementedError(f"{self.__class__}.remove_subscriber")

    def notify_subscribers(self, event: EventTypeVar) -> list[Exception]:
        raise NotImplementedError(f"{self.__class__}.notify_subscribers")

    def remove_all_subscribers(self):
        raise NotImplementedError(f"{self.__class__}.remove_all_subscribers")


class AsyncEventsManagerInterface:

    def add_subscriber(
        self,
        event_cls: type[EventTypeVar],
        subscriber: t.Callable[[EventTypeVar], t.Coroutine[t.Any, t.Any, None]],
    ):
        raise NotImplementedError(f"{self.__class__}.add_subscriber")

    def remove_subscriber(
        self,
        event_cls: type[EventTypeVar],
        subscriber: t.Callable[[EventTypeVar], t.Coroutine[t.Any, t.Any, None]],
    ):
        raise NotImplementedError(f"{self.__class__}.remove_subscriber")

    async def notify_subscribers(self, event: EventTypeVar) -> list[Exception]:
        raise NotImplementedError(f"{self.__class__}.notify_subscribers")

    def remove_all_subscribers(self):
        raise NotImplementedError(f"{self.__class__}.remove_all_subscribers")
