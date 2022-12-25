from app.api.api_v1.endpoints import (
    beverage,
    category,
    cold_side,
    combo,
    dessert,
    hot_side,
    ingredient,
    item,
    login,
    option,
    sauce,
    station,
    user,
    setting,
    alert,
    order,
    printer,
    special,
    vendor,
    request,
    dashboard,
)
from fastapi import APIRouter

api_router = APIRouter()
api_router.include_router(login.router, tags=["sign-in"])
api_router.include_router(user.router, prefix="/user", tags=["user"])
api_router.include_router(dashboard.router, prefix="/dashboard", tags=["dashboard"])
api_router.include_router(item.router, prefix="/item", tags=["item"])
api_router.include_router(combo.router, prefix="/combo", tags=["combo"])
api_router.include_router(special.router, prefix="/special", tags=["special"])
api_router.include_router(beverage.router, prefix="/beverage", tags=["beverage"])
api_router.include_router(dessert.router, prefix="/dessert", tags=["dessert"])
api_router.include_router(category.router, prefix="/category", tags=["category"])
api_router.include_router(sauce.router, prefix="/sauce", tags=["sauce"])
api_router.include_router(hot_side.router, prefix="/hot_side", tags=["hot_side"])
api_router.include_router(cold_side.router, prefix="/cold_side", tags=["cold_side"])
api_router.include_router(ingredient.router, prefix="/ingredient", tags=["ingredient"])
api_router.include_router(option.router, prefix="/option", tags=["option"])
api_router.include_router(station.router, prefix="/station", tags=["station"])
api_router.include_router(setting.router, prefix="/setting", tags=["setting"])
api_router.include_router(printer.router, prefix="/printer", tags=["printer"])
api_router.include_router(alert.router, prefix="/alert", tags=["alert"])
api_router.include_router(order.router, prefix="/order", tags=["order"])
api_router.include_router(vendor.router, prefix="/vendor", tags=["vendor"])
api_router.include_router(request.router, prefix="/request", tags=["request"])
