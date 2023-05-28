import os
from calypso.db.session import SessionLocal
from sqlalchemy.orm import sessionmaker, Session
from calypso.models import ApplicationLog, RequestLog


class CalpysoLoggerClass:
    def __init__(
        self, level: str = "INFO", db: sessionmaker[Session] = SessionLocal
    ) -> None:
        self.session = db
        self.level = level

    def _write_to_db(self, log_object: ApplicationLog | RequestLog) -> None:
        with SessionLocal() as open_db_session:
            open_db_session.add(log_object)
            open_db_session.commit()

    # Default application log methods
    def info(self, info: str, idem: str, module: str) -> None:
        log_entry = ApplicationLog(
            info=info, level="INFO", request_identifier=idem, module=module
        )
        self._write_to_db(log_entry)

    def error(self, info: str, idem: str, module: str) -> None:
        log_entry = ApplicationLog(
            info=info, level="ERROR", request_identifier=idem, module=module
        )
        self._write_to_db(log_entry)

    def debug(self, info: str, idem: str, module: str) -> None:
        if self.level.upper() == "DEBUG":
            print(self.level, info, idem, module)
        else:
            pass

    # Request log methods for the middleware
    def write_to_request_log(
        self,
        request_type: str,
        response_time_ms: float,
        status_code: int,
        request_identifier: str,
        path: str,
    ) -> None:
        log_entry = RequestLog(
            request_type=request_type,
            response_time_ms=response_time_ms,
            status_code=status_code,
            request_identifier=request_identifier,
            path=path,
        )
        self._write_to_db(log_entry)


CalypsoLogger = CalpysoLoggerClass()
