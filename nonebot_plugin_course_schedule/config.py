from pydantic import BaseModel, Field
from pathlib import Path

from nonebot import get_plugin_config

# fmt:off
class Config(BaseModel):
    course_font_path: str = Field(default_factory=lambda: str(
        Path(__file__).parent / "resources" / "MapleMono-NF-CN-Medium.ttf"
    ))
    # 群聊黑名单
    course_group_blacklist: list[int] = Field(default_factory=list)
# fmt:on

config = get_plugin_config(Config)
