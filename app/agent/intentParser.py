import json
from app.agent.baseAgent import BaseAgent


class IntentParser(BaseAgent):

    def run(self, instruction: str):
        prompt_data = {
            "system": "You are a browser automation planning agent.",
            "instruction": instruction,
            "rules": {
                "output": [
                    "Output MUST be valid JSON only",
                    # "Do NOT include explanations",
                    # "Do NOT include markdown",
                    "Do NOT wrap the JSON in code fences",
                    # "Do NOT include comments",
                    "Do NOT add fields not defined in the schema",
                    "All required fields MUST exist",
                    "Use standard ASCII JSON syntax only",
                    # "Use only double quotes",
                    # "Do not use smart quotes",
                    # "Do not use trailing commas",
                    # "Do not output any text before or after the JSON",
                    "The output must be directly parseable by a standard JSON parser"
                ],
                "general": [
                    "Each step must be atomic",
                    "Step numbers must start at 1 and increment by 1",
                    "Use only allowed step types: navigate, click, fill, press, wait_for, extract, finish",
                    "Use minimum steps necessary",
                    "Use clear and realistic descriptions",
                    "Prefer stable selectors",
                    "Include starting URL if implied"
                ],
                "target_rules": {
                    "required_fields": ["description", "match", "keywords"],
                    "keywords_rules": [
                        "At least 10 keywords",
                        "At least 5 Korean",
                        "At least 5 English",
                        "Use synonyms and variations",
                        "Do not repeat similar words"
                    ]
                },
                "step_rules": {
                    "navigate": ["args.url required", "no target"],
                    "click": ["target required"],
                    "fill": ["target required", "args.text required"],
                    "press": ["args.key required"],
                    "wait_for": ["target required"],
                    "extract": ["target required"],
                    "finish": ["args.message required"]
                }
                # ,
                # "safety": [
                #         "Set requires_confirmation true for sensitive actions",
                #         "Keep allow_on_sensitive_page false unless explicitly intended"
                # ]
            },
            "example": {
                "task_id": "short_unique_task_id",
                "goal": "clear one-sentence goal",
                "site": "https://example.com/",
                "steps": [
                    {
                        "step": 1,
                        "type": "navigate",
                        "args": {
                            "url": "https://example.com/"
                        }
                    },
                    {
                        "step": 2,
                        "type": "click",
                        "target": {
                            "description": "element description",
                            "match": {
                                "role": "button",
                                "text": "example text"
                            },
                            "keywords": [
                                "한국어키워드1",
                                "한국어키워드2",
                                "한국어키워드3",
                                "한국어키워드4",
                                "한국어키워드5",
                                "english keyword 1",
                                "english keyword 2",
                                "english keyword 3",
                                "english keyword 4",
                                "english keyword 5"
                            ],
                            "fallbacks": [
                                {
                                    "role": "button",
                                    "text": "example text"
                                },
                                {
                                    "css": "button"
                                }
                            ],
                            "frame_scope": "all_frames",
                            "index": 0,
                            "reuse_previous_target": False
                        }
                    },
                    {
                        "step": 3,
                        "type": "finish",
                        "args": {
                            "message": "task completed"
                        }
                    }
                ]
            },
            "final_instruction": "Return JSON only. Do not output any non-JSON text."
        }

        prompt = json.dumps(prompt_data, ensure_ascii=False, indent=2)
        # pretty_json = json.dumps(json.loads(result), indent=4, ensure_ascii=False)

        result = self.llm.generate(prompt)

        return json.loads(result)

    def run_prompt(self, instruction: str, prompt:dict):

        prompt["instruction"] = instruction


        prompt = json.dumps(prompt, ensure_ascii=False, indent=2)
        # pretty_json = json.dumps(json.loads(result), indent=4, ensure_ascii=False)

        result = self.llm.generate(prompt)

        return json.loads(result)

