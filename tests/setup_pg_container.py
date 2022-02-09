import docker
from src.config import config

client = docker.from_env()

container = client.containers.run(
    "postgres",
    detach=True,
    ports={"5432/tcp": ("127.0.0.1", 5432)},
    environment=[
        f"POSTGRES_USER={config['postgres']['user']}",
        f"POSTGRES_PASSWORD={config['postgres']['password']}",
        "POSTGRES_HOST_AUTH_METHOD=trust"],
    name="postgres_for_test",
)

print(f"Docker container with postgres is up and ready: {container.id}")
print(f"Don't forget to stop it with command 'docker kill postgres_for_test'")
