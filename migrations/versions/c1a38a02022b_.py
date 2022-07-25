"""empty message

Revision ID: c1a38a02022b
Revises: c2d837df8f3f
Create Date: 2022-07-22 10:20:50.703711

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c1a38a02022b'
down_revision = 'c2d837df8f3f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('courseteachers',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('courses_id', sa.Integer(), nullable=True, comment='关联课程id'),
    sa.Column('teacher_id', sa.Integer(), nullable=True, comment='关联老师id'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('courseteachers')
    # ### end Alembic commands ###
