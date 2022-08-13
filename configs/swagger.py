from eve import Eve
from eve_swagger import get_swagger_blueprint


def config_swagger(app: Eve) -> None:
    swagger = get_swagger_blueprint()
    app.register_blueprint(swagger)

    app.config['SWAGGER_INFO'] = {
        'title': 'Sinergija v2 API',
        'version': '1.0',
        'description': '',
        'termsOfService': '',
        'contact': {
            'name': 'Nikola Ajzenhamer',
            'url': 'https://nikolaajzenhamer.rs'
        },
        'license': {
            'name': 'GPL-3.0',
            'url': 'https://github.com/ajzenhamernikola/sinergija-v2/blob/main/LICENSE',
        },
        'schemes': ['http'],
    }
