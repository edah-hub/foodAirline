"""another migration

Revision ID: 032b9020506e
Revises: b004518cac84
Create Date: 2022-05-20 02:55:46.061458

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '032b9020506e'
down_revision = 'b004518cac84'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('checkout', sa.Column('phone', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('checkout', 'phone')
    # ### end Alembic commands ###
