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
        num_image=30000,
        save_dir=CURRENT_DIR / "output/train_data",
        render_cfg=RenderCfg(
            bg_dir=CURRENT_DIR / "bg",
            height=41,
            perspective_transform=NormPerspectiveTransformCfg(10, 10, 1.2),
            corpus=CharCorpus(
                CharCorpusCfg(
                    text_paths=[CURRENT_DIR / "text" / "text.txt"],
                    font_dir=CURRENT_DIR / "../bg1_gen/font",
                    font_size=(37, 38),
                    char_spacing=(0.13, 0.13),
                    length=(18, 20),
                    text_color_cfg=FixedTextColorCfg(),
                ),
            ),
            corpus_effects=Effects(Line(0.001, thickness=(2, 3))),
            gray=False,
        ),
    )

def story1_data():
    return GeneratorCfg(
        num_image=10000,
        save_dir=CURRENT_DIR / "output/train_data",
        render_cfg=RenderCfg(
            bg_dir=CURRENT_DIR / "bg",
            height=41,
            perspective_transform=NormPerspectiveTransformCfg(10, 10, 1.2),
            corpus=CharCorpus(
                CharCorpusCfg(
                    text_paths=[CURRENT_DIR / "text" / "text.txt"],
                    font_dir=CURRENT_DIR / "../bg1_gen/font",
                    font_size=(37, 38),
                    char_spacing=(0.13, 0.13),
                    length=(1, 20),
                    text_color_cfg=FixedTextColorCfg(),
                ),
            ),
            corpus_effects=Effects(Line(0.001, thickness=(2, 3))),
            gray=False,
        ),
    )

def story2_data():
    return GeneratorCfg(
        num_image=1000,
        save_dir=CURRENT_DIR / "output/test_data",
        render_cfg=RenderCfg(
            bg_dir=CURRENT_DIR / "bg",
            height=41,
            perspective_transform=NormPerspectiveTransformCfg(10, 10, 1.2),
            corpus=CharCorpus(
                CharCorpusCfg(
                    text_paths=[CURRENT_DIR / "text" / "text.txt"],
                    font_dir=CURRENT_DIR / "../bg1_gen/font",
                    font_size=(37, 38),
                    char_spacing=(0.13, 0.13),
                    length=(1, 20),
                    text_color_cfg=FixedTextColorCfg(),
                ),
            ),
            corpus_effects=Effects(Line(0.005, thickness=(1, 3))),
            gray=False,
        ),
    )

# configs = [story_data()]
configs = [story_data(), story2_data(), story1_data()]