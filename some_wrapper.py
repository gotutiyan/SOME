from some import Scorer
from transformers import AutoTokenizer
from dataclasses import dataclass

@dataclass
class Dataclass_for_args:
    g_dir: str = None
    f_dir: str = None
    m_dir: str = None
    batch_size: int = None
    weight_g: float = None
    weight_f: float = None
    weight_m: float = None
    model_type: float = None

class SOME_Wrapper:
    def __init__(
        self,
        g_dir,
        f_dir,
        m_dir,
        batch_size,
        weight_g,
        weight_f,
        weight_m,
    ):
        self.args = Dataclass_for_args(
            g_dir=g_dir,
            f_dir=f_dir,
            m_dir=m_dir,
            batch_size=batch_size,
            weight_g=weight_g,
            weight_f=weight_f,
            weight_m=weight_m,
            model_type='bert-base-cased'
        )
        self.some = Scorer(self.args)

    def score(self, srcs, trgs):
        self.some.add(srcs, trgs)
        return self.some.score()
    
import argparse

def main(args):
    some = SOME_Wrapper(
        g_dir='gfm-models/grammer',
        f_dir='gfm-models/fluency',
        m_dir='gfm-models/meaning',
        batch_size=5,
        weight_g=0.55,
        weight_f=0.43,
        weight_m=0.02
    )
    srcs = [
        'This is a sample sentence .',
        'This is an another sample sentene .'
    ]
    trgs = [
        'This a is sample sentence .',
        'This is another sample sentence .'
    ]
    scores = some.score(srcs, trgs)
    print(scores) # [0.7722907622655234, 0.9522199455897014]
    

def get_parser():
    parser = argparse.ArgumentParser()
    # parser.add_argument('--input', required=True)
    # parser.add_argument('--output', required=True)
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = get_parser()
    main(args)

        