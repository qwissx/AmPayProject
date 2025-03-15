from fastapi import FastAPI
from fastapi.openapi.docs import (
    get_swagger_ui_html,
    get_swagger_ui_oauth2_redirect_html,
)

from ampay.routers.auth import auth_router
from ampay.routers.payments import pay_router


app = FastAPI(docs_url=None)

app.include_router(auth_router)
app.include_router(pay_router)


@app.get("/", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + " - Swagger UI",
        oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
        swagger_js_url=f"https://unpkg.com/swagger-ui-dist@5.18.2/swagger-ui-bundle.js",
        swagger_css_url=f"https://unpkg.com/swagger-ui-dist@5.18.2/swagger-ui.css",
    )
