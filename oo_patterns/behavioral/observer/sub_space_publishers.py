__all__ = (
    "BaseSubSpacePublisher",
    "BaseAsyncSubSpacePublisher",
)

import logging
import typing as t
from collections import defaultdict

from .interfaces import AsyncSubSpacePublisherInterface, SubSpacePublisherInterface
from .publishers import AsyncPublisher, Publisher

if t.TYPE_CHECKING:
    ...

logger = logging.getLogger(__name__)

EventContextTypeVar = t.TypeVar("EventContextTypeVar")


class BaseSubSpacePublisher(
    SubSpacePublisherInterface[EventContextTypeVar], t.Generic[EventContextTypeVar]
):
    def __init__(self):
        self._sub_spaces_publishers_map: dict[
            t.Any, "Publisher[EventContextTypeVar]"
        ] = defaultdict(Publisher[EventContextTypeVar])

    def add_subscribers(
        self, *args: "t.Callable[[EventContextTypeVar], None]", sub_space: t.Any
    ):
        self._sub_spaces_publishers_map[sub_space].add_subscribers(*args)

    def remove_subscribers(
        self, *args: "t.Callable[[EventContextTypeVar], None]", sub_space: t.Any
    ):
        if sub_space not in self._sub_spaces_publishers_map:
            return

        self._sub_spaces_publishers_map[sub_space].remove_subscribers(*args)

    def notify_subscribers(self, context: EventContextTypeVar) -> list[Exception]:
        sub_space = self.get_event_context_sub_space(context=context)
        if sub_space not in self._sub_spaces_publishers_map:
            return []
        return self._sub_spaces_publishers_map[sub_space].notify_subscribers(
            context=context
        )

    def remove_all_subscribers(self):
        for publisher in self._sub_spaces_publishers_map.values():
            publisher.remove_all_subscribers()
        self._sub_spaces_publishers_map.clear()


class BaseAsyncSubSpacePublisher(
    AsyncSubSpacePublisherInterface[EventContextTypeVar], t.Generic[EventContextTypeVar]
):

    def __init__(self):
        self._sub_spaces_publishers_map: dict[
            t.Any, "AsyncPublisher[EventContextTypeVar]"
        ] = defaultdict(AsyncPublisher[EventContextTypeVar])

    def add_subscribers(
        self,
        *args: "t.Callable[[EventContextTypeVar], t.Coroutine[t.Any, t.Any, None]]",
        sub_space: t.Any,
    ):
        self._sub_spaces_publishers_map[sub_space].add_subscribers(*args)

    def remove_subscribers(
        self,
        *args: "t.Callable[[EventContextTypeVar], t.Coroutine[t.Any, t.Any, None]]",
        sub_space: t.Any,
    ):
        if sub_space not in self._sub_spaces_publishers_map:
            return

        self._sub_spaces_publishers_map[sub_space].remove_subscribers(*args)

    async def notify_subscribers(self, context: EventContextTypeVar) -> list[Exception]:
        sub_space = self.get_event_context_sub_space(context=context)
        if sub_space not in self._sub_spaces_publishers_map:
            return []
        return await self._sub_spaces_publishers_map[sub_space].notify_subscribers(
            context=context
        )

    def remove_all_subscribers(self):
        for publisher in self._sub_spaces_publishers_map.values():
            publisher.remove_all_subscribers()
        self._sub_spaces_publishers_map.clear()
