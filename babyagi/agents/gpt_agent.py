from hyperon import *
from .llmagent import ChatGPTAgent


# Example text and question
# text = "Patient exhibits multiple risk factors for skin cancer, including excessive sun exposure, fair skin, and a family history of the disease. The patient reports a rapidly growing lesion on their forearm, which has recently changed color and is causing discomfort. Upon examination, the lesion shows asymmetry, irregular borders, and a diameter exceeding 6mm. Given these symptoms and diagnostic criteria, there is a high likelihood of melanoma. Preventive measures, such as consistent sunscreen use, wearing protective clothing, and avoiding tanning beds, are recommended to reduce further risk."
def prompt_agent(metta: MeTTa, *args):

    for atom in args:
        text = str(atom) 

    gpt_agent = ChatGPTAgent()
    prompt = f'''
    Your task is to extract triples from a text. Below are some examples of triples:

    (isTypeOf BasalCellCarcinoma SkiCancer)
    (isTypeOf  SquamousellCarcinoma  SkinCancer)
    (isTypeOf  Melanoma  SkinCancer)
    (hasDiagnosticCriterion  SkinCancer  Asymmetry)
    (hasDiagnosticCriterion  SkinCancer  BorderIrregularity)
    (hasDiagnosticCriterion  SkinCancer  Diameter)
    (hasSymptom SkinCancer Growth)
    (hasSymptom SkinCancer ColorChange)
    (hasSymptom SkinCancer Pain)
    (hasRiskFactor SkinCancer SunExposure)
    (hasRiskFactor SkinCancer FairSkin)
    (hasRiskFactor SkinCancer FamilyHistory)

    The text: {text}
    Note: return only the triples.
    '''
    messages = [
        {"role": "user", "content": prompt}
    ]
    answer = gpt_agent(messages, functions=[])
    atoms = metta.parse_all(answer.content)
    return [ValueAtom(atoms, 'Expression')]

# prompt_agent(text)