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
    SameLineLayout,
)
from text_renderer.effect.curve import Curve

CURRENT_DIR = Path(os.path.abspath(os.path.dirname(__file__)))

# python main.py --config app_en_pinjie/my_test.py --dataset img --num_processes 2 --log_period 10
def story_data():
    return GeneratorCfg(
        num_image=20000,
        save_dir=CURRENT_DIR / "../../data/text_renderer_en/henxian/train_data",
        render_cfg=RenderCfg(
            bg_dir=CURRENT_DIR / "bg",
            height=60,
            # perspective_transform=NormPerspectiveTransformCfg(5, 5, 1.2),
            corpus=CharCorpus(
                CharCorpusCfg(
                    text_paths=[CURRENT_DIR / "text" / "eng_text.txt"],
                    font_dir=CURRENT_DIR / "../app_en_gen/font",
                    font_size=(60, 65),
                    char_spacing=(-0.13, -0.08),
                    length=(40, 50),
                    text_color_cfg=FixedTextColorCfg(),
                ),
            ),
            corpus_effects=Effects(
                [
                    # Padding(p=1, w_ratio=(0.2, 0.21), h_ratio=(0.7, 0.71), center=True),
                    Curve(p=1, period=180, amplitude=(2, 3)),
                ]
            ),
            # corpus_effects=Effects(Line(0.95, thickness=(5, 6), line_pos_p=[0, 0.6, 0, 0, 0, 0, 0, 0, 0.4, 0],
            #                             color_cfg=FixedTextColorCfg(), tb_in_offset=(0, 1))),
            gray=False,
        ),
    )

# def story1_data():
#     return GeneratorCfg(
#         num_image=10000,
#         save_dir=CURRENT_DIR / "F:/fix_bug/data/text_renderer_en/train_data",
#         render_cfg=RenderCfg(
#             bg_dir=CURRENT_DIR / "bg",
#             height=41,
#             perspective_transform=NormPerspectiveTransformCfg(20, 20, 1.2),
#             corpus=CharCorpus(
#                 CharCorpusCfg(
#                     text_paths=[CURRENT_DIR / "text" / "text.txt"],
#                     font_dir=CURRENT_DIR / "../bg1_gen/font",
#                     font_size=(37, 38),
#                     char_spacing=(0.13, 0.13),
#                     length=(1, 20),
#                     text_color_cfg=FixedTextColorCfg(),
#                 ),
#             ),
#             corpus_effects=Effects(Line(0.001, thickness=(2, 3))),
#             gray=False,
#         ),
#     )

def story2_data():
    return GeneratorCfg(
        num_image=5000,
        save_dir=CURRENT_DIR / "../../data/text_renderer_en/henxian/test_data",
        render_cfg=RenderCfg(
            bg_dir=CURRENT_DIR / "bg",
            height=40,
            # perspective_transform=NormPerspectiveTransformCfg(5, 5, 1.2),
            corpus_effects=Effects(
                [
                    # Padding(p=1, w_ratio=(0.2, 0.21), h_ratio=(0.7, 0.71), center=True),
                    Curve(p=1, period=180, amplitude=(2, 3)),
                ]
            ),
            corpus=CharCorpus(
                CharCorpusCfg(
                    text_paths=[CURRENT_DIR / "text" / "eng_text.txt"],
                    font_dir=CURRENT_DIR / "../app_en_gen/font",
                    font_size=(100, 101),
                    char_spacing=(-0.13, -0.08),
                    length=(40, 50),
                    text_color_cfg=FixedTextColorCfg(),
                ),
            ),
            # corpus_effects=Effects(Line(0.95, thickness=(5, 6), line_pos_p=[0, 0.6, 0, 0, 0, 0, 0, 0, 0.4, 0],
            #                             color_cfg=FixedTextColorCfg(), tb_in_offset=(0, 1))),
            gray=False,
        ),
    )

# configs = [story_data()]
configs = [story_data(), story2_data()]
# python main.py --config app_en_gen/mytest.py --dataset img --num_processes 4 --log_period 100
