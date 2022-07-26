"""empty message

Revision ID: c2d837df8f3f
Revises: b7c1d38b3bd4
Create Date: 2022-07-22 10:15:39.309562

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'c2d837df8f3f'
down_revision = 'b7c1d38b3bd4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('courses',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=16), nullable=False, comment='课程名字'),
    sa.Column('info', sa.String(length=256), nullable=True, comment='简介'),
    sa.Column('create_time', sa.DateTime(), nullable=True, comment='创建时间'),
    sa.Column('start_time', sa.DateTime(), nullable=True, comment='开课时间'),
    sa.Column('end_time', sa.DateTime(), nullable=True, comment='结束时间'),
    sa.Column('total', sa.DateTime(), nullable=True, comment='本课程包含几节课'),
    sa.Column('total_time', sa.Integer(), nullable=True, comment='总时长（秒数）'),
    sa.Column('photo', sa.String(length=256), nullable=True, comment='书皮'),
    sa.Column('money', sa.Float(precision=5, asdecimal=2), nullable=True, comment='价格'),
    sa.Column('type', sa.Integer(), nullable=True, comment='{1:特色课，2:一对一}'),
    sa.Column('teacher_num', sa.Integer(), nullable=True, comment='讲师人数'),
    sa.Column('collect_num', sa.Integer(), nullable=True, comment='收藏量'),
    sa.Column('course_num', sa.Integer(), nullable=True, comment='预约量'),
    sa.Column('buy_num', sa.Integer(), nullable=True, comment='购买量'),
    sa.Column('solo_num', sa.Integer(), nullable=True, comment='一对一课数量'),
    sa.Column('vip_free', sa.DateTime(), nullable=True, comment='会员'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('excerpts',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('courses_id', sa.Integer(), nullable=True, comment='关联课程id'),
    sa.Column('name', sa.String(length=16), nullable=False, comment='课节名字'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_excerpts_courses_id'), 'excerpts', ['courses_id'], unique=False)
    op.add_column('students', sa.Column('vip', sa.DateTime(), nullable=True, comment='会员'))
    op.drop_column('students', 'vippp')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('students', sa.Column('vippp', mysql.DATETIME(), nullable=True, comment='会员'))
    op.drop_column('students', 'vip')
    op.drop_index(op.f('ix_excerpts_courses_id'), table_name='excerpts')
    op.drop_table('excerpts')
    op.drop_table('courses')
    # ### end Alembic commands ###
