import pytest

from ampay.dependencies import cache
from ampay.dependencies import auth


@pytest.mark.asyncio
async def test_add_and_get_token_for_cache(clean_cache):
    pass