"""empty message

Revision ID: 1f3c8d3e4a93
Revises: be3e3bdcb87e
Create Date: 2020-03-29 15:25:11.996923

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1f3c8d3e4a93'
down_revision = 'be3e3bdcb87e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('Us', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['Us'], ['USER.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('content')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post')
    # ### end Alembic commands ###
