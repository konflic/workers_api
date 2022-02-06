from app import database
from aiohttp import web
from api.models import Worker, UpdateWorker

from pydantic.error_wrappers import ValidationError


async def index(request):
    return web.Response(text="Welcome to Workers database!")


async def workers(request):
    async with request.app["db"].acquire() as conn:
        cursor = await conn.execute(database.workers.select())
        records = await cursor.fetchall()
        questions = [dict(q) for q in records]
        return web.json_response(questions)


async def add_worker(request):
    if request.method == "POST" and request.can_read_body:
        data = await request.json()

        try:
            worker = Worker(**data)
        except ValidationError as error:
            return web.json_response(error, status=400)

        async with request.app["db"].acquire() as conn:
            await conn.execute(database.workers.insert().values(**worker.dict()))
            return web.json_response(worker.json())

    return web.Response(status=400)


async def update_worker(request):
    if request.method == "PATCH" and request.can_read_body:
        async with request.app["db"].acquire() as conn:
            data = await request.json()
            worker_id = data.get("worker_id")

            if not worker_id or not str(worker_id).isnumeric():
                return web.json_response({"error": "worker_id is required as numeric value"}, status=400)

            del data["worker_id"]

            if not data:
                return web.json_response({"error": "add data to adjust"}, status=400)

            try:
                worker = UpdateWorker(**data)
            except ValidationError as error:
                return web.json_response(error, status=400)

            await conn.execute(
                database.workers.update().where(database.workers.c.id == worker_id).values(
                    **worker.dict(exclude_none=True))
            )
            return web.json_response({"success": True, "worker_data": worker.dict(exclude_none=True)}, status=200)

    return web.Response(status=400)


async def delete_worker(request):
    if request.method == "DELETE" and request.can_read_body:
        async with request.app["db"].acquire() as conn:
            data = await request.json()
            worker_id = data.get("worker_id")

            if not worker_id or not str(worker_id).isnumeric():
                return web.json_response({"error": "worker_id is required as numeric value"}, status=400)

            await conn.execute(database.workers.delete().where(database.workers.c.id == worker_id))
            return web.json_response({"success": True, "worker_id": worker_id}, status=200)

    return web.Response(status=400)
