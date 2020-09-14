from pydantic import BaseModel

"""
Pydantic models.

"""


class EntryBase(BaseModel):
    date: str
    channel: str
    country: str
    os: str
    impressions: int
    clicks: int
    installs: int
    spend: int
    revenue: int

    cpi: int


class EntryCreate(EntryBase):
    pass


class Entry(EntryBase):
    id: int
    date: str
    channel: str
    country: str
    os: str
    impressions: int
    clicks: int
    installs: int
    spend: int
    revenue: int

    cpi: int

    class Config:
        # Read data even if it's not a dict
        orm_mode = True
