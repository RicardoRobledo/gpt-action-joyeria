from fastapi import APIRouter

from .authentication.controllers.routers import router as authentication_router
from .users.controllers.routers import router as users_router
from .training.controllers.routers import router as training_router


__author__ = "Ricardo Robledo"
__version__ = "1.0"


router = APIRouter(prefix='/api/v1')

router.include_router(authentication_router)
router.include_router(users_router)
router.include_router(training_router)
