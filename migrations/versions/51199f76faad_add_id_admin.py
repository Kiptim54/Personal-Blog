"""add id admin

Revision ID: 51199f76faad
Revises: 5e330777614f
Create Date: 2018-04-19 15:29:43.271143

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '51199f76faad'
down_revision = '5e330777614f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('is_admin', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'is_admin')
    # ### end Alembic commands ###