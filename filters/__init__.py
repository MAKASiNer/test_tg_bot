from .base import CommandFilter, ChatIdFilter, ContentTypeFilter


CommandStart = CommandFilter('start')

MyChatFilter = ChatIdFilter(891958065) & ContentTypeFilter('text')