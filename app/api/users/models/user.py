from typing import List, Optional
import datetime

from sqlalchemy import DateTime, Boolean, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.dialects.mysql import VARCHAR, ENUM, INTEGER
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.api.base.models.base_models import BaseModel


__author__ = "Ricardo Robledo"
__version__ = "1.0"
__all__ = ["UserModel", "UserActionModel", "UserWeakPointModel", "UserStrongPointModel"]


class UserModel(BaseModel):

    __tablename__ = "users"

    id:Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name:Mapped[str] = mapped_column(VARCHAR(30), nullable=False)
    middle_name:Mapped[str] = mapped_column(VARCHAR(30), nullable=False)
    last_name:Mapped[str] = mapped_column(VARCHAR(30), nullable=False)
    username:Mapped[str] = mapped_column(VARCHAR(30), nullable=False, unique=True)
    password:Mapped[str] = mapped_column(VARCHAR(255), nullable=False, unique=True)
    is_active:Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    is_superuser:Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    created_at:Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at:Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now(), onupdate=func.now())

    def __repr__(self) -> str:
        return f"User(id={self.id}, name={self.name}, middle_name={self.middle_name}, last_name={self.last_name}, username={self.username}, password={self.password}, is_active={self.is_active}, is_superuser={self.is_superuser}, created_at={self.created_at}, updated_at={self.updated_at})"


class UserActionModel(BaseModel):

    __tablename__ = "user_actions"

    id:Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id:Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    method:Mapped[ENUM] = mapped_column(ENUM("GET", "POST", "PUT", "PATCH", "DELETE"), nullable=False)
    path:Mapped[str] = mapped_column(VARCHAR(255), nullable=False)
    status_code:Mapped[int] = mapped_column(INTEGER, nullable=False)
    created_at:Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now())

    user:Mapped[UserModel] = relationship("UserModel", backref="user_action_back")

    def __repr__(self) -> str:
        return f"UserAction(id={self.id}, user_id={self.user_id}, method={self.method}, path={self.path}, created_at={self.created_at})"


class WeakPointModel(BaseModel):

    __tablename__ = "weak_points"

    id:Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id:Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    weakness:Mapped[str] = mapped_column(VARCHAR(100), nullable=False)
    created_at:Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now())

    user:Mapped[UserModel] = relationship("UserModel", backref="user_weak_point_back")

    def __repr__(self) -> str:
        return f"WeakPoint(id={self.id}, user_id={self.user_id}, weakness={self.weakness}, created_at={self.created_at})"


class StrongPointModel(BaseModel):

    __tablename__ = "strong_points"

    id:Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id:Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    strength:Mapped[str] = mapped_column(VARCHAR(100), nullable=False)
    created_at:Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now())

    user:Mapped[UserModel] = relationship("UserModel", backref="user_strong_point_back")

    def __repr__(self) -> str:
        return f"StrongPoint(id={self.id}, user_id={self.user_id}, strength={self.strength}, created_at={self.created_at})"
