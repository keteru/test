from sqlalchemy import Column, Integer, String, Text
from testapp import Base

class Uriage(Base):
    __tablename__ = "uriage"
    denpyo_no = Column(String(7))
    date = Column(String(15))
    torihikisaki_code = Column(String(4))
    torihikisaki_mei = Column(Text)
    tantosha_code = Column(String(4))
    tantosha_mei = Column(Text)
    no = Column(Integer)
    shohin_code = Column(String(11))
    shohin_mei = Column(Text)
    suryo = Column(Integer)
    tanka = Column(Integer)
    kingaku = Column(Integer)
    biko = Column(Text)
    id = Column(Integer, primary_key=True, autoincrement=True)
    filename = Column(Text)
