from typing import List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .models import Route
from .schemas import RouteCreate


async def create_route(db: AsyncSession, route: RouteCreate) -> Route:
    new_route = Route(**route.dict())
    db.add(new_route)
    await db.commit()
    await db.refresh(new_route)
    return new_route


async def get_routes(db: AsyncSession, skip: int = 0, limit: int = 10):
    query = select(Route).offset(skip).limit(limit)
    result = await db.execute(query)
    routes = result.scalars().all()
    return routes


async def get_route(route_id: int, db: AsyncSession):
    query = select(Route).filter(Route.id == route_id)
    result = await db.execute(query)
    route = result.scalar_one_or_none()
    return route


async def delete_route(route_id: int, db: AsyncSession):
    query = select(Route).filter(Route.id == route_id)
    result = await db.execute(query)
    route = result.scalar_one_or_none()
    if route:
        await db.delete(route)
        await db.commit()
    return route
