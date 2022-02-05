from app import db
from aiohttp import web
from api.models import Worker

from pydantic.error_wrappers import ValidationError


async def index(request):
    return web.Response(text="Welcome to Workers database!")


async def workers(request):
    async with request.app["db"].acquire() as conn:
        cursor = await conn.execute(db.workers.select())
        records = await cursor.fetchall()
        questions = [dict(q) for q in records]
        return web.Response(text=str(questions))


async def add_worker(request):
    if request.method == "POST" and request.can_read_body:
        data = await request.json()

        try:
            worker = Worker(**data)
        except ValidationError as error:
            return web.Response(status=400, text=str(error))

        async with request.app["db"].acquire() as conn:
            await conn.execute(db.workers.insert().values(**worker.dict()))
            return web.Response(text=str(worker))

    return web.Response(status=400)


async def update_worker(request):
    async with request.app["db"].acquire() as conn:
        pass


async def delete_worker(request):
    async with request.app["db"].acquire() as conn:
        pass
