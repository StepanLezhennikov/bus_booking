from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from auth.auth import role_required
from .schemas import Route as SRoute, RouteCreate

from database import get_db
from .crud import create_route as create_one_route, get_routes as get_all_routes, get_route as get_one_route, \
    delete_route as delete_one_route
from .validators import validate_bus_id

router = APIRouter(prefix='/route', tags=["Работа с маршрутами"])


@router.post('/', dependencies=[Depends(role_required('admin'))], description="Создание маршрута")
async def create_route(route: RouteCreate, db: AsyncSession = Depends(get_db)) -> SRoute:
    await validate_bus_id(route.bus_id, db)
    return await create_one_route(db, route)


@router.get('/', description="Получить все маршруты")
async def get_routes(db: AsyncSession = Depends(get_db)) -> List[SRoute]:
    return await get_all_routes(db)


@router.get('/{route_id}', description="Получить маршрут")
async def get_route(route_id: int, db: AsyncSession = Depends(get_db)) -> SRoute:
    result = await get_one_route(route_id, db)
    if not result:
        raise HTTPException(status_code=404, detail="Маршрута с таким id нет")
    return result


@router.delete('/{route_id}', dependencies=[Depends(role_required('admin'))], description="Удаление маршрута")
async def delete_route(route_id: int, db: AsyncSession = Depends(get_db)) -> SRoute:
    route = await delete_one_route(route_id, db)
    if not route:
        raise HTTPException(status_code=404, detail="Маршрута с таким id нет")
    return route
