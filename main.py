from app.app import create_app
from settings import GET

app = create_app()

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app=app,
                host=GET.HOST,
                port=GET.PORT)
