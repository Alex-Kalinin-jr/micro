"""revision_number_five

Revision ID: 88a5fd5afaf5
Revises: 105fb8d77417
Create Date: 2024-05-14 22:19:33.060472

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '88a5fd5afaf5'
down_revision: Union[str, None] = '105fb8d77417'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
