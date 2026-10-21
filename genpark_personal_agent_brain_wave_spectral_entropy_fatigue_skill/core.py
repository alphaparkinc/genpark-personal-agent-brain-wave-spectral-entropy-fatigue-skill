# -*- coding: utf-8 -*-
"""EEG Spectral Entropy & Mental Fatigue Tracker for GenPark Personal Agent."""
import json
import math
from typing import Dict, Any

class EEGSpectralEntropyMentalFatigueTracker:
    @staticmethod
    def calculate_theta_beta_ratio_and_entropy(theta_power_uv2: float, beta_power_uv2: float, alpha_power_uv2: float = 1.0) -> Dict[str, Any]:
        tbr = round(theta_power_uv2 / max(0.1, beta_power_uv2), 2)
        total_p = theta_power_uv2 + beta_power_uv2 + alpha_power_uv2
        
        # Shannon Spectral Entropy
        p_theta = theta_power_uv2 / total_p
        p_beta = beta_power_uv2 / total_p
        p_alpha = alpha_power_uv2 / total_p
        entropy = - (p_theta * math.log(max(1e-6, p_theta)) + p_beta * math.log(max(1e-6, p_beta)) + p_alpha * math.log(max(1e-6, p_alpha)))
        entropy_normalized = round(min(1.0, max(0.0, entropy / math.log(3.0))), 2)
        
        fatigue_tier = "ACUTE_EXECUTIVE_EXHAUSTION" if tbr >= 4.0 else ("MODERATE_COGNITIVE_STRAIN" if tbr >= 2.5 else "OPTIMAL_ALERTNESS_FOCUS")
        return {
            "theta_beta_ratio_tbr": tbr,
            "normalized_spectral_entropy": entropy_normalized,
            "cognitive_fatigue_tier": fatigue_tier,
            "prefrontal_cortex_alertness": "HIGH" if tbr < 2.5 else "IMPAIRED"
        }

    @staticmethod
    def synthesize_neuro_recovery_non_sleep_deep_rest_protocol(fatigue_index_score: float, available_break_minutes: int = 20) -> Dict[str, Any]:
        duration = min(30, max(10, available_break_minutes))
        interventions = [
            f"{duration}-minute guided Yoga Nidra / NSDR audio with eyes covered",
            "10Hz Alpha binaural beat entrainment with isochronic tones",
            "Cool mist facial hydration to trigger trigeminal dive reflex and downregulate autonomic arousal"
        ]
        return {
            "fatigue_score": fatigue_index_score,
            "session_duration_minutes": duration,
            "restorative_protocol": interventions,
            "expected_neuro_outcome": "Resets dopamine receptor sensitivity and clears adenosine pressure for 3+ hours."
        }
