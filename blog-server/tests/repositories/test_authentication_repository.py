import pytest

from blog.repositories.admin import AdminRepository


@pytest.mark.asyncio
async def test_register(unauthenticated_context):
    authentication_repository = AdminRepository()

    response = await authentication_repository.register_user(
        unauthenticated_context,
        'john.smith@example.com',
        'password')
    assert response is not None

    response = authentication_repository.authenticate_user(
        unauthenticated_context,
        'john.smith@example.com',
        'password')
    assert response is not None
