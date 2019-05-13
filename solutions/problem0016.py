"""Problem #16 [Easy]

This problem was asked by Twitter.

You run an e-commerce website and want to record the last `N` order ids in a
log. Implement a data structure to accomplish this, with the following API:

- `record(order_id)`: adds the `order_id` to the log;
- `get_last(i)`: gets the `i`th last element from the log. `i` is guaranteed to
  be smaller than or equal to `N`.

You should be as efficient with time and space as possible.
"""

from abc import ABCMeta, abstractmethod
from collections import deque
from typing import Deque, Generic, List, Optional, TypeVar


T = TypeVar('T')


class OrderLog(Generic[T], metaclass=ABCMeta):
    """Order log abstract base class."""

    @abstractmethod
    def record(self, order_id: T) -> None:
        ...

    @abstractmethod
    def get_last(self, i: int) -> Optional[T]:
        ...


class OrderLogDeque(OrderLog[T]):
    """Order log implemented using standard deque data structure."""

    def __init__(self, n: int) -> None:
        self.n = n
        self.order_ids: Deque[T] = deque(maxlen=n)

    def __len__(self):
        return len(self.order_ids)

    def __repr__(self):
        order_ids_str = ', '.join(str(oid) for oid in self.order_ids)
        return (
            f'{self.__class__.__name__}'
            f'(n={self.n}, order_ids=[{order_ids_str}])'
        )

    def record(self, order_id: T) -> None:
        """Add the specified order ID to the log."""

        self.order_ids.append(order_id)

    def get_last(self, i: int) -> Optional[T]:
        """Get the `i`th last element from the log."""

        if i >= len(self):
            return None

        return self.order_ids[-i - 1]


class OrderLogCircularArray(OrderLog[T]):
    """Order log implemented using circular array data structure."""

    def __init__(self, n: int) -> None:
        self.n = n
        self.order_ids: List[Optional[T]] = [None] * n
        self.next_idx = 0
        self.is_filled = False

    def __len__(self):
        return len(self.order_ids) if self.is_filled else self.next_idx

    def __repr__(self):
        order_ids = []
        if self.is_filled:
            order_ids += self.order_ids[self.next_idx:]
        order_ids += self.order_ids[:self.next_idx]

        order_ids_str = ', '.join(str(oid) for oid in order_ids)
        return (
            f'{self.__class__.__name__}'
            f'(n={self.n}, order_ids=[{order_ids_str}])'
        )

    def record(self, order_id: T) -> None:
        """Add the specified order ID to the log."""

        self.order_ids[self.next_idx] = order_id

        self.next_idx = (self.next_idx + 1) % self.n
        if self.next_idx == 0 and not self.is_filled:
            self.is_filled = True

    def get_last(self, i: int) -> Optional[T]:
        """Get the `i`th last element from the log."""

        if i >= len(self):
            return None

        return self.order_ids[(self.next_idx - i - 1 + self.n) % self.n]


if __name__ == '__main__':
    log: OrderLog[int]
    for log in [OrderLogDeque[int](5), OrderLogCircularArray[int](5)]:
        print(f'{log.__class__.__name__} test:')

        for order_id in range(3):
            log.record(order_id)
            print(f'append({order_id}) -> {log}')

        for i in range(4):
            print(f'get_last({i}) -> {log.get_last(i)}')

        for order_id in range(3, 7):
            log.record(order_id)
            print(f'append({order_id}) -> {log}')

        for i in range(6):
            print(f'get_last({i}) -> {log.get_last(i)}')

        print()
