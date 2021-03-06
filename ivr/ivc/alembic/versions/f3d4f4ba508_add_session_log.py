"""Add session log

Revision ID: f3d4f4ba508
Revises: 6e1fe9c20c6
Create Date: 2016-01-10 23:22:48.575319

"""

# revision identifiers, used by Alembic.
revision = 'f3d4f4ba508'
down_revision = '6e1fe9c20c6'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sessionlog',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('uuid', sa.CHAR(length=36, convert_unicode=True), nullable=False),
    sa.Column('project_name', sa.String(length=64, convert_unicode=True), server_default=u'', nullable=False),
    sa.Column('camera_uuid', sa.CHAR(length=36, convert_unicode=True), server_default=u'', nullable=False),
    sa.Column('stream_format', sa.CHAR(length=16, convert_unicode=True), server_default=u'', nullable=False),
    sa.Column('stream_quality', sa.CHAR(length=8, convert_unicode=True), server_default=u'', nullable=False),
    sa.Column('ip', sa.String(length=39, convert_unicode=True), server_default=sa.text(u'0'), nullable=False),
    sa.Column('user_agent', sa.String(length=255, convert_unicode=True), server_default=u'', nullable=False),
    sa.Column('username', sa.String(length=64, convert_unicode=True), server_default=u'', nullable=False),
    sa.Column('subuser', sa.String(length=64, convert_unicode=True), server_default=u'', nullable=False),
    sa.Column('start', sa.TIMESTAMP(), server_default=sa.text(u'0'), nullable=False),
    sa.Column('end', sa.TIMESTAMP(), server_default=sa.text(u'0'), nullable=False),
    sa.ForeignKeyConstraint(['camera_uuid'], [u'camera.uuid'], onupdate=u'CASCADE'),
    sa.ForeignKeyConstraint(['project_name'], [u'project.name'], onupdate=u'CASCADE', ondelete=u'CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_sessionlog_uuid'), 'sessionlog', ['uuid'], unique=True)
    op.create_index('sessionlog_list_index', 'sessionlog', [sa.text(u'project_name ASC'), sa.text(u'end ASC'), sa.text(u'uuid ASC')], unique=False)
    op.add_column(u'project', sa.Column('is_public', sa.Boolean(), server_default=sa.text(u'0'), nullable=False))
    op.add_column(u'user', sa.Column('user_type', sa.SmallInteger(), server_default=sa.text(u'0'), nullable=False))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column(u'user', 'user_type')
    op.drop_column(u'project', 'is_public')
    op.drop_index('sessionlog_list_index', table_name='sessionlog')
    op.drop_index(op.f('ix_sessionlog_uuid'), table_name='sessionlog')
    op.drop_table('sessionlog')
    ### end Alembic commands ###

