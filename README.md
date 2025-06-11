# DavidBetBackend
An api integration to manage the backend operation for users soccer bets

Estructura de carpetas (Arquitectura limpia)

betting-app-backend/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── core/            # configuración, constantes, seguridad
│   ├── db/              # setup de motor y sesión
│   ├── models/          # SQLAlchemy ↔ tablas
│   ├── schemas/         # Pydantic ↔ validación
│   ├── repositories/    # acceso a datos
│   ├── services/        # lógica de negocio (SerpApi, apuestas…)
│   ├── api/             # routers (v1/users.py, v1/bets.py)
│   └── dependencies.py  # dependencias de FastAPI
├── .env
├── .gitignore
└── README.md
