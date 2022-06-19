#created by by @Arjun_La_Lis_A - tg
#use with proper credits

import random
from pyrogram import Client, filters
from info import COMMAND_HAND_LER
from plugins.helper_functions.cust_p_filters import f_onw_fliter


IKKA_STRINGS = (
    "CAACAgIAAxkBAAIDm2Ku1QZ-sgvcSx9XgiMT0ipeEfNqAAIKHQACwaggSQiNN_5i8NF4HgQ",
    "CAACAgIAAxkBAAIDoWKu1Td2P22VKwU3JaZdnZ3cQEBEAAIbFAACT1VwSf8R3UMpnjhZHgQ",
    "CAACAgUAAxkBAAIDUmIN8bqiD5DYQLjQzUwH7-1AsH0eAAJGBAAClj7wVxJlL3v8QuaoHgQ",
    "CAACAgUAAxkBAAIDVmIN8cCiVJZl05m0wiggUJaOvYarAAL5BAACo7lRVClze9Et3bCJHgQ",
    "CAACAgIAAxkBAAIDpGKu1UM8R8DOg01NFLcRcxOMjeaZAAL2EgACKf1ISWa82rO4MQcqHgQ",
    "CAACAgUAAxkBAAIDV2IN8cSKz20_0T-f7BlHVQfQYPu_AAKfAwACA4rwV01BOgyNllX1HgQ",
    "CAACAgUAAxkBAAIDuWKu1jTmLX-wQ9PJcX8lCPsH_YAoAAITAwACMC-pVLw9VWKp1ITyHgQ",
    "CAACAgIAAxkBAAIDtWKu1d7mW8dG13PrjtNKRkl9u_dZAALRFAAC_uKhSUgTcUzavgjYHgQ",
    "CAACAgIAAxkBAAIDqmKu1WmQs-ywRZU60FBbJpcGxNfdAAL6FQACgb8QSU-cnfCjPKF6HgQ",
    "CAACAgUAAxkBAAIDWGIN8coT1jTnXpetiFOKVGZVCX78AAJLBAACrXgAAVTcB_E8ndEu0h4E",
    "CAACAgUAAxkBAAIDumKu1i6HN_4XRt5X7kQ8rHwParAhAAKVBwACK3ZgV-PrCds8EyJ0HgQ",
    "CAACAgUAAxkBAAIDWWIN8c-GSo6HX8bmIvJOwDXG1pJ-AAJkBAACbYZIVIF7psBskaRiHgQ",
    "CAACAgUAAxkBAAIDWmIN8dfwrILfwAABBczAR4DoYxpkvAACvwUAAlNOSFRraTuQ8L5Qzx4E",
    "CAACAgUAAxkBAAIDsmKu1ccvXZ4mTHQemmYw2M9DYeaGAAIpAwACPZgJVbNVsSlbrQVnHgQ",
    "CAACAgUAAxkBAAIDXGIN8eN4RRZPSvKW5OcDhBGnF_qIAAJtBQACwq0JVAnAmIgTMZr6HgQ",
    "CAACAgUAAxkBAAIDeGIN8ke0Qm7S8rWAp5XRHtG21RP1AAJzBQACg5tAVL8bVAS2wafYHgQ",
    "CAACAgUAAxkBAAIDfGIN8lvvH0C9VGSLMV7fvxJ9L_r9AAIlBgACf4hJVA_SXDgpTipeHgQ",
    "CAACAgUAAxkBAAIDf2IN8nL54y-xsW_PGMX5T96e_ErnAAJiAwACjh3YV6f4T7ZwQqExHgQ",
    "CAACAgUAAxkBAAIDgmIN8oZFf70SfKUOl9nnk0Q0uIGPAAJjAwAC3-lRVqPrbp8AAeUBch4E",
    "CAACAgUAAxkBAAIDj2IN86K_5xEpxc00sVRoFLgNgvh_AALeAgACh49oVh2VB0KUEX3zHgQ",
    "CAACAgUAAxkBAAIDkmIN87LWn-56jo9wHTdifHsdBCAiAAJPAwACK4yZVlCyU1tXbk2YHgQ",
    "CAACAgUAAxkBAAIDTWIN7t5h_8P6FDH-fkeliFYtuTSoAAJaBAAC78rxVyVXsqnnB2vXHgQ",
)


@Client.on_message(
    filters.command("ikka", COMMAND_HAND_LER) &
    f_onw_fliter
)
async def ikka(_, message):
    """ /ikka strings """
    effective_string = random.choice(IKKA_STRINGS)
    if message.reply_to_message:
        await message.reply_to_message.reply_sticker(effective_string)
    else:
        await message.reply_sticker(effective_string)
