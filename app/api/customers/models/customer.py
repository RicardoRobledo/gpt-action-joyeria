from typing import List, Optional
import datetime

from sqlalchemy import DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.dialects.mysql import VARCHAR
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.api.base.models.base_models import BaseModel


__author__ = "Ricardo Robledo"
__version__ = "1.0"
__all__ = ["CustomerTypeModel", "CustomerLevelModel", "CustomerDocumentModel"]


class CustomerTypeModel(BaseModel):

    __tablename__ = "customer_types"

    id:Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    customer_type:Mapped[str] = mapped_column(VARCHAR(30), nullable=False)
    created_at:Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now())

    def __repr__(self) -> str:
        return f"CustomerTypeModel(id={self.id}, customer_type={self.customer_type}, created_at={self.created_at})"


class CustomerLevelModel(BaseModel):

    __tablename__ = "customer_levels"

    id:Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    level:Mapped[str] = mapped_column(VARCHAR(30), nullable=False)
    created_at:Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now())

    def __repr__(self) -> str:
        return f"CustomerLevelModel(id={self.id}, customer_level={self.level}, created_at={self.created_at})"


class CustomerDocumentModel(BaseModel):

    __tablename__ = "customer_documents"

    id:Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    document_name:Mapped[str] = mapped_column(VARCHAR(100), nullable=False)
    customer_type_id:Mapped[int] = mapped_column(ForeignKey("customer_types.id"), nullable=False)
    customer_level_id:Mapped[int] = mapped_column(ForeignKey("customer_levels.id"), nullable=False)
    created_at:Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now())

    customer_type:Mapped[CustomerTypeModel] = relationship("CustomerTypeModel", backref="customer_type_back")
    customer_level:Mapped[CustomerLevelModel] = relationship("CustomerLevelModel", backref="customer_level_back")

    def __repr__(self) -> str:
        return f"CustomerDocumentModel(id={self.id}, document_name={self.document_name}, customer_type_id={self.customer_type_id}, customer_level_id={self.customer_level_id}, created_at={self.created_at})"
