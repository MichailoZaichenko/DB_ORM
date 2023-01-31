from sqlalchemy import create_engine
from sqlalchemy import INTEGER, DATE, TEXT
from sqlalchemy import desc
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Session
from sqlalchemy.orm import relationship

class Base(DeclarativeBase):
    pass



engine = create_engine("sqlite:///orm_db.db")