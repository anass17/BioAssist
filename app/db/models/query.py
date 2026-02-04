from sqlalchemy import Column, Integer, String, TIMESTAMP, func
from db.base import Base

class Query(Base):
    __tablename__ = "queries"

    id = Column(Integer, primary_key=True, index=True)
    query = Column(String, nullable=False)
    reponse = Column(String, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())