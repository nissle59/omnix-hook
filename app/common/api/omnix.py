from httpx import AsyncClient


class APIClient(AsyncClient):
    def __init__(self, base_url: str, api_key: str) -> None:
        headers = {
            "X-API-Key": api_key
        }
        super().__init__(
            verify=False,
            headers=headers,
            base_url=base_url
        )

    async def get_users(self, referer=None):
        response = await self.get("/users")
        if response.status_code == 200:
            users = response.json().get("items")
            if not referer:
                return users
            out = []
            for user in users:
                if user.get("referred_by_id") == referer:
                    out.append(user)
            return out
        return None

    async def change_promo_group(self, user_id, promo_group_id):
        data = {
            "promo_group_id": promo_group_id
        }
        response = await self.patch(f"/users/{user_id}", json=data)
        if response.status_code == 200:
            return True
        return False
