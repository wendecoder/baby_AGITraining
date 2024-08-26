# Baby AGI

Baby AGI is a project that integrates two AI techniques within a unified framework using the Hyperon framework. The project demonstrates how these AI techniques can work together as agents to perform specific AI tasks.

## The Agents

### GPT Agent
- **Purpose**: Handles conversations with the GPT language model.
- **Functionality**: In Baby AGI, this agent is used to extract facts from a person's diagnosis text. The extracted facts are represented as triples, which are used for further reasoning in the symbolic reasoner agent (written in MeTTa code).

### CNN Agent
- **Purpose**: Detects the presence of skin cancer from an image.
- **Functionality**: After analyzing the image, the agent returns the detected result as an atom, which serves as the basic unit for the symbolic reasoner agent.

### MeTTa Agent
- **Purpose**: Acts as the symbolic reasoner agent.
- **Functionality**: Calls the GPT and CNN agents, stores and reads their outputs, and reasons over them using symbolic reasoning.

## Motivation

The Baby AGI project aims to demonstrate how the Hyperon framework can be used as a unified environment to perform neural-symbolic reasoning. It shows how different AI techniques can be defined and utilized as grounded atoms within MeTTa, the programming language of the Hyperon framework.

## How to Define a Specific Agent and Register it as a Grounded Atom

In Baby AGI, the GPT and CNN agents are independently defined under the `babyagi` module within the `agents` folder. These agents are then registered as `OperationAtoms` and returned as grounded atoms inside `main.py`. This allows users to import the Baby AGI module in a MeTTa file, call the agents, and perform reasoning on the results returned by the agents.

## SetUp Guide

Clone the repo
```bash
git clone https://github.com/wendecoder/baby_AGITraining.git
```

Cd to the repo
```bash
cd baby_AGITraining
```

Install the requirements
```bash
pip install -r requirements.txt
```

Export your OPENAI_API_KEY
```bash
export OPENAI_API_KEY=<your open ai api key>
```

Run the metta file
```bash
metta run-baby-agi.metta
```