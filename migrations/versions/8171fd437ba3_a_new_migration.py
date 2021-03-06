"""a new migration

Revision ID: 8171fd437ba3
Revises: 
Create Date: 2022-05-17 14:11:45.404726

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8171fd437ba3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('meals', sa.Column('meal_image_path', sa.String(length=255), nullable=True))
    op.add_column('packages', sa.Column('package_image_path', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('packages', 'package_image_path')
    op.drop_column('meals', 'meal_image_path')
    # ### end Alembic commands ###
