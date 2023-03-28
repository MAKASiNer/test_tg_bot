from .base import *


CommandStart = CommandFilter('start')
СommandHelp = CommandFilter('help')

MyChatFilter = ChatIdFilter(891958065) & ContentTypeFilter('text')