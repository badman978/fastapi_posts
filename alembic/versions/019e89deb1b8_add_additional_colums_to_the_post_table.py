"""add additional colums to the post table

Revision ID: 019e89deb1b8
Revises: 5bf043d9e89b
Create Date: 2023-05-30 22:14:59.450911

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '019e89deb1b8'
down_revision = '5bf043d9e89b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, server_default="TRUE"))
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
