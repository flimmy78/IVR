"""create init tables

Revision ID: 6e1fe9c20c6
Revises: 
Create Date: 2015-12-24 01:36:15.358182

"""

# revision identifiers, used by Alembic.
revision = '6e1fe9c20c6'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('project',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('name', sa.String(length=64, convert_unicode=True), nullable=False),
    sa.Column('title', sa.String(length=255, convert_unicode=True), server_default=u'', nullable=False),
    sa.Column('desc', sa.String(length=255, convert_unicode=True), server_default=u'', nullable=False),
    sa.Column('long_desc', sa.String(length=1024, convert_unicode=True), server_default=u'', nullable=False),
    sa.Column('ctime', sa.TIMESTAMP(), server_default=sa.text(u'0'), nullable=False),
    sa.Column('utime', sa.TIMESTAMP(), server_default=sa.text(u'CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('max_media_sessions', sa.Integer(), server_default=sa.text(u'0'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_project_name'), 'project', ['name'], unique=True)
    op.create_table('user',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('username', sa.String(length=64, convert_unicode=True), nullable=False),
    sa.Column('password', sa.String(length=64, convert_unicode=True), server_default=u'', nullable=False),
    sa.Column('title', sa.String(length=255, convert_unicode=True), server_default=u'', nullable=False),
    sa.Column('desc', sa.String(length=255, convert_unicode=True), server_default=u'', nullable=False),
    sa.Column('long_desc', sa.String(length=1024, convert_unicode=True), server_default=u'', nullable=False),
    sa.Column('cellphone', sa.String(length=32, convert_unicode=True), server_default=u'', nullable=False),
    sa.Column('email', sa.String(length=64, convert_unicode=True), server_default=u'', nullable=False),
    sa.Column('ctime', sa.TIMESTAMP(), server_default=sa.text(u'0'), nullable=False),
    sa.Column('utime', sa.TIMESTAMP(), server_default=sa.text(u'CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('ltime', sa.TIMESTAMP(), server_default=sa.text(u'0'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.create_table('device',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('uuid', sa.CHAR(length=36, convert_unicode=True), nullable=False),
    sa.Column('name', sa.String(length=255, convert_unicode=True), server_default=u'', nullable=False),
    sa.Column('type', sa.String(length=32, convert_unicode=True), server_default=u'IVT', nullable=False),
    sa.Column('firmware_model', sa.String(length=255, convert_unicode=True), server_default=u'', nullable=False),
    sa.Column('hardware_model', sa.String(length=255, convert_unicode=True), server_default=u'', nullable=False),
    sa.Column('media_channel_num', sa.Integer(), server_default=sa.text(u'0'), nullable=False),
    sa.Column('desc', sa.String(length=255, convert_unicode=True), server_default=u'', nullable=False),
    sa.Column('long_desc', sa.String(length=1024, convert_unicode=True), server_default=u'', nullable=False),
    sa.Column('longitude', sa.Float(), server_default=u'0.0', nullable=False),
    sa.Column('latitude', sa.Float(), server_default=u'0.0', nullable=False),
    sa.Column('altitude', sa.Float(), server_default=u'0.0', nullable=False),
    sa.Column('project_name', sa.String(length=64, convert_unicode=True), server_default=u'', nullable=False),
    sa.Column('flags', sa.Integer(), server_default=sa.text(u'0'), nullable=False),
    sa.Column('is_online', sa.Boolean(), server_default=sa.text(u'0'), nullable=False),
    sa.Column('login_code', sa.String(length=64, convert_unicode=True), nullable=False),
    sa.Column('login_passwd', sa.String(length=64, convert_unicode=True), server_default=u'', nullable=False),
    sa.Column('ctime', sa.TIMESTAMP(), server_default=sa.text(u'0'), nullable=False),
    sa.Column('utime', sa.TIMESTAMP(), server_default=sa.text(u'CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('ltime', sa.TIMESTAMP(), server_default=sa.text(u'0'), nullable=False),
    sa.ForeignKeyConstraint(['project_name'], [u'project.name'], onupdate=u'CASCADE', ondelete=u'CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_device_login_code'), 'device', ['login_code'], unique=True)
    op.create_index(op.f('ix_device_uuid'), 'device', ['uuid'], unique=True)
    op.create_table('project_user_relation',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('user_username', sa.String(length=64, convert_unicode=True), nullable=False),
    sa.Column('project_name', sa.String(length=64, convert_unicode=True), nullable=False),
    sa.ForeignKeyConstraint(['project_name'], [u'project.name'], onupdate=u'CASCADE', ondelete=u'CASCADE'),
    sa.ForeignKeyConstraint(['user_username'], [u'user.username'], onupdate=u'CASCADE', ondelete=u'CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('camera',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('uuid', sa.CHAR(length=36, convert_unicode=True), nullable=False),
    sa.Column('device_uuid', sa.CHAR(length=36, convert_unicode=True), server_default=u'', nullable=False),
    sa.Column('channel_index', sa.Integer(), server_default=sa.text(u'0'), nullable=False),
    sa.Column('name', sa.String(length=255, convert_unicode=True), server_default=u'', nullable=False),
    sa.Column('desc', sa.String(length=255, convert_unicode=True), server_default=u'', nullable=False),
    sa.Column('long_desc', sa.String(length=1024, convert_unicode=True), server_default=u'', nullable=False),
    sa.Column('longitude', sa.Float(), server_default=u'0.0', nullable=False),
    sa.Column('latitude', sa.Float(), server_default=u'0.0', nullable=False),
    sa.Column('altitude', sa.Float(), server_default=u'0.0', nullable=False),
    sa.Column('project_name', sa.String(length=64, convert_unicode=True), server_default=u'', nullable=False),
    sa.Column('flags', sa.Integer(), server_default=sa.text(u'0'), nullable=False),
    sa.Column('is_online', sa.Boolean(), server_default=sa.text(u'0'), nullable=False),
    sa.Column('ctime', sa.TIMESTAMP(), server_default=sa.text(u'0'), nullable=False),
    sa.Column('utime', sa.TIMESTAMP(), server_default=sa.text(u'CURRENT_TIMESTAMP'), nullable=False),
    sa.ForeignKeyConstraint(['device_uuid'], [u'device.uuid'], onupdate=u'CASCADE', ondelete=u'CASCADE'),
    sa.ForeignKeyConstraint(['project_name'], [u'project.name'], onupdate=u'CASCADE', ondelete=u'CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_camera_uuid'), 'camera', ['uuid'], unique=True)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_camera_uuid'), table_name='camera')
    op.drop_table('camera')
    op.drop_table('project_user_relation')
    op.drop_index(op.f('ix_device_uuid'), table_name='device')
    op.drop_index(op.f('ix_device_login_code'), table_name='device')
    op.drop_table('device')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_project_name'), table_name='project')
    op.drop_table('project')
    ### end Alembic commands ###
