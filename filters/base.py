from abc import ABC, abstractmethod
from telebot.types import Message
from collections.abc import Mapping


class FilterBase(ABC, Mapping):

    def __and__(self, other):
        return _CombineFilter([self, other], 'and')

    def __or__(self, other):
        return _CombineFilter([self, other], 'or')

    def __getitem__(self, key):
        return self.check

    def __iter__(self):
        yield 'func'

    def __len__(self):
        return 1

    @abstractmethod
    def check(self, msg: Message): ...


class _CombineFilter(FilterBase):
    def __init__(self, filters, rule) -> None:
        super().__init__()
        if rule == 'and':
            self.combo = lambda m: all(f.check(m) for f in filters)
        elif rule == 'or':
            self.combo = lambda m: any(f.check(m) for f in filters)
        else:
            raise ValueError('Unexpected rule of filter combining')

    def check(self, msg: Message):
        return self.combo(msg)


# Фильтр по одной или нескольким командам
class CommandFilter(FilterBase):
    def __init__(self, cmd) -> None:
        super().__init__()
        self.cmd = cmd.rpartition('/')[-1]

    def check(self, msg: Message):
        return msg.text.startswith('/' + self.cmd)


# Фильтр по одному или нескольким типам контента контента
class ContentTypeFilter(FilterBase):
    def __init__(self, content_types) -> None:
        super().__init__()
        if isinstance(content_types, (list, set, tuple)):
            self.content_types = content_types
        else:
            self.content_types = {content_types}

    def check(self, msg: Message):
        return msg.content_type in self.content_types


# Филтр по id пользователя. Может фильтровать как одного, так и нескольких пользователе
class UserIdFilter(FilterBase):
    def __init__(self, user_id) -> None:
        super().__init__()
        if isinstance(user_id, (list, set, tuple)):
            self.ids = set(user_id)
        else:
            self.ids = {user_id}

    def check(self, msg: Message):
        return msg.from_user.id in self.ids


# Фильтр по id чата. Может фильтровать как одного, так и несколько чатов
class ChatIdFilter(UserIdFilter):
    def __init__(self, char_id) -> None:
        super().__init__(char_id)

    def check(self, msg: Message):
        return msg.chat.id in self.ids
