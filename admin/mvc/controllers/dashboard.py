from flask import request
from flask_restful import Resource, abort
from admin.managers.security import SecurityCallback, SecurityManager
from core.managers.auth.oauth import OAuth2Manager
from defines import PERMISSIONS
import psutil


class DashboardProvider(Resource):
    """
    ## Dashboard Provider

    """
    def __init__(self) -> None:
        super().__init__()
        self.manager = OAuth2Manager()
        self.security = SecurityManager()
        self.SCB = SecurityCallback
    
    def get(self):
        auth_token = request.headers.get("Authorization", None)

        if not auth_token:
            abort(401, message="Authentication required")
        
        if not auth_token.startswith("Bearer"):
            abort(401, message="Authentication required")

        token = auth_token.split(" ")[1]
        # try:
        #     get_user = self.manager.get_current_user(auth_token[1])
        
        # except:
        #     abort(401, message="Unauthorized user")

        
        # get virtual memory statistics
        virtual_memory = psutil.virtual_memory()
        central_processing_units = psutil.cpu_percent()

        # 1. get the memory used in bytes
        # 2. get the total memory available in bytes
        memory_used = virtual_memory.used
        memory_total = virtual_memory.total

        response_type = {
            "memory": {
                "used": psutil._common.bytes2human(memory_used),
                "total": psutil._common.bytes2human(memory_total),
            },
            "cpu": central_processing_units
        }
        return self.security.logged_or_respond(token, self.SCB(abort, 401, message="Unauthorized user"), (response_type, 200))