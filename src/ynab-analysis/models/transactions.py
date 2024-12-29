import datetime

from pydantic import BaseModel, Field

__all__ = ["Transaction", "Subtransaction"]

class Transaction(BaseModel):
    id_: str = Field(alias="id", frozen=True)
    date: datetime.datetime
    amount: int
    memo: str | None = Field(default=None)
    cleared: str | None = Field(default=None)  # should be an enum
    approved: bool
    account_id: str | None = Field(default=None)
    account_name: str | None = Field(default=None)
    payee_id: str | None = Field(default=None)
    payee_name: str | None = Field(default=None)
    transfer_transaction_id: str | None = Field(default=None)
    matched_transaction_id: str | None = Field(default=None)
    flag_color: str | None = Field(default=None)
    debt_transaction_type: str | None = Field(default=None)
    deleted: bool = Field(default=True)
    subtransactions: list[Subtransaction] = Field(default_factory=list)


class Subtransaction(BaseModel):
    id_: str = Field(alias="id", frozen=True)
    transaction_id: str
    amount: float
    memo: str | None = Field(default=None)
    payee_id: str | None = Field(default=None)
    payee_name: str | None = Field(default=None)
    category_id: str | None = Field(default=None)
    category_name: str | None = Field(default=None)
    transfer_account_id: str | None = Field(default=None)
    transfer_transaction_id: str | None = Field(default=None)
    deleted: bool = Field(default=False)
