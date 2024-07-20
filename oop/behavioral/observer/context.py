__all__ = ("Publisher",)

import typing as t
import logging
import asyncio

from oop.behavioral.observer.interfaces import ContextPublisherInterface, ContextSubscriberInterface
from oop.behavioral.observer.base import Publisher

if t.TYPE_CHECKING:
    ...

EventContextTypeVar = t.TypeVar("EventContextTypeVar")

logger = logging.getLogger(__name__)


class BaseContextPublisher(ContextPublisherInterface):

    def __init__(self):
        self._context_publishers_map: dict[t.Any, "Publisher"] = {}

    def add_subscriber(self, subscriber: "ContextSubscriberInterface", context: EventContextTypeVar):
        key = self.build_context_subscriber_key(context=context)

        try:
            publisher = self._context_publishers_map[key]
        except KeyError:
            publisher = Publisher()
            self._context_publishers_map[key] = publisher

        publisher.add_subscriber(subscriber=subscriber)

    def remove_subscriber(self, subscriber: "ContextSubscriberInterface"):
        self._subscribers.remove(subscriber)

    async def notify_subscribers(self, context: EventContextTypeVar):
        names, coros = [], []
        for s in self.get_subscribers(context=context):
            names.append(s.name)
            coros.append(s.on_notified(publisher=self))

        results = await asyncio.gather(*coros, return_exceptions=True)
        for name, result in zip(names, results):
            if isinstance(result, Exception):
                logger.error(
                    "Execution subscriber error. Name: %r. Error: %r.", name, result
                )
            else:
                logger.debug("Subscriber is executed. Name: %r.", name)

    def get_subscribers(self, context: EventContextTypeVar) -> t.Iterable["ContextSubscriberInterface"]:
        return (s for s in self._subscribers)
