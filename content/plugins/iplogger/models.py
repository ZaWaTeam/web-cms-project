from core.plugins.model import *


class IPLog(PluginModel):
    id = AutoField()
    ip = IPField()


ModelController.create_model_tables([IPLog])
