"""add foreignkey to posts

Revision ID: 6df69e2f8354
Revises: a057dd7600b0
Create Date: 2023-06-10 19:07:53.562816

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6df69e2f8354'
down_revision = 'a057dd7600b0'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        'posts',
        sa.Column('owner_id', sa.Integer(), nullable=False)
    )
    op.create_foreign_key('posts_users_fk',
                          source_table='posts', referent_table='users',
                          local_cols=['owner_id'], remote_cols=['id'], ondelete='CASCADE')


def downgrade() -> None:
    op.drop_constraint('posts_users_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')
