import docker
from app.config import config

client = docker.from_env()

container = client.containers.run(
    "postgres",
    detach=True,
    ports={"5432/tcp": ("0.0.0.0", 5432)},
    environment=[f"POSTGRES_PASSWORD={config['postgres']['password']}"],
    name="postgres_for_test",
)

print(f"Docker container with postgres is up and ready: {container.id}")
print(f"Don't forget to stop it with command 'docker kill postgres_for_test'")
