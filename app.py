from typing import List, Optional
from fastapi import Depends, FastAPI, Query
from sqlalchemy.orm import Session
import crud, models, schemas
from database import SessionLocal, engine
import uvicorn

# Initialise app
app = FastAPI(debug=True)

models.Base.metadata.create_all(bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Routes

@app.get(
    "/entries",
    response_model=List[schemas.Entry],
)
def get_entries(
    start_date: Optional[str] = Query(None),
    end_date: Optional[str] = Query(None),
    filter_column: Optional[str] = Query(None),
    filter_value: Optional[str] = Query(None),
    sort_column: Optional[str] = Query(None),
    sort_order: Optional[str] = Query(None), # 1 is descending order, 0 is ascending 
    group_by: List[str] = Query(None),
    db: Session = Depends(get_db),
):

    entries = crud.get_entries(
        db,
        start_date=start_date,
        end_date=end_date,
        filter_column=filter_column,
        filter_value=filter_value,
        sort_column=sort_column,
        sort_order=sort_order,
        group_by=group_by,
    )
    return entries


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port="8000")
