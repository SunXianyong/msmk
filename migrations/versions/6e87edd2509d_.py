"""empty message

Revision ID: 6e87edd2509d
Revises: ea5dae98bffb
Create Date: 2022-07-22 16:17:17.886995

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6e87edd2509d'
down_revision = 'ea5dae98bffb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('courseorders',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('courses_id', sa.Integer(), nullable=True, comment='关联课程id'),
    sa.Column('courses_name', sa.String(length=16), nullable=False, comment='课程名字'),
    sa.Column('student_id', sa.Integer(), nullable=True, comment='关联老师id'),
    sa.Column('real_price', sa.Integer(), nullable=True, comment='实付价格'),
    sa.Column('price', sa.Integer(), nullable=True, comment='标价'),
    sa.Column('create_time', sa.DateTime(), nullable=True, comment='下订单时间'),
    sa.Column('fail', sa.BOOLEAN(), nullable=True, comment='退款'),
    sa.Column('coupon_id', sa.Integer(), nullable=True, comment='优惠券id'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('courseorders')
    # ### end Alembic commands ###