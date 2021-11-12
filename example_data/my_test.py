# python3.7
# -*- coding: utf-8 -*-
# @Author : listen
# @Time   :
import os
from pathlib import Path

from text_renderer.effect import *
from text_renderer.corpus import *
from text_renderer.config import (
    RenderCfg,
    NormPerspectiveTransformCfg,
    GeneratorCfg,
    SimpleTextColorCfg,
    TextColorCfg,
    FixedTextColorCfg,
)

CURRENT_DIR = Path(os.path.abspath(os.path.dirname(__file__)))


def story_data():
    return GeneratorCfg(
        num_image=10,
        save_dir=CURRENT_DIR / "output",
        render_cfg=RenderCfg(
            bg_dir=CURRENT_DIR / "bg",
            height=76,
            perspective_transform=NormPerspectiveTransformCfg(20, 20, 1.5),
            corpus=CharCorpus(
                CharCorpusCfg(
                    text_paths=[CURRENT_DIR / "text" / "chn_text.txt"],
                    font_dir=CURRENT_DIR / "font",
                    font_size=(45, 55),
                    char_spacing=(0.1, 0.1),
                    length=(1, 20),
                    text_color_cfg=FixedTextColorCfg(),
                ),
            ),
            corpus_effects=Effects(Line(0.1, thickness=(2, 5))),
            gray=False,
        ),
    )


configs = [story_data()]