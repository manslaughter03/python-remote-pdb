from aiohttp import web

async def get_users(request):
    return web.json_response([{"id": "123456", "username": "osirius"}])

def main():
    app = web.Application()
    app.add_routes([web.get('/users', get_users)])
    web.run_app(app)

if __name__ == '__main__':
    main()
