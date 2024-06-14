from typing import List, Optional
import datetime

from sqlalchemy import DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.dialects.mysql import MEDIUMTEXT, VARCHAR
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.api.base.models.base_models import BaseModel


__author__ = "Ricardo Robledo"
__version__ = "1.0"
__all__ = ["Topic", "TrainingDocument"]


class TopicModel(BaseModel):

    __tablename__ = "topics"

    id:Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    topic_name:Mapped[str] = mapped_column(VARCHAR(255), nullable=False)
    created_at:Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now())

    def __repr__(self) -> str:
        return f"Topic(id={self.id}, topic_name={self.topic_name}), created_at={self.created_at}"


class TrainingDocumentModel(BaseModel):

    __tablename__ = "training_documents"

    id:Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    topic_id:Mapped[int] = mapped_column(ForeignKey("topics.id"), nullable=False)
    document_name:Mapped[str] = mapped_column(VARCHAR(200), nullable=False)
    content:Mapped[str] = mapped_column(MEDIUMTEXT, nullable=False)
    created_at:Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at:Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now(), onupdate=func.now())

    topic:Mapped[TopicModel] = relationship("TopicModel", backref="topic_model_back")

    def __repr__(self) -> str:
        return f"TrainingDocument(id={self.id}, topic_id={self.topic_id}, document_name={self.document_name}, content={self.content}, created_at={self.created_at}"
