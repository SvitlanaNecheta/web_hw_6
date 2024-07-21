from alembic import context
from sqlalchemy import engine_from_config, pool, create_engine
from logging.config import fileConfig
import os

# Alembic Config object
config = context.config

# Interpret the config file for Python logging
fileConfig(config.config_file_name)

# MetaData object for 'autogenerate' support
from models import Base
target_metadata = Base.metadata

# Встановіть URL безпосередньо
DATABASE_URL = 'postgresql://postgres:s4v0e1t6a@localhost:5432/test.db'

def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    context.configure(
        url=DATABASE_URL, target_metadata=target_metadata, literal_binds=True
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """Run migrations in 'online' mode."""
    connectable = create_engine(DATABASE_URL)

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
