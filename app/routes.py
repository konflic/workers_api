from app import handlers
from src.application import Application


def setup_routes(app: Application):
    app.router.add_get("/", handlers.index)
    app.router.add_get("/workers", handlers.workers)
    app.router.add_get("/workers/{worker_id}", handlers.worker_by_id)
    app.router.add_post("/workers/add", handlers.add_worker)
    app.router.add_patch("/workers/update", handlers.update_worker)
    app.router.add_delete("/workers/delete", handlers.delete_worker)
