from brain.ollama_client import OllamaClient
from brain.gemma_client import GemmaClient
from brain.kimi_client import KimiClient
from brain.phi_client import PhiClient

gemma = GemmaClient()
kimi = KimiClient()
ollama = OllamaClient()
phi = PhiClient()

class LLMInterface:
    
    def generate(self , prompt):
        # return phi.generate(prompt)
        return kimi.generate(prompt)
        return gemma.generate(prompt)
        return ollama.generate(prompt)