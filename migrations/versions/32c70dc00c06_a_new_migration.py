"""a new migration

Revision ID: 32c70dc00c06
Revises: 021e0c4acebd
Create Date: 2022-05-19 14:12:42.928576

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '32c70dc00c06'
down_revision = '021e0c4acebd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('meals', sa.Column('cost', sa.String(length=255), nullable=True))
    op.drop_column('meals', 'meal_name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('meals', sa.Column('meal_name', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_column('meals', 'cost')
    # ### end Alembic commands ###