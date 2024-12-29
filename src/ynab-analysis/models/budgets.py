import datetime
import re

from pydantic import BaseModel, ConfigDict, Field

__all__ = ["Budget", "BudgetData"]


class CurrencyFormat(BaseModel):
    model_config = ConfigDict(
        field_title_generator=lambda field_name, field_info: field_name,
        model_title_generator = lambda model: _class_to_underscore_separated(model.__name__)
    )
    
    iso_code: str = Field(default="USD", validate_default=True)
    decimal_digits: int = Field(default=2, validate_default=True)
    decimal_separator: str = Field(default=".", validate_default=True)
    group_separator: str = Field(default=",", validate_default=True)
    currency_separator: str = Field(default="$", validate_default=True)
    symbol_first: bool = Field(default=True, validate_default=True)
    display_symbol: bool = Field(default=True, validate_default=True)


class DateFormat(BaseModel):
    format_: str = Field(alias="format", default="MM/DD/YYYY")


class Budget(BaseModel):
    id: str = Field(frozen=True)
    name: str = Field()
    currency_format: CurrencyFormat = Field(default_factory=CurrencyFormat.__init__)
    last_modified_on: datetime.datetime
    first_month: datetime.datetime
    last_month: datetime.datetime
    date_format: DateFormat


class BudgetData(BaseModel):
    budgets: list[Budget]
    default_budget: str | None = None


def _class_to_underscore_separated(class_name: str) -> str:
    split = re.sub(
        "([A-Z][a-z]+)",
        r" \1",
        re.sub(
            "([A-Z]+)",
            r" \1",
            class_name
        )
    ).split()
    split = map(lambda x: x.lower(), split)
    return "_".join(split)