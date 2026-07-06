import datetime

type JsonValue = str | int | float | bool | None | datetime.date | datetime.datetime | list[JsonValue] | JsonObj
type JsonObj = dict[str, JsonValue]
