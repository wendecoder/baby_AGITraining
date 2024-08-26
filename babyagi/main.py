from hyperon import *
from hyperon.ext import register_atoms
from .agents import *

@register_atoms(pass_metta=True)
def babyagi_atoms(metta):
    gptAtom = OperationAtom('gpt', lambda *args: prompt_agent(metta, *args), [AtomType.ATOM, "Expression"], unwrap=False)
    cnnAtom = OperationAtom('cnn', lambda *args: detect_skin_cancer(metta, *args), unwrap=False)

    return {
        r"gpt": gptAtom,
        r"cnn": cnnAtom
    }