"""Initial migration

Revision ID: f39e40161613
Revises: 
Create Date: 2025-01-09 12:44:05.829792

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f39e40161613'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('rotaract_students',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('roll_no', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=150), nullable=False),
    sa.Column('gender', sa.String(length=10), nullable=True),
    sa.Column('dept', sa.String(length=100), nullable=True),
    sa.Column('start_year', sa.Integer(), nullable=False),
    sa.Column('end_year', sa.Integer(), nullable=True),
    sa.Column('mobile_no', sa.String(length=15), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_rotaract_students_email'), 'rotaract_students', ['email'], unique=True)
    op.create_index(op.f('ix_rotaract_students_id'), 'rotaract_students', ['id'], unique=False)
    op.create_index(op.f('ix_rotaract_students_roll_no'), 'rotaract_students', ['roll_no'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_rotaract_students_roll_no'), table_name='rotaract_students')
    op.drop_index(op.f('ix_rotaract_students_id'), table_name='rotaract_students')
    op.drop_index(op.f('ix_rotaract_students_email'), table_name='rotaract_students')
    op.drop_table('rotaract_students')
    # ### end Alembic commands ###
