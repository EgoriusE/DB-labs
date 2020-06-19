"""empty message

Revision ID: aa4f7a08dc50
Revises: c872f001c008
Create Date: 2020-06-18 19:18:07.570573

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aa4f7a08dc50'
down_revision = 'c872f001c008'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('artists_table_creator_fkey', 'artists_table', type_='foreignkey')
    op.create_foreign_key(None, 'artists_table', 'artist', ['creator'], ['name'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'artists_table', type_='foreignkey')
    op.create_foreign_key('artists_table_creator_fkey', 'artists_table', 'group', ['creator'], ['name'])
    # ### end Alembic commands ###