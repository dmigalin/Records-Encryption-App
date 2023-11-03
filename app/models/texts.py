from sqlalchemy.orm import Mapped, mapped_column
import time
from db.pgs import Base


class Text(Base):
    __tablename__ = "texts"

    user_id: Mapped[str] = mapped_column(primary_key=True, nullable=False)

    date: Mapped[str] = mapped_column(
        nullable=False, default=time.strftime('%d.%m.%Y',time.localtime()))
    
    time: Mapped[str] = mapped_column(
        nullable=False, default=time.strftime('%H:%M:%S',time.localtime()))
    
    status: Mapped[bool] = mapped_column(default=True)







# from sqlalchemy import MetaData, Table, Column, String, Boolean
# import time
#
# metadata = MetaData
# Texts = Table(
#     'texts',
#     metadata,
#     Column('user_id',String, nullable=False,primary_key=True),
#     Column('date',String, nullable=False,
#            default=time.strftime('%d.%m.%Y',time.localtime())),
#     Column('time',String, nullable=False,
#            default=time.strftime('%H:%M:%S',time.localtime())),
#     Column('status',Boolean(), default=True)
#)