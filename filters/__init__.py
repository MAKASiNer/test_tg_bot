from .base import *


CommandStart = CommandFilter('start')

CommandHelp = CommandFilter('help')

CommandWeek = CommandFilter('week')

CommandToday = CommandFilter('today')

CommandTomorrow = CommandFilter('tomorrow')

MyChatFilter = ChatIdFilter(891958065) & ContentTypeFilter('text') # пример фильтра для одного чата