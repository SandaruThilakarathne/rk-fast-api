"""meal

Revision ID: d77e08362c12
Revises: b6e2546e1c6a
Create Date: 2022-02-23 08:37:36.697744

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd77e08362c12'
down_revision = 'b6e2546e1c6a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('meal-plan',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=250), nullable=True),
    sa.Column('meal_plan_link', sa.String(length=250), nullable=True),
    sa.Column('body', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['body'], ['body-type.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_meal-plan_id'), 'meal-plan', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_meal-plan_id'), table_name='meal-plan')
    op.drop_table('meal-plan')
    # ### end Alembic commands ###
