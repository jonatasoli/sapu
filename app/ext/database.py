from tortoise import Tortoise
from dynaconf import settings

async def init():
    # Here we connect to a Postgres.
    # also specify the app name of "models"
    # which contain models from "app.models"
    await Tortoise.init(
        db_url=settings.DATABASE_URL,
        modules={'models': ['app.models', "aerich.models"]}
    )


TORTOISE_ORM = {
    "connections": {"default":
    f"settings.DATABASE_URL"},
    "apps": {
        "models": {
            "models": ["models", "aerich.models"],
            "default_connection": "default",
        },
    },
}
