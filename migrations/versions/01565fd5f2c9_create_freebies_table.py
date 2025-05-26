"""create freebies table"""

from alembic import op
import sqlalchemy as sa

revision = '20240526'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'freebies',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('item_name', sa.String(), nullable=False),
        sa.Column('value', sa.Integer(), nullable=False),
        sa.Column('company_id', sa.Integer(), sa.ForeignKey('companies.id')),
        sa.Column('dev_id', sa.Integer(), sa.ForeignKey('devs.id')),
    )

def downgrade():
    op.drop_table('freebies')
