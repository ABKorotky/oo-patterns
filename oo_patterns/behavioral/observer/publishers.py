__all__ = (
    "Publisher",
    "AsyncPublisher",
)

import asyncio
import logging
import typing as t

from .interfaces import AsyncPublisherInterface, PublisherInterface

if t.TYPE_CHECKING:
    ...


logger = logging.getLogger(__name__)

EventContextTypeVar = t.TypeVar("EventContextTypeVar")


class Publisher(
    PublisherInterface[EventContextTypeVar], t.Generic[EventContextTypeVar]
):

    def __init__(self):
        self._subscribers: set[t.Callable[[EventContextTypeVar], None]] = set()

    def add_subscribers(self, *args: "t.Callable[[EventContextTypeVar], None]"):
        for s in args:
            if s in self._subscribers:
                continue

            self._subscribers.add(s)
            logger.debug("Publisher: %r. Subscriber is added: %r.", self, s)

    def remove_subscribers(self, *args: "t.Callable[[EventContextTypeVar], None]"):
        for s in args:
            try:
                self._subscribers.remove(s)
            except KeyError:
                pass
            else:
                logger.debug("Publisher: %r. Subscriber is removed: %r.", self, s)

    def notify_subscribers(self, context: EventContextTypeVar):
        for s in self._subscribers:
            try:
                s(context)
            except Exception as err:
                logger.error(
                    "Publisher: %r. Context: %r. Subscriber: %r. Error: %r.",
                    self,
                    context,
                    s,
                    err,
                )
                self.handle_subscriber_error(context=context, error=err)
            else:
                logger.debug(
                    "Publisher: %r. Context: %r. Subscriber: %r. OK.", self, context, s
                )

    def handle_subscriber_error(self, context: EventContextTypeVar, error: Exception):
        pass

    def remove_all_subscribers(self):
        self._subscribers.clear()


class AsyncPublisher(
    AsyncPublisherInterface[EventContextTypeVar], t.Generic[EventContextTypeVar]
):

    def __init__(self):
        self._subscribers: set[
            t.Callable[[EventContextTypeVar], t.Coroutine[t.Any, t.Any, None]]
        ] = set()

    def add_subscribers(
        self,
        *args: "t.Callable[[EventContextTypeVar], t.Coroutine[t.Any, t.Any, None]]",
    ):
        for s in args:
            if s in self._subscribers:
                continue

            self._subscribers.add(s)
            logger.debug("Publisher: %r. Subscriber is added: %r.", self, s)

    def remove_subscribers(
        self,
        *args: "t.Callable[[EventContextTypeVar], t.Coroutine[t.Any, t.Any, None]]",
    ):
        for s in args:
            try:
                self._subscribers.remove(s)
            except KeyError:
                pass
            else:
                logger.debug("Publisher: %r. Subscriber is removed: %r.", self, s)

    async def notify_subscribers(self, context: EventContextTypeVar):
        subscribers, coros = [], []
        for s in self._subscribers:
            subscribers.append(s)
            coros.append(s(context))

        results = await asyncio.gather(*coros, return_exceptions=True)
        for s, result in zip(subscribers, results):
            if isinstance(result, Exception):
                logger.error(
                    "Publisher: %r. Context: %r. Subscriber: %r. Error: %r.",
                    self,
                    context,
                    s,
                    result,
                )
                self.handle_subscriber_error(context=context, error=result)
            else:
                logger.debug(
                    "Publisher: %r. Context: %r. Subscriber: %r. OK.", self, context, s
                )

    def handle_subscriber_error(self, context: EventContextTypeVar, error: Exception):
        pass

    def remove_all_subscribers(self):
        self._subscribers.clear()
