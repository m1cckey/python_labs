from collections import deque
from typing import Any


class Stack:

    def __init__(self):
        self._data: list[Any] = []

    def push(self, item: Any) -> None:
        self._data.append(item)

    def pop(self) -> Any:
        if not self._data:
            raise IndexError("pop from empty Stack")
        return self._data.pop()

    def peek(self) -> Any | None:

        if not self._data:
            return None
        return self._data[-1]

    def is_empty(self) -> bool:
        return len(self._data) == 0

    def __len__(self) -> int:
        return len(self._data)


class Queue:

    def __init__(self):
        self._data: deque[Any] = deque()

    def enqueue(self, item: Any) -> None:

        self._data.append(item)

    def dequeue(self) -> Any:
        if not self._data:
            raise IndexError("dequeue from empty Queue")
        return self._data.popleft()

    def peek(self) -> Any | None:
        if not self._data:
            return None
        return self._data[0]

    def is_empty(self) -> bool:
        return len(self._data) == 0

    def __len__(self) -> int:
        return len(self._data)
