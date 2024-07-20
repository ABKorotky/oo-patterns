__all__ = (
    "PublisherInterface",
    "SubscriberInterface",
    "ContextPublisherInterface",
    "ContextSubscriberInterface",
)

import typing as t

if t.TYPE_CHECKING:
    ...


PublisherTypeVar = t.TypeVar("PublisherTypeVar", bound="PublisherInterface")

EventContextTypeVar = t.TypeVar("EventContextTypeVar")
ContextPublisherTypeVar = t.TypeVar(
    "ContextPublisherTypeVar", bound="ContextPublisherInterface"
)


class PublisherInterface:

    def add_subscriber(self, subscriber: "SubscriberInterface"):
        raise NotImplementedError

    def remove_subscriber(self, subscriber: "SubscriberInterface"):
        raise NotImplementedError

    async def notify_subscribers(self):
        raise NotImplementedError

    def get_subscribers(self) -> t.Iterable["SubscriberInterface"]:
        raise NotImplementedError


class SubscriberInterface(t.Generic[PublisherTypeVar]):
    name: str

    async def on_notified(self, publisher: PublisherTypeVar):
        raise NotImplementedError


class ContextPublisherInterface(t.Generic[EventContextTypeVar]):

    def add_subscriber(
        self, subscriber: "ContextSubscriberInterface", context: EventContextTypeVar
    ):
        raise NotImplementedError

    def remove_subscriber(self, subscriber: "ContextSubscriberInterface"):
        raise NotImplementedError

    def build_context_subscriber_key(self, context: EventContextTypeVar) -> t.Any:
        raise NotImplementedError

    async def notify_subscribers(self, context: EventContextTypeVar):
        raise NotImplementedError

    def get_subscribers(
        self, context: EventContextTypeVar
    ) -> t.Iterable["ContextSubscriberInterface"]:
        raise NotImplementedError


class ContextSubscriberInterface(t.Generic[ContextPublisherTypeVar, EventContextTypeVar]):
    name: str

    async def on_notified(
        self, publisher: ContextPublisherTypeVar, context: EventContextTypeVar
    ):
        raise NotImplementedError
