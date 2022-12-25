from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class PrinterBase(BaseModel):
    remote_printer_ip: Optional[str] = None
    port_number: Optional[str] = None
    queue_name: Optional[str] = None
    status: Optional[bool] = None

    class Config:
        orm_mode = True


class PrinterCreate(PrinterBase):
    remote_printer_ip: str
    port_number: str
    queue_name: str


class PrinterUpdate(PrinterBase):
    pass


class Printer(PrinterBase):
    id: Optional[UUID]
    user_id: Optional[UUID]

    class Config:
        orm_mode = True
