__all__ = ("Publisher",)

import typing as t
import logging
import asyncio

from oop.behavioral.observer.interfaces import PublisherInterface, SubscriberInterface

if t.TYPE_CHECKING:
    ...


logger = logging.getLogger(__name__)


class Publisher(PublisherInterface):

    def __init__(self):
        self._subscribers: set["SubscriberInterface"] = set()

    def add_subscriber(self, subscriber: "SubscriberInterface"):
        self._subscribers.add(subscriber)

    def remove_subscriber(self, subscriber: "SubscriberInterface"):
        self._subscribers.remove(subscriber)

    async def notify_subscribers(self):
        names, coros = [], []
        for s in self.get_subscribers():
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

    def get_subscribers(self) -> t.Iterable["SubscriberInterface"]:
        return (s for s in self._subscribers)
