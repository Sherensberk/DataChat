from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, registry

class User:
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    email: Mapped[str] = mapped_column(unique=True)
    username: Mapped[str]
    password_hash: Mapped[str]

    created_at: Mapped[datetime] = mapped_column( init=False, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column( init=False, server_default=func.now(), onupdate=func.now())