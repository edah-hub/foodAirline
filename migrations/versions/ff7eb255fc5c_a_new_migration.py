"""a new migration

Revision ID: ff7eb255fc5c
Revises: a2d2cd05fd0f
Create Date: 2022-05-19 14:18:31.963414

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ff7eb255fc5c'
down_revision = 'a2d2cd05fd0f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('meals', sa.Column('meal_name', sa.String(length=255), nullable=True))
    op.drop_column('meals', 'column')
    op.drop_column('meals', 'meal')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('meals', sa.Column('meal', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.add_column('meals', sa.Column('column', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_column('meals', 'meal_name')
    # ### end Alembic commands ###
