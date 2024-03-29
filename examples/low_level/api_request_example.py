from typing import NoReturn

from telefone.api import API

# Make an API with a token from an environment variable.
api = API(__import__("os").getenv("token"))


async def main() -> NoReturn:
    # Make a single API request.
    print(await api.request("getMe", {}))

    # Make multiple API requests from one session.
    async for response in api.request_many(
        [api.APIRequest("getMe", {}), api.APIRequest("getUpdates", {})]
    ):
        print(response)


# Run an example function in the current event loop.
__import__("asyncio").get_event_loop().run_until_complete(main())
