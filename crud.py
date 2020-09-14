from sqlalchemy.orm import Session
import schemas
from models import Entry
from datetime import datetime

"""
Reusable functions for interacting with the data in the database.

"""


def get_entries(
    db: Session,
    start_date: str,
    end_date: str,
    filter_column: str,
    filter_value: str,
    sort_column: str,
    sort_order: int,
    group_by: list,
):

    entries = db.query(Entry)
    if start_date:
        # filter by start date
        date_object_start = datetime.strptime(start_date, "%Y-%m-%d").date()
        entries = entries.filter(Entry.date >= date_object_start)
    if end_date:
        # filter by end date
        date_object_end = datetime.strptime(end_date, "%Y-%m-%d").date()
        entries = entries.filter(Entry.date <= date_object_end)
    if filter_column and filter_value:
        # filter by column
        entries = entries.filter(Entry.__table__.c[filter_column] == filter_value)
    if group_by:
        # group by columns
        entries = entries.group_by(*group_by)
    if sort_order:
        # Sort order 1 = descending, 0 = ascending
        entries = (
            entries.order_by(Entry.__table__.c[sort_column].desc())
            if int(sort_order) == 1
            else entries
        )

    return entries.all()
