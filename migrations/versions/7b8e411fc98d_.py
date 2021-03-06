"""empty message

Revision ID: 7b8e411fc98d
Revises: 3032a4892d39
Create Date: 2020-09-04 09:56:27.712886

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7b8e411fc98d'
down_revision = '3032a4892d39'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todos', sa.Column('completed', sa.Boolean(), nullable=True))

    op.execute('UPDATE todos SET completed = False WHERE completed IS NULL;')

    op.alter_column('todos', 'completed', nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('todos', 'completed')
    # ### end Alembic commands ###
