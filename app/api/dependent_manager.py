from functools import lru_cache

from app.agent.baseAgent import BaseAgent
from app.agent.intentParser import IntentParser
from app.infra.llm.client import LLMClient
from app.service.agentService import AgentService


@lru_cache
def get_agent_service():
    return AgentService(get_intent_parser())

@lru_cache
def get_intent_parser()-> IntentParser:
    return IntentParser(get_llm_client())

@lru_cache
def get_base_agent()-> BaseAgent:
    return BaseAgent(get_llm_client())

@lru_cache
def get_llm_client():
   return LLMClient()