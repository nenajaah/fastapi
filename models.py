from sqlalchemy import Column, Integer, String
from database import Base


class Entry(Base):
    __tablename__ = "entry"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(
        String
    )  # Could also be date object but available date string format is easily sortable
    channel = Column(String)
    country = Column(String)
    os = Column(String)
    impressions = Column(Integer)
    clicks = Column(Integer)
    installs = Column(Integer)
    spend = Column(Integer)
    revenue = Column(Integer)

    # Derived metric CPI (cost per install) which is calculated as cpi = spend / installs
    cpi = Column(Integer)
