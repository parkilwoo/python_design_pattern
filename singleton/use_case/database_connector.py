"""_summary_
    여러개의 서비스가 한개의 DB를 공유하는 구조.
    안정된 서비스를 설계하려면 다음 사항들을 반드시 명심해야 한다.
    * 데이터베이스 작업 간에 일관성이 유지돼야 한다. 작업 간 충돌이 발생하지 않아야 한다.
    * 다수의 DB 연산을 처리하려면 메모리와 CPU를 효율적으로 사용해야 한다.
"""
import sqlite3
from typing import Any
class MetaSingleton(type):
    _instance = {}
    def __call__(cls, *args: Any, **kwds: Any) -> Any:
        if cls not in cls._instance:
            cls._instance[cls] = super(MetaSingleton, cls).__call__(*args, \
                **kwds)
        return cls._instance[cls]
    
class Database(metaclass=MetaSingleton):
    connection = None
    def connect(self):
        if self.connection is None:
            self.connection = sqlite3.connect("db.sqlite3")
            self.cursorobj = self.connection.cursor()
        return self.cursorobj
    
db1 = Database().connect()
db2 = Database().connect()

print("Database Objects DB1", db1)
print("Database Objects DB2", db2)