from nonebot_plugin_marshoai.plugin import PluginMetadata

from .file_io import *
from .manager import *
from .network import *

__marsho_meta__ = PluginMetadata(
    name="内置增强组件",
    version="0.0.1",
    description="内置工具插件",
    author="MarshoTeam of LiteyukiStudio",
)