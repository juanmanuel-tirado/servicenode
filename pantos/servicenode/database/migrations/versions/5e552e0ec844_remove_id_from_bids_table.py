"""remove_id_from_bids_table

Revision ID: 5e552e0ec844
Revises: bd913c5bfdfb
Create Date: 2024-01-15 10:11:31.137322

"""
import sqlalchemy as sa  # type: ignore
from alembic import op

# revision identifiers, used by Alembic.
revision = '5e552e0ec844'
down_revision = 'bd913c5bfdfb'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('bids', 'id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        'bids',
        sa.Column('id', sa.INTEGER(),
                  server_default=sa.text("nextval('bids_id_seq'::regclass)"),
                  autoincrement=True, nullable=False))
    # ### end Alembic commands ###
