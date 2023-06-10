"""add content column to posts

Revision ID: a773d6b57c94
Revises: 12a55613a337
Create Date: 2023-06-10 18:54:54.059414

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a773d6b57c94'
down_revision = '12a55613a337'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        'posts',
        sa.Column('content', sa.String(), nullable=False)
    )


def downgrade() -> None:
    op.drop_column('posts', 'content')
