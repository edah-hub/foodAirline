"""a new migration

Revision ID: f730aa1c6435
Revises: f72c49185ab1
Create Date: 2022-05-19 13:11:33.806304

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f730aa1c6435'
down_revision = 'f72c49185ab1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('contacts_user_id_fkey', 'contacts', type_='foreignkey')
    op.drop_column('contacts', 'user_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('contacts', sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('contacts_user_id_fkey', 'contacts', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###