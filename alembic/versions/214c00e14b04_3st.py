"""3st

Revision ID: 214c00e14b04
Revises: 65affe0e0f71
Create Date: 2020-09-21 01:36:57.520907

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '214c00e14b04'
down_revision = '65affe0e0f71'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###

    op.create_table('df',
    sa.Column('index', sa.BIGINT(), nullable=True),
    sa.Column('int', sa.BIGINT(), nullable=True),
    sa.Column('str', sa.TEXT(), nullable=True),
    sa.Column('float', sa.FLOAT(), nullable=True)
    )
    op.create_index('ix_df_index', 'df', ['index'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_df_index', table_name='df')
    op.drop_table('df')
    # ### end Alembic commands ###
