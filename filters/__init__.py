from .base import *


CommandStart = CommandFilter('start')

CommandHelp = CommandFilter('help')

MyChatFilter = ChatIdFilter(891958065) & ContentTypeFilter('text') # пример фильтра для одного чата