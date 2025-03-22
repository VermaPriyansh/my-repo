# backend/app/core/prompt_processor.py
from typing import List, Dict, Any, Optional
import asyncio
import logging

from app.models.language_detector import LanguageDetector
from app.models.grammar_corrector import GrammarCorrector
from app.models.toxicity_classifier import ToxicityClassifier
from app.models.cultural_adapter import CulturalAdapter
from app.models.prompt_optimizer import PromptOptimizer

logger = logging.getLogger("prompt_processor")

class PromptProcessor:
    def __init__(self):
        self.stages = [
            LanguageDetector(),        # Custom FastText model
            GrammarCorrector(),        # GECToR fine-tuned
            ToxicityClassifier(),      # Multi-headed RoBERTa
            CulturalAdapter(),         # Azure Custom Translator
            PromptOptimizer()          # OpenPrompt framework
        ]
    
    async def process(
        self, 
        text: str, 
        source_language: Optional[str] = None,
        target_language: Optional[str] = None,
        options: Dict[str, Any] = {}
    ) -> Dict[str, Any]:
        """
        Process a prompt through the validation pipeline
        """
        start_time = asyncio.get_event_loop().time()
        context = {
            "original_text": text,
            "current_text": text,
            "source_language": source_language,
            "target_language": target_language,
            "options": options,
            "issues": [],
            "metrics": {},
            "suggestions": []
        }
        
        try:
            # Apply each stage in the pipeline
            for stage in self.stages:
                stage_name = stage.__class__.__name__
                logger.info(f"Running stage: {stage_name}")
                
                # Apply the current stage
                context = await stage.process(context)
                
                # Sanity check
                if "current_text" not in context:
                    logger.warning(f"Stage {stage_name} did not return current_text!")
                    
            # Calculate processing time
            elapsed = asyncio.get_event_loop().time() - start_time
            context["metrics"]["processing_time_ms"] = round(elapsed * 1000, 2)
            
            # Create the final response
            return {
                "original_text": context["original_text"],
                "validated_text": context["current_text"],
                "issues": context["issues"],
                "metrics": context["metrics"],
                "suggestions": context["suggestions"]
            }
            
        except Exception as e:
            logger.error(f"Error in prompt processing pipeline: {str(e)}")
            raise
