from app.models.order import Order
from sqlalchemy.orm import Session
from sqlalchemy import and_
from datetime import datetime


class CrudDashboard:
    def get_total_orders_count(self, db: Session) -> int:
        return db.query(Order).count()

    def get_orders_count_per_datatime(
        self, db: Session, *, start_datetime: datetime, end_datetime: datetime
    ) -> int:
        return (
            db.query(Order)
            .filter(
                and_(
                    Order.created_at <= end_datetime, Order.created_at >= start_datetime
                )
            )
            .count()
        )


dashboard = CrudDashboard()
